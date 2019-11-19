from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser 

# User 는 Custom User 를 사용 (default user를 사용하더라도 django 에서는 *강력히* Custom User 를 사용하라고 권장)

class User(AbstractUser):
    pass


class Todo(models.Model):
    # user.todo_set.all() 을 related_name 으로 고쳐줄 수 있음 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
