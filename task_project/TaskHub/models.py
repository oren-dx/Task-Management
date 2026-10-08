from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    full_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.username}'


class TaskModel(models.Model):
    STATUS_TYPE =[
        ('not_started','not_started'),
        ('in_progress','in_progress'),
        ('completed','completed'),
    ]
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    status = models.CharField(choices=STATUS_TYPE,max_length=20,null=True)
    deadline = models.DateField(null=True)
    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        related_name='user_task'
    )

    def __str__(self):
        return f'{self.title}'
    
    