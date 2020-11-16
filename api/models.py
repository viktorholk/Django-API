from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser )
# Create your models here.


    
class NodeManager(BaseUserManager):
    def create_node(self, title, password=None):
        if not title:
            raise ValueError("Nodes must have a title")
    
        node = self.model(
            title=title
        )
        node.set_password(password)
        node.save(using=self._db)
        return node


class Node(AbstractBaseUser):
    title       = models.CharField(max_length=45, unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD  = 'title'
    REQUIRED_FIELDS = []

    objects = NodeManager()

    def __str__(self):
        return self.title