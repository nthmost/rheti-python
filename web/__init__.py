import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
csrf = CSRFProtect()


def create_app(config=None):
    app = Flask(__name__, template_folder='templates', static_folder='static')

    # Defaults
    app.config.update(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev-change-me-in-production'),
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            'DATABASE_URL',
            f'sqlite:///{os.path.join(os.path.dirname(__file__), "rheti.db")}'
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        MAIL_SERVER=os.environ.get('MAIL_SERVER', 'localhost'),
        MAIL_PORT=int(os.environ.get('MAIL_PORT', 587)),
        MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS', 'true').lower() == 'true',
        MAIL_USERNAME=os.environ.get('MAIL_USERNAME'),
        MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD'),
        MAIL_DEFAULT_SENDER=os.environ.get('MAIL_DEFAULT_SENDER', 'rheti@nthmost.com'),
        WTF_CSRF_ENABLED=True,
    )

    if config:
        app.config.update(config)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to take the test.'

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    from .auth import bp as auth_bp
    from .test import bp as test_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(test_bp)

    with app.app_context():
        db.create_all()

    return app
