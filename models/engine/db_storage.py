#!/usr/bin/python3
"""Database storage engine using SQLAlchemy ORM"""

from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os


class DBStorage:
    """Handles database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Create engine and link to database"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = scoped_session(sessionmaker(expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None):
        """Query all objects of optional class"""
        if cls:
            objects = self.__session.query(cls).all()
        else:
            from models.base_model import BaseModel
            objects = self.__session.query(BaseModel).all()

        return {obj.id: obj for obj in objects}

    def new(self, obj):
        """Add object to current session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from current session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and session from engine"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    def close(self):
        """Call remove() on private session attribute"""
        self.__session.remove()
