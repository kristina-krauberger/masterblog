from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-key")
    DATA_FILE = os.getenv("DATA_FILE", "data/data.json")