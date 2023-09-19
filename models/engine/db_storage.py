#!/usr/bin/python3
"""Database storage engine using SQLAlchemy ORM"""

from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

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

    def all(self, cls=None):
        """Query all objects of optional class"""
        classes = {
            "City": City,
            "State": State,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity,
        }
        result = {}
        query_rows = []
        
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query_rows = self.__session.query(cls)
            for obj in query_rows:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                result[key] = obj
            return result
        else:
            for name, value in classes.items():
                query_rows = self.__session.query(value)
                for obj in query_rows:
                    key = '{}.{}'.format(name, obj.id)
                    result[key] = obj
            return result

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
        self.__session.close()
