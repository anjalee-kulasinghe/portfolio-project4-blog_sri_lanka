from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    travel_interests = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users_userprofile"

    def __str__(self):
        return self.user.username