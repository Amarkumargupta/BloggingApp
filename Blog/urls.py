from django.urls import path
from .views import post_detail,home, PostListView,post_share 
app_name = "Blog"
urlpatterns =[
path('',home,name='home'),
path('posts/',PostListView.as_view(),name='post_list'),
path('posts/<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_details'),
path('posts/<int:post_id>/share/',post_share,name='post_share')
]