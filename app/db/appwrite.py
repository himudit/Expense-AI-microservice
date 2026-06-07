from appwrite.client import Client
from appwrite.services.databases import Databases

from app.config import settings

client = Client()

client.set_endpoint(settings.APPWRITE_ENDPOINT)
client.set_project(settings.APPWRITE_PROJECT_ID)
client.set_key(settings.APPWRITE_API_KEY)

databases = Databases(client)