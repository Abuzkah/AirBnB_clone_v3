#!/usr/bin/python3
"""Defines the State class."""
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Get a list of City instances with
                state_id equals to the current State.id.

            This is a getter attribute for FileStorage
                relationship between State and City.
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

    def to_json(self):
        """Return a JSON-serializable representation of the object."""
        try:
            json_dict = {
                "__class__": "State",
                "id": self.id,
                "name": self.name,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
            }
        except AttributeError:
            json_dict = {
                "__class__": "State",
                "id": "N/A",
                "name": "N/A",
                "created_at": "N/A",
                "updated_at": "N/A",
            }
        return json_dict

    def bm_update(self, data):
        """Update the State object with the data provided in the dictionary."""
        for key, value in data.items():
            if key != 'id' and key != 'created_at' and key != 'updated_at':
                setattr(self, key, value)
        self.save()
