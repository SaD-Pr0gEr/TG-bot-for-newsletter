from sqlalchemy.orm import sessionmaker
from database.models import engine, Subscribers


class DbManager:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_all_subscribers(self):
        get_users = self.session.query(Subscribers).filter(Subscribers.is_subscribed == True).all()
        return get_users

    def get_user_from_subs(self, user_id):
        get_user = self.session.query(Subscribers).filter(Subscribers.user_id == user_id).first()
        if not get_user:
            return False
        return get_user

    def set_status(self, user_id, status: bool):
        get_user = self.session.query(Subscribers).filter(Subscribers.user_id == user_id).first()
        get_user.is_subscribed = status
        self.session.commit()
        return get_user

    def add_user(self, user_id, status: bool):
        add = Subscribers(user_id=user_id, is_subscribed=status)
        self.session.add(add)
        self.session.commit()
        return add
