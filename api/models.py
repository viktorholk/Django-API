from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser )
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