from django.urls import path
from .views import home_page,single_blog

urlpatterns = [
    path('',home_page, name='home'),
    path('post/<int:blog_id>/', single_blog, name="post")
]