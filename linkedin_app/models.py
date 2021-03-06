from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


    
class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=150)
    image = models.ImageField(upload_to='static/uploads/', blank=True, null=True)
    following = models.ManyToManyField('self', blank=True, symmetrical=False)
    liked_posts = models.ManyToManyField('Post', blank=True, symmetrical=False)

    def check_messages(self):
        new_messages = ''
        messages = DirectMessage.objects.filter(target=self.id)
        for dm in messages:
            if not dm.message.seen:
                new_messages= 'You have unread messages!'
        return new_messages



class Post(models.Model):
    user_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_name")
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/uploads/', blank=True, null=True)
    body = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)


class Message(models.Model):
    text = models.CharField(max_length=140)
    time = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField(default=False)


class DirectMessage(models.Model):
    target= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message= models.ForeignKey(Message, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')