from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    role = models.CharField(max_length = 100)

    def get_username(self):
        return self.email
    class Meta:
        swappable = 'AUTH_USER_MODEL'

CustomUser._meta.get_field_by_name('email')[0]._unique=True
CustomUser._meta.get_field('username')._unique = False


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField(null=True, blank=True)
    week_id = models.PositiveIntegerField(null=True, blank=True)
    timeout = models.IntegerField(null=True, blank=True)
class Choices(models.Model):
    question_id = models.ForeignKey('Questions')
    choice_1 = models.TextField()
    choice_2 = models.TextField()
    choice_3 = models.TextField(null = True)
    choice_4 = models.TextField(null = True)
    answer = models.CharField(max_length=255)
class QuizHistory(models.Model):
    """
    Contains the last attended quiz id.
    """
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    week_id = models.PositiveIntegerField()
    
class LeaderBoard(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    week_id = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now = True)    

class UserAnswers(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    week_id = models.PositiveIntegerField()
    question = models.TextField()
    user_answer = models.CharField(max_length=255)
    is_correct = models.NullBooleanField(null=True, blank=True)

class Badges(models.Model):
    id = models.AutoField(primary_key=True)
    badge_id = models.PositiveIntegerField()
    badge_name = models.CharField(max_length=255)
    badge_description = models.CharField(max_length=800)

class UserBadges(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    badge_id = models.ForeignKey(Badges)
    is_new = models.NullBooleanField(null=True, blank=True)
class GCMRegistrations(models.Model):
    id = models.AutoField(primary_key=True)
    registration_id = models.TextField()    
    timestamp = models.DateTimeField(auto_now_add=True)
