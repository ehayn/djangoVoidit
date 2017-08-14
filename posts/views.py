from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User
from django.utils.timesince import timesince
from django import template

register = template.Library()

@register.filter(name='timesincemin')
def timesincemin(value):
    now = datetime.now()
    try:
        difference = now - value
    except:
        return value

    if difference <= timedelta(minutes=1):
        return 'just now'
    return '%(time)s ago' % {'time': timesince(value).split(', ')[0]}

@login_required
def newPost(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['url']:
			post = Post()
			post.title = request.POST['title']
			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
				post.url = request.POST['url']
			else:
				post.url = 'http://' + request.POST['url']
			post.pub_date = timezone.datetime.now()
			post.author = request.user
			post.save()
			return redirect('home')
		else:
			return render(request, 'posts/newPost.html', {'error':'Please enter a title and url'})
	else:
		return render(request, 'posts/newPost.html')

	
def home(request):
	posts = Post.objects.order_by('-votes_total')
	return render(request, 'posts/home.html', {'posts':posts})
	
def userPosts(request, pk):
	user = User.objects.get(pk=pk)
	posts = Post.objects.filter(author=user)
	posts = posts.order_by('-pub_date')
	return render(request, 'posts/userPosts.html', {'posts':posts, 'user':user})
	
def upvote(request, pk):
	if request.method == 'POST':
		post = Post.objects.get(pk=pk)
		post.votes_total += 1
		post.save()
		return redirect('home')
	
def downvote(request, pk):
	if request.method == 'POST':
		post = Post.objects.get(pk=pk)
		post.votes_total -= 1
		post.save()
		return redirect('home')