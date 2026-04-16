from datetime import datetime

class BaseItem:
    def __init__(self, item_id, name):
        self.item_id = item_id
        self.name = name
        self.date = datetime.now().strftime("%d-%m-%Y")

    def basic_info(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "date": self.date
        }