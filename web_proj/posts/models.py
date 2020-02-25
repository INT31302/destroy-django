from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        get_user_model(), related_name="post", on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)
    like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="like_user_set", through="Like")
    unlike_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="unlike_user_set", through="Unlike")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def like_count(self):
        return self.like_user_set.count()

    @property
    def unlike_count(self):
        return self.unlike_user_set.count()


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)


class Unlike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
