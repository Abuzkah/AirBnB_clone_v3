#!/usr/bin/python3
"""Defines the User class."""

import hashlib
import os
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """Represents a user for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table users.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        email: (sqlalchemy String): The user's email address.
        password (sqlalchemy String): The user's password.
        first_name (sqlalchemy String): The user's first name.
        last_name (sqlalchemy String): The user's last name.
        places (sqlalchemy relationship): The User-Place relationship.
        reviews (sqlalchemy relationship): The User-Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")

    def __init__(self, *args, **kwargs):
        """
        Instantiates user object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.__set_password(kwargs['password'])

    def __set_password(self, password):
        """
        Sets the hashed password for the user.

        Args:
            password (str): The password to be hashed.
        """
        if isinstance(password, str):
            secure = hashlib.md5()
            secure.update(password.encode('utf-8'))
            self.password = secure.hexdigest()
        else:
            self.password = ''

    if STORAGE_TYPE != "db":
        def to_dict(self, save_fs=None):
            """
            Returns a dictionary representation of the User instance.

            Args:
                save_fs (FileStorage): The file storage instance.

            Returns:
                dict: A dictionary representation of the User instance.
            """
            user_dict = super().to_dict()
            if save_fs is None or save_fs == "db":
                user_dict.pop('password', None)
            return user_dict
