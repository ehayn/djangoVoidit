from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
	url(r'^newPost/', views.newPost, name='newPost'),
	url(r'^(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
	url(r'^(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),
	url(r'^(?P<pk>[0-9]+)/userPosts', views.userPosts, name='userPosts'),
]
