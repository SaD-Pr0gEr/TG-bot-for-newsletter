from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.db.models import Subscribers


class DbManager:

    def __init__(self, db_url):
        self.db_url = db_url

    def retrieve_user(self, user_id):
        Session = sessionmaker(bind=create_engine(self.db_url))
        session = Session()
        get = session.query(Subscribers).filter(user_id == user_id).first()
        return get

    def get_all_users(self):
        Session = sessionmaker(bind=create_engine(self.db_url))
        session = Session()
        get = session.query(Subscribers).all()
        return get

    def get_all_subscribers(self):
        Session = sessionmaker(bind=create_engine(self.db_url))
        session = Session()
        get = session.query(Subscribers).filter(Subscribers.is_subscribed == True).all()
        return get

    def get_user_from_subs(self, user_id: [str, int]):
        Session = sessionmaker(bind=create_engine(self.db_url))
        session = Session()
        get_user = session.query(Subscribers).filter(Subscribers.user_id == user_id).first()
        if not get_user:
            return False
        return get_user

    def set_status(self, user_id: [str, int], status: bool):
        Session = sessionmaker(bind=create_engine(self.db_url))
        session = Session()
        get_user = session.query(Subscribers).filter(Subscribers.user_id == user_id).first()
        get_user.is_subscribed = status
        session.commit()
        return get_user

    def add_user(self, user_id: [str, int], status: bool):
        Session = sessionmaker(bind=create_engine(self.db_url))
        session = Session()
        add = Subscribers(user_id=user_id, is_subscribed=status)
        session.add(add)
        session.commit()
        return add

    def reset_data(self):
        Session = sessionmaker(bind=create_engine(self.db_url))
        session = Session()
        session.query(Subscribers).delete()
        session.commit()
        return True
