# Create your models here.
import uuid
from datetime import datetime, timedelta
import jwt
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from src import settings
from api.user_manager import UserManager

AUTH_PROVIDERS = {
    'email': 'email'
}
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email Address'), unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    staff = models.BooleanField(default=False)  ######3 For django staff user
    admin = models.BooleanField(default=False)  ##########3 For jango adminuser
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(max_length=255,
                                     null=False, default=AUTH_PROVIDERS.get('email'))
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def token(self):
        token = jwt.encode(
            {'email': self.email,
                'exp': datetime.utcnow() + timedelta(hours=24)},
            settings.SECRET_KEY, algorithm='HS256')

        return token


class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Customer(models.Model):
    user = models.OneToOneField(User, primary_key=True ,on_delete=models.CASCADE, related_name='customer')
    full_name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return str(self.full_name)


class Vendor(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='vendor')
    business_name = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return str(self.business_name)