# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import CustomUser, CandidateProfile, RecruiterProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver that creates a Candidate or Recruiter profile
    automatically whenever a new CustomUser instance is saved.
    """
    if created:
        if instance.role == 'CANDIDATE':
            CandidateProfile.objects.create(user=instance)
        elif instance.role == 'RECRUITER':
            RecruiterProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver that saves the profile whenever the user is saved.
    """
    # We check role just in case, but profiles should exist due to create_user_profile
    if hasattr(instance, 'candidate_profile'):
        instance.candidate_profile.save()
    elif hasattr(instance, 'recruiter_profile'):
        instance.recruiter_profile.save()