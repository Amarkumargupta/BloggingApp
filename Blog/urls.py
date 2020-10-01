from django.urls import path
from .views import post_list ,post_detail
app_name = "Blog"
urlpatterns =[
path('',post_list,name='post_list'),
path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_details')
]