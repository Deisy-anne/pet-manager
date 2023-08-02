from django.contrib import admin
from pet import models

@admin.register(models.Pet)
class PetAdmin(admin.ModelAdmin):
  list_display = ('id_pet','name', 'age', 'created_at',)
  ordering = ('-id_pet',)
  list_filter = ('created_at', 'guardian_email')
  search_fields = ('id_pet', 'name')
  list_per_page = 10
  list_display_links = ('id_pet',)

