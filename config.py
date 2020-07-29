import json
import os

LOCAL_FILE = "local.json"
CONFIG_FILE = "config.json"

class Config:
    def __init__(self):
        if os.path.isfile(LOCAL_FILE):
            with open(LOCAL_FILE, "r") as read_file:
                self.data = json.load(read_file)
        else:
            with open(CONFIG_FILE, "r") as read_file:
                self.data = json.load(read_file)
            with open(LOCAL_FILE, "w+") as write_file:
                json.dump(self.data, write_file)

    def save_config(self):
        with open(LOCAL_FILE, "w+") as write_file:
            json.dump(self.data, write_file)

cfg = Config()