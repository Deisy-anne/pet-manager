from django.db import models
from uuid import uuid4


class Pet(models.Model):
    
    id_pet = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    breed = models.CharField(max_length=150, blank=True)
    weight = models.FloatField(null=True,blank=True)
    guardian_email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'   
    
 
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.breed = self.breed.capitalize()
        
        super(Pet,self).save(*args,**kwargs)