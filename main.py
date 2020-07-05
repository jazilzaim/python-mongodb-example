from mongoengine import *

from datetime import datetime
import os
import json

# Also install dnspython

# Import the MongoDB Atlas URI
DB_URI = "<DB_NAME>"

# Connected to our MongoDB database
connect(host=DB_URI)

# This is like our schema
# Defining documents
class User(Document):
    username = StringField(unique=True, required=True)
    email = EmailField(unique=True)
    password = BinaryField(required=True)
    age = IntField()
    bio = StringField(max_length=100)
    categories = ListField()
    admin = BooleanField(default=False)
    registered = BooleanField(default=False)
    date_created = DateTimeField(default=datetime.utcnow)

    def json(self):
        user_dict = {
            "username": self.username,
            "email": self.email,
            "age": self.age,
            "bio": self.bio,
            "categories": self.categories,
            "admin": self.admin,
            "registered": self.registered
        }
        return json.dumps(user_dict)

    meta = {
        "indexes": ["username", "email"],
        "ordering": ["-date_created"]
    }

# Dynamic Documents
class BlogPost(DynamicDocument):
    title = StringField()
    content = StringField()
    author = ReferenceField(User)
    date_created = DateTimeField(default=datetime.utcnow)

    meta = {
        "indexes": ["title"],
        "ordering": ["-date_created"]
    }

# Save a document to the database
# user = User(
#         username="jazil",
#         email="bill@example.com",
#         password=os.urandom(16),
#         age=22,
#         bio="Hello There!",
#         admin=True
# ).save()
#
# BlogPost(
#     title="My first blog post",
#     content="MongoDB and Python are awesome!",
#     author=user,
#     tags=["Python", "MongoDB", "MongoEngine"],
#     category="MongoDB"
# ).save()

# A different way to save a document in MongoDB
user = User(
        username="zaim",
        email="jack@example.com",
        password=os.urandom(16),
        age=22,
        bio="I love MongoDB!",
)

user.admin = True
user.registered = True

# This saves to the database
#     try:
#         user.save()
#     except NotUniqueError:
#         print('Username or email is not unique')

# Querying the database
# users = User.objects()

# print(users)

# for user in users:
#     print(user.username, user.email, user.bio)

# Filtering the database
# admin_users = User.objects(admin=True, registered=True)
#
# for a in admin_users:
#     print(a.username)

# Looking up an individual user in the database
# try:
#     jazza = User.objects(username="zaim").get()
# except DoesNotExist:
#     print('User not found')
#
# print(jazza.username, jazza.email)

# jaz_zaim = User.objects(username="zaim").get()
#
# posts = BlogPost.objects(author=jaz_zaim)
#
# for post in posts:
#     print(post.author.username)




print('Done')













