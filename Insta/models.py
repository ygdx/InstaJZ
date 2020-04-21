from django.db import models
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/image/posts',
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])


class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality': 100},
        null=True,
        blank=True,
        )

    def get_connections(self):
        connections = UserConnection.objects.filter(creator=self)
        return connections

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self)
        return followers

    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(following=self)
        return followers.filter(creator=user).exists()

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def __str__(self):
        return self.username
