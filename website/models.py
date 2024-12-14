from django.db import models



class BlogPost(models.Model):
    """
    Represents a blog post with fields for title, content, author, and created date.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the post is created


    def __str__(self):
        return self.title
