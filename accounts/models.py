from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(_('email address'),unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()
    ROLE_CHOICES=(
        ('CANDIDATE','Candidate'),
        ('RECRUITER','Recruiter'),
    )
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default='CANDIDATE')

    def __str__(self):
        return self.email

class CandidateProfile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='candidate_profile')
    bio=models.TextField(blank=True)
    location=models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return f"candidate profile of {self.user.email}"

class RecruiterProfile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="recruiter_profile")
    job_title=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return f"Recuritet profile for {self.user.email}"