import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .table_def.base import Base
from .table_def.modify_items import ModifyItems


class DatabaseHelper:

    def __init__(self):
        self._engine = create_engine('mysql+pymysql://root:root1234@127.0.0.1/Food_db')
        Base.metadata.create_all(bind=self._engine, checkfirst=True)
        self._Session = sessionmaker(bind=self._engine)
        self.new_session = self._Session()

    def add_items(self, table_name, data):
        table_object = table_name(data)
        self.new_session.add(table_object)
        self.new_session.commit()

    def read_items(self, table_name, data):
        data2 = table_name.read_data(self.new_session, data)
        self.new_session.commit()
        return data2

    def update_items(self, table_name, data):
        if table_name == ModifyItems:
            table_name.update_items(self.new_session, data)

    def delete_items(self, table_name, data):
        if table_name == ModifyItems:
            table_name.delete_items(self.new_session, data)
            pass


def main(table_name, action, data):
    data2 = None
    db_helper_obj = DatabaseHelper()
    if action == "add":
        if table_name == "ModifyItems":
            db_helper_obj.add_items(ModifyItems, data)

    if action == "read":
        if table_name == "ModifyItems":
            data2 = db_helper_obj.read_items(ModifyItems, data)

    if action == "update":
        if table_name == "ModifyItems":
            db_helper_obj.update_items(ModifyItems, data)

    if action == "delete":
        print("database helper data", data[0])
        if table_name == "ModifyItems":
            db_helper_obj.delete_items(ModifyItems, data)

    db_helper_obj.new_session.close()
    return data2

if __name__ == "__main__":
    obj = DatabaseHelper()
    data = "read_modify_items"
    data2 = main("ModifyItems", "read", data)
    print("data2", data2)
