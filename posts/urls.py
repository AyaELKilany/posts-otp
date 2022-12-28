from django.urls import path
from .views import *

urlpatterns = [
    path('' , all_posts , name='posts'),
    path('published' , all_published_posts , name='published_posts'),
    path('unpublished' , all_unpublished_posts , name='unpublished_posts'),
    path('create' , create_post , name='create post'),
]