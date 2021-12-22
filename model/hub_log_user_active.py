from peewee import *
from .base import BaseModel


class HubLogUserActive(BaseModel):
  id    = AutoField(column_name='id')
  profile    = IntegerField(column_name='id_perfil')
  app  = IntegerField(column_name='id_aplicacao')
  autorized = BooleanField(column_name='authotized')
  datetime = DateTimeField(column_name='datetime_request')

  class Meta:
    table_name = 'hub_log_user_active'