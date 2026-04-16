from models.base_item import BaseItem

class Item(BaseItem):
    def __init__(self, item_id, name, description, category, location, contact):
        super().__init__(item_id, name)

        self.description = description
        self.category = category
        self.location = location
        self.contact = contact
        self.status = "Lost"

    def to_dict(self):
        data = self.basic_info()
        data.update({
            "description": self.description,
            "category": self.category,
            "location": self.location,
            "contact": self.contact,
            "status": self.status
        })
        return data
