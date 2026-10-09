from django.db import models
from django.conf import settings
from companies.models import Company
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(unique=True,help_text="URl-freindly name")

    class Meta:
        verbose_name_plural="Categggories"

    def __str__(self):
        return self.name

class Job(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('FULL_TIME', 'Full-Time'),
        ('PART_TIME', 'Part-Time'),
        ('CONTRACT', 'Contract'),
        ('INTERNSHIP', 'Internship'),
    ]
    EXPERIENCE_LEVEL_CHOICES = [
        ('ENTRY', 'Entry Level'),
        ('MID', 'Mid Level'),
        ('SENIOR', 'Senior Level'),
        ('LEAD', 'Lead / Manager'),
    ]
    company= models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name="jobs")
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)

    # Salary is optional, so null=True/blank=True
    salary_min = models.PositiveIntegerField(null=True, blank=True, help_text="Annual minimum salary")
    salary_max = models.PositiveIntegerField(null=True, blank=True, help_text="Annual maximum salary")

    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPE_CHOICES,
        default='FULL_TIME'
    )
    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_LEVEL_CHOICES,
        default='MID'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} at {self.company.name}"