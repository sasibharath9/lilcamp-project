from models.item import Item
from storage.storage import Storage
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class LILCAMP:

    def add_item(self):
        data = Storage.load()

        item_id = input("Enter ID: ")
        if item_id in data:
            print("ID exists!")
            return

        name = input("Lost Item Name: ")
        desc = input("Description: ")
        cat = input("Category: ").lower()
        loc = input("Location: ").lower()
        contact = input("Contact: ")

        item = Item(item_id, name, desc, cat, loc, contact)
        data[item_id] = item.to_dict()

        Storage.save(data)
        print("Item Added!")

    def view_items(self):
        data = Storage.load()
        if not data:
            print("No data")
            return

        df = pd.DataFrame.from_dict(data, orient="index")
        print(df)

    def search(self):
        data = Storage.load()
        df = pd.DataFrame.from_dict(data, orient="index")

        key = input("Search: ").lower()

        result = df[df.apply(lambda r:
                             key in str(r["name"]).lower() or
                             key in str(r["category"]).lower(), axis=1)]

        print(result if not result.empty else "No match")

    def report(self):
        data = Storage.load()
        if not data:
            print("No data")
            return

        df = pd.DataFrame.from_dict(data, orient="index")


        arr = np.array(df["status"])
        lost = np.sum(arr == "Lost")
        found = np.sum(arr == "Found")

        print("\n--- REPORT ---")
        print("Lost:", lost)
        print("Found:", found)


        labels = ["Lost", "Found"]
        values = [lost, found]

        plt.figure()
        plt.bar(labels, values)
        plt.title("Lost vs Found Items")
        plt.xlabel("Status")
        plt.ylabel("Count")
        plt.show()


        category_counts = df["category"].value_counts()

        plt.figure()
        category_counts.plot(kind="bar")
        plt.title("Category Distribution")
        plt.xlabel("Category")
        plt.ylabel("Count")
        plt.show()


        location_counts = df["location"].value_counts()

        plt.figure()
        location_counts.plot(kind="bar")
        plt.title("Location Distribution")
        plt.xlabel("Location")
        plt.ylabel("Count")
        plt.show()