from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profile."""

    def create_user(self, email, name, password = None):
        """"Create a new user profile"""
        if not email :
            raise ValueError ('User must have email address')
        email = self.normalize_email(email)
        user = self.model(email = email, name=name)
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser():
        """Create and save a super user"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin ):
    """Database Model for Users in the system"""
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField (default = True)
    is_staff = models.BooleanField( default = False )

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name():
        """"retrieve full name of user"""
        return self.name

    def get_short_name():
        """"retrieve full name of user"""
        return self.name

    def __str__(self):
        """"return string representation of our user"""
        return self.email


# Create your models here.
