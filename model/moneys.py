from __init__ import db

class UserBalance(db.Model):
    __tablename__ = 'user_balance'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)

    def __init__(self, user_id, balance=0.0):
        self.user_id = user_id
        self.balance = balance

    def update_balance(self, amount):
        self.balance += amount
        db.session.commit()

    def get_balance(self):
        return self.balance

    @classmethod
    def get_or_create(cls, user_id):
        user_balance = cls.query.filter_by(user_id=user_id).first()
        if user_balance is None:
            user_balance = cls(user_id=user_id)
            db.session.add(user_balance)
            db.session.commit()
        return user_balance
