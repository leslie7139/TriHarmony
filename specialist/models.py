from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Specialist(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default=None, null=True)
    is_specialist = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Child(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=255)
    specialist = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True)
    is_child = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Parent(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default=None, null=True)
    is_parent = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Behavior(models.Model):
    behavior = models.CharField(max_length=255)
    behavior_details = models.CharField(max_length=1000, default='')
    notes = models.CharField(max_length=255, blank=True)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    def __str__(self):
        return self.behavior


class BehaviorCheckIn(models.Model):
    behavior = models.ForeignKey(Behavior, on_delete=models.CASCADE)
    behavior_intensity = models.IntegerField(null=True)
    behavior_frequency = models.IntegerField(null=True)
    note = models.TextField(max_length=3000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.behavior)


class Feeling(models.Model):
    FEELINGS_CHOICES = (
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('scared', 'Scared'),
        ('tired', 'Tired'),
        ('confused', 'Confused'),
        ('disappointed', 'Disappointed'),
        ('frustrated', 'Frustrated'),
        ('lonely', 'Lonely'),
        ('nervous', 'Nervous'),
        ('proud', 'Proud'),
        ('surprised', 'Surprised'),
        ('worried', 'Worried'),
        ('overwhelmed', 'Overwhelmed'),
    )
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    feeling = models.CharField(
        choices=FEELINGS_CHOICES, max_length=255, blank=False)
    recorded_at = models.DateTimeField(auto_now_add=True, null=True)
    note = models.TextField(max_length=3000, blank=True)

    def __str__(self):
        return self.feeling
