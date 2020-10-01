from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger
from .models import Post

def post_list(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list,2)
    page_no = request.GET.get('page')
    try:
        posts=paginator.page(page_no)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'title':'All Posts',
        'page': page_no,
        'Posts':posts,
    }
    return render(request,'Blog/post/list.html',context)

def post_detail(request,year,month,day,post):
    post = get_object_or_404(
                    Post,
                slug=post,
                status='published',
                publish__year=year,
                publish__month=month,
                publish__day=day     )
    context={
        'title':post.title,
        'post':post,
    }
    return render(request,'Blog/post/details.html',context)