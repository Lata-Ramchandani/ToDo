from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):
    status_choice=[
        ('c','Completed'),
        ('p','Pending')
    ]   
    task=models.CharField(max_length=50)
    details=models.TextField(max_length=100)
    date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=1,choices=status_choice,default='p')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.task
