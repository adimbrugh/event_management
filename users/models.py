from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Email is required")
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user



class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=10)
    username = models.CharField(unique=False, max_length=10)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()



