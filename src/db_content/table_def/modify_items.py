from sqlalchemy import Column, Integer, String

from ..table_def.base import Base


class ModifyItems(Base):
    __tablename__ = "ModifyItems"
    id = Column(Integer, autoincrement=True, primary_key=True)
    food_name = Column(String(200))
    food_price = Column(String(50))

    def __init__(self, records):
        self.food_name = records[0]
        self.food_price = records[1]

    @classmethod
    def read_data(cls, session, data):
        info = dict()
        info["food_names"] = []
        info["food_price"] = []
        if data == "read_modify_items":
            result = session.query(ModifyItems).all()
            for row in result:
                info["food_names"].append(row.food_name)
                info["food_price"].append(row.food_price)

        return info

    @classmethod
    def update_items(cls, session, data):
        food_name = data[0]
        food_price = data[1]
        print("food price db", food_name)
        session.query(ModifyItems).filter(ModifyItems.food_name == food_name)\
            .update({"food_price": food_price})
        session.commit()

    @classmethod
    def delete_items(cls, session, data):
        food_name = data[0]
        print("food name db del", food_name)
        session.query(ModifyItems).filter(ModifyItems.food_name == food_name).delete()
        session.commit()
