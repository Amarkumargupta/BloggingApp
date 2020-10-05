from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger
from django.core.mail import send_mail 
from django.views.generic import ListView
from .models import Post,Comment
from .forms import EmailPostForm, CommentForm
def home(request):
    return render(request,'Blog/home.html')
class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'Posts'
    paginate_by     = 3
    template_name = 'Blog/post/list.html'
    
    
 
 
 
 
 
# def post_list(request):
#     posts_list = Post.objects.all()
#     paginator = Paginator(posts_list,2)
#     page_no = request.GET.get('page')
#     try:
#         posts=paginator.page(page_no)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     context = {
#         'title':'All Posts',
#         'page': page_no,
#         'Posts':posts,
#     }
#     return render(request,'Blog/post/list.html',context)

def post_detail(request,year,month,day,post):
    post = get_object_or_404(
                    Post,
                slug=post,
                status='published',
                publish__year=year,
                publish__month=month,
                publish__day=day     )
    if request.method == "POST":
        C_Form = CommentForm(request.POST)
        if C_Form.is_valid:
            form_ins=C_Form.save(commit=False)
            form_ins.post=post
            form_ins.save()
    
    commForm = CommentForm()
    comments = Comment.objects.filter(post=post,active=True)
    print(comments)
    context={
        'title':post.title,
        'post':post,
        'commentForm':commForm,
        'comments':comments,
    }
    return render(request,'Blog/post/details.html',context)


def post_share(request,post_id):
    post = get_object_or_404(Post,id=post_id,status='published')
    send = False
    if request.method =="POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recomand you reading "{}" '.format(cd['name'],cd['email'],post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments {}'.format(post.title,post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'ndtheboy04@gmail.com',[cd['to']])
            send = True 
    else :
        form = EmailPostForm()
    return render(request,'Blog/post/share.html',{'post':post,'Form':form})
