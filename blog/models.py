from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Define a model for articles
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    banner = CloudinaryField('image', default='placeholder')

    def get_absolute_url(self):
        return reverse('detail_article', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

# Define a model for comments
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # Article to which the comment belongs
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)  # User who made the comment
    text = models.TextField()  # Text content of the comment
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time when the comment was created

    # Define a string representation for the Comment model
    def __str__(self):
        return f'Comment by {self.commenter.username} on {self.article.title}'