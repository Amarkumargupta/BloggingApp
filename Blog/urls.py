from django.urls import path
from .views import post_detail, PostListView,post_share 
app_name = "Blog"
urlpatterns =[
path('',PostListView.as_view(),name='post_list'),
path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_details'),
path('<int:post_id>/share/',post_share,name='post_share')
]