from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

users_collection = db["users"]
projects_collection = db["projects"]
content_calendars_collection = db["content_calendars"]
captions_collection = db["captions"]
brands_collection = db["brands"]
campaigns_collection = db["campaigns"]
seo_reports_collection = db["seo_reports"]
trend_reports_collection = db["trend_reports"]
ads_collection = db["ads"]
mockups_collection = db["mockups"]


def connect_db():
    try:
        client.admin.command("ping")
        print("✅ MongoDB Connected Successfully")
    except Exception as e:
        print("❌ MongoDB Connection Failed")
        print(e)
