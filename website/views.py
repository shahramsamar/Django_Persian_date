from django.shortcuts import render
from .models import BlogPost

from persiantools.jdatetime import JalaliDate
def index_views(request):
    blog_posts = BlogPost.objects.all()
    
    # Convert the created_date to Persian format (if you want to do it here)
    for post in blog_posts:
        post.persian_created_date = JalaliDate(post.created_date).strftime('%Y/%m/%d')



    blog_posts = BlogPost.objects.all()
    return render(request,'index.html',{'blog_posts': blog_posts})


def index_temp(request):
    blog_posts = BlogPost.objects.all()
    return render(request,'index_temp.html',{'blog_posts': blog_posts})

