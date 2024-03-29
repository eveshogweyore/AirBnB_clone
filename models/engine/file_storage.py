#!/usr/bin/python3
"""FileStorage module for serialization & deserialization."""

import json


class FileStorage:
    """Serializes instance to JSON & deserializes"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary `__objects`."""
        return self.__objects

    def new(self, obj):
        """sets obj in __objects with key `<obj class name>.id`."""
        objkey = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[objkey] = obj

    def save(self):
        """serializes __objects to JSON & save to __file_path."""
        mobj = {}

        for k, v in self.__objects.items():
            mobj[k] = v.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(mobj, f)

    def reload(self):
        """deserializes json file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                des_dict = json.load(f)

                for k, v in des_dict.items():
                    from models.base_model import BaseModel
                    from models.state import State
                    from models.user import User
                    from models.city import City
                    from models.amenity import Amenity
                    from models.place import Place
                    from models.review import Review
                    model_dict = {"BaseModel": BaseModel, "State": State,
                                  "User": User, "City": City,
                                  "Amenity": Amenity,
                                  "Place": Place, "Review": Review}
                    obj_inst = model_dict[v['__class__']](**v)
                    self.__objects[k] = obj_inst
        except FileNotFoundError:
            pass
