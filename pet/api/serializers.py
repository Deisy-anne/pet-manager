from rest_framework import serializers

from pet import models

class PetSerializer(serializers.ModelSerializer):
    class Meta:
      model = models.Pet
      fields = '__all__'