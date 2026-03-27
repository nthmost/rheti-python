import secrets
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from . import db, mail
from .models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


class RegisterForm(FlaskForm):
    email        = StringField('Email', validators=[DataRequired(), Email()])
    display_name = StringField('Name (optional)', validators=[Length(max=100)])
    password     = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm      = PasswordField('Confirm Password',
                                 validators=[DataRequired(), EqualTo('password')])


class LoginForm(FlaskForm):
    email      = StringField('Email', validators=[DataRequired(), Email()])
    password   = PasswordField('Password', validators=[DataRequired()])
    remember   = BooleanField('Remember me')


class ForgotForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])


class ResetForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired(), Length(min=8)])
    confirm  = PasswordField('Confirm Password',
                             validators=[DataRequired(), EqualTo('password')])


def send_verification_email(user):
    token = secrets.token_urlsafe(32)
    user.verify_token = token
    db.session.commit()
    link = url_for('auth.verify_email', token=token, _external=True)
    msg = Message(
        subject='Verify your email — RHETI Enneagram Test',
        recipients=[user.email],
        body=(
            f'Hi{" " + user.display_name if user.display_name else ""},\n\n'
            f'Click the link below to verify your email address:\n\n{link}\n\n'
            'This link expires when you use it.\n\n— RHETI'
        )
    )
    mail.send(msg)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('test.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data.lower()).first():
            flash('An account with that email already exists.', 'error')
            return render_template('auth/register.html', form=form)
        user = User(
            email=form.email.data.lower(),
            display_name=form.display_name.data.strip() or None,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        try:
            send_verification_email(user)
            flash('Account created! Check your email to verify your address.', 'success')
        except Exception:
            flash('Account created! (Email verification unavailable right now.)', 'warning')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@bp.route('/verify/<token>')
def verify_email(token):
    user = User.query.filter_by(verify_token=token).first_or_404()
    user.email_verified = True
    user.verify_token = None
    db.session.commit()
    login_user(user)
    flash('Email verified! You can now take the test.', 'success')
    return redirect(url_for('test.index'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('test.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(request.args.get('next') or url_for('test.index'))
        flash('Invalid email or password.', 'error')
    return render_template('auth/login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@bp.route('/forgot', methods=['GET', 'POST'])
def forgot():
    form = ForgotForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user:
            try:
                send_verification_email(user)
            except Exception:
                pass
        # Always show same message to avoid email enumeration
        flash('If that email is registered, you\'ll receive a reset link shortly.', 'info')
        return redirect(url_for('auth.login'))
    return render_template('auth/forgot.html', form=form)


@bp.route('/results')
@login_required
def my_results():
    return render_template('auth/results.html', results=current_user.results)
