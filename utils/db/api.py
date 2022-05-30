from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.db.models import Subscribers


class DbManager:

    def __init__(self, db_url) -> None:
        self.db_url = db_url
        self.session = sessionmaker(bind=create_engine(self.db_url))

    def retrieve_user(self, user_id):
        return self.session().query(Subscribers).filter(user_id == user_id).first()

    def get_all_users(self):
        return self.session().query(Subscribers).all()

    def get_all_subscribers(self):
        return self.session().query(Subscribers).filter(Subscribers.is_subscribed.is_(True)).all()

    def get_user_from_subs(self, user_id: [str, int]):
        return self.session().query(Subscribers).filter(Subscribers.user_id == user_id).first() or None

    def set_status(self, user_id: [str, int], status: bool):
        session = self.session()
        get_user = session.query(Subscribers).filter(Subscribers.user_id == user_id).first()
        get_user.is_subscribed = status
        session.commit()
        return get_user

    def add_user(self, user_id: [str, int], status: bool):
        session = self.session()
        add = Subscribers(user_id=user_id, is_subscribed=status)
        session.add(add)
        session.commit()
        return add

    def reset_data(self):
        session = self.session()
        session.query(Subscribers).delete()
        session.commit()
        return True
