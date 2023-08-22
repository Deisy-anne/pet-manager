from django.db import models
from uuid import uuid4

class User(models.Model):
   id = models.UUIDField(primary_key=True,default=uuid4, editable=False)
   first_name = models.CharField(max_length=150)
   last_name = models.CharField(max_length=150)
   birth_date = models.DateField()
   email = models.EmailField()
   password = models.CharField()
   
   class Meta:
       db_table = 'user'
   
   def save(self, *args, **kwargs):
       self.first_name = self.first_name.capitalize()
       self.last_name = self.last_name.capitalize()
       super(User, self).save(*args, **kwargs)
       
       
