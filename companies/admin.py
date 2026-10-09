from django.contrib import admin
from .models import Company
# Register your models here.
admin.site.register(Company)
#@admin.register(Company)
#class CompanyAdmin(admin.ModelAdmin):
 #   list_display=("id","name","owner")
  #  search_fields=("name",)