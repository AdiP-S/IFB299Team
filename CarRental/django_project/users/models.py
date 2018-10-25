from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django import forms
# Create your models here.

#The storage place to store the created users
class UserProfile(models.Model):
    user_choices = (('Customer', 'Customer'),
                    ('Employee', 'Employee'),
                    ('Employee', 'Manager'),
                    )
    state_choices = (('New South Wales', 'New South Wales'),
                    ('Queensland', 'Queensland'),
                    ('South Australia', 'South Australia'),
                    ('Victoria', 'Victoria'),
                    ('Tasmania', 'Tasmania'),
                    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length = 50,
                                 choices = user_choices,
                                 blank = False)
    user_state = models.CharField(max_length = 50,
                                 choices = state_choices,
                                 blank = False)
    employee_id = models.IntegerField(blank = True, null = True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender = User)
def create_user_profile( sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)
    instance.userprofile.save()
