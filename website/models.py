from django.db import models
from persiantools.jdatetime import JalaliDate



class BlogPost(models.Model):
    """
    Represents a blog post with fields for title, content, author, and created date.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the post is created
    def persian_created_date(self):
        # Convert the datetime to Persian date and format it
         return JalaliDate(self.created_date).strftime('%Y/%m/%d')

    def __str__(self):
        return self.title
