from django.shortcuts import render,get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status='published')
    context = {
        'title':'All Posts',
        'Posts':posts,
    }
    return render(request,'Blog/post/list.html',context)

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    context={
        'title':post.title,
        'post':post,
    }
    return render(request,'Blog/post/details.html',context)