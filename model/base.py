import os
from peewee import *

database = MySQLDatabase(
  os.environ['DATABASE_NAME'],
  user=os.environ['DATABASE_USER'],
  password=os.environ['DATABASE_PASS'],
  host=os.environ['DATABASE_HOST'],
  port=int(os.environ['DATABASE_PORT'])
)
class BaseModel(Model):
  """
  A base model
  """
  class Meta:
    database = database
