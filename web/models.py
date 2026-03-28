from datetime import datetime, timezone
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class User(UserMixin, db.Model):
    id               = db.Column(db.Integer, primary_key=True)
    email            = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash    = db.Column(db.String(255), nullable=False)
    display_name     = db.Column(db.String(100))
    email_verified   = db.Column(db.Boolean, default=False, nullable=False)
    verify_token     = db.Column(db.String(100), unique=True)
    created_at       = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    results          = db.relationship('Result', backref='user', lazy=True,
                                       order_by='Result.completed_at.desc()')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'


class TestProgress(db.Model):
    """Persists in-progress test answers so the user can resume after a session loss."""
    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    q_index     = db.Column(db.Integer, nullable=False, default=0)
    answers     = db.Column(db.JSON, nullable=False, default=list)
    updated_at  = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc),
                            onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<TestProgress user={self.user_id} q={self.q_index}>'


class Result(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    user_id      = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    completed_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    top_type     = db.Column(db.Integer, nullable=False)
    scores       = db.Column(db.JSON, nullable=False)   # {type_num: count, ...}
    answers      = db.Column(db.JSON, nullable=False)   # [{"q": "q1", "choice": "a", "value": "E"}, ...]
    n_questions  = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Result user={self.user_id} type={self.top_type}>'
