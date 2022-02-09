from django.urls import path
from post.views import *

app_name = 'post'

urlpatterns = [
    path('', posts_list, name='posts'),
    path('create/', post_create, name='create'),
    path('delete/<int:id>/', post_delete, name='post_delete'),
    path('detail/<int:id>/', post_detail, name='post_detail'),
    path('update/<int:id>/', post_update, name='post_update'),
]


