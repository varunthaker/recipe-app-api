"""Data base Models"""

from django.db import models
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Email must be provided')
        user = self.model(email = self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):

    #abstract for authentication feat
    #Permissionmixing for permission feat

    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    #ref to use our own custome User manager from base user class
    objects = UserManager()

    USERNAME_FIELD = 'email'

class Recipe(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

class Youth(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now_add=True)
    from_city_germany = models.CharField(max_length=50)
    from_city_india = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    # followup_sevak = models.OneToOneField()
    sabha_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name
