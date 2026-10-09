from django.db import models
from django.conf import settings #for USer model
# Create your models here.

class Company(models.Model):
    owner=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='companies'
    )
    name= models.CharField(max_length=255,unique=True)
    description=models.TextField(blank=True,null=True)
    location=models.CharField(max_length=255,blank=True)
    website=models.URLField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural="companies"
    def __str__(self):
        return self.name