from pymongo import MongoClient
from passlib.context import CryptContext

# MongoDB connection
client = MongoClient("mongodb+srv://inzhamed:Ci1J6mwUivURVrxZ@railwaydefectsapp.npfehik.mongodb.net/")
db = client["railwaydefectsapp"]

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
hashed_password = pwd_context.hash("password123")  # Replace with your desired password

# User document
user = {
    "username": "testuser",
    "email": "testuser@example.com",
    "password_hash": hashed_password,
    "role": "operator",
    "language": "en",
    "notifications": {
        "email": True,
        "push": True
    }
}

# Insert user into the database
db.users.insert_one(user)
print("User added successfully!")