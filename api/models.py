from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser )
# Create your models here.


class NodeManager(BaseUserManager):
    def create_user(self, node, password=None):
        if not node:
                raise ValueError('Users must have an node name')
        
        user = self.model(
            node=node
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, node, password=None):
        user = self.create_user(
            node
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Node(AbstractBaseUser):
    node = models.CharField(max_length=45, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = NodeManager()

    USERNAME_FIELD  = 'node'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.node

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin