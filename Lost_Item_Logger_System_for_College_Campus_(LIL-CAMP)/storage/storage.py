import pandas as pd
import os

FILE = "data/lilcamp_data.json"

class Storage:

    @staticmethod
    def load():
        if os.path.exists(FILE):
            df = pd.read_json(FILE)
            return df.to_dict(orient="index")
        return {}

    @staticmethod
    def save(data):
        df = pd.DataFrame.from_dict(data, orient="index")
        df.to_json(FILE, indent=4)