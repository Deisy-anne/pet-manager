from django.db import models
from uuid import uuid4

from apps.user.models import User

class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    breed = models.CharField(max_length=150, blank=True)
    weight = models.FloatField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'pet'
    
    def __str__(self):
        return f'{self.name}'   
 
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.breed = self.breed.capitalize()
        super(Pet,self).save(*args,**kwargs)