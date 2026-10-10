from django.contrib import admin
from django.apps import apps
app_models=apps.get_app_config('accounts').get_models()
# Register your models here.
for model in app_models:
    admin.site.register(model)