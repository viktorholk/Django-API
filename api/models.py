from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser )
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from datetime import datetime, timedelta
import pytz
# Create your models here.

# class UserManager(BaseUserManager):
#     def create_user(self, username, password=None):
#         if not username:
#             raise ValueError('Invalid User')
    
#         user = self.model(
#             username
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, username, password=None):
#         user = self.create_user(username)
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser):
#     username    = models.CharField(max_length=45, unique=True, null=False)
#     created_at  = models.DateTimeField(auto_now_add=True)

#     is_active   = models.BooleanField(default=True)
#     is_admin    = models.BooleanField(default=False)


#     objects = UserManager()

#     USERNAME_FIELD  = 'username'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.username

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin

class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key):
        except: self.model.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deleted')

        # time comparison
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        if token.created > utc_now - timedelta(hours=2):
            raise AuthenticationFailed('Token has expired')
    
        return token.user, token


