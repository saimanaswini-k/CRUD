from database import Base,engine
from models import Dataset
import asyncio

print("Creating database ....")

Base.metadata.create_all(engine)
