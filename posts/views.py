from django.shortcuts import render, render_to_response, get_object_or_404
from posts.models import BlogCategories, BlogPost, TypeOfEntry


# Create your views here.
def index(request):
	return render_to_response('index.html', {
		'categories': BlogCategories.objects.all(),
		'posts': BlogPost.objects.all(),
		'type': TypeOfEntry.objects.all()
		})

def view_post(request, slug):
	return render_to_response('view_post.html', {
		'post': get_object_or_404(Blog, slug=slug)
		})

def view_category(request, slug):
	category = get_object_or_404(BlogCategories, slug=slug)
	type_of = get_object_or_404(TypeOfEntry, slug=slug)
	return render_to_response('view_category.html', {
		'category': category,
		'post': BlogPost.objects.filter(category=category)[:5],
		'type': TypeOfEntry.objects.filter(type_of=type_of)[:5]
		})

def view_type(request, slug):
	category = get_object_or_404(BlogCategories, slug=slug)
	type_of = get_object_or_404(TypeOfEntry, slug=slug)
	return render_to_response('view_type.html', {
		'category': category,
		'post': BlogPost.objects.filter(category=category)[:5],
		'type': TypeOfEntry.objects.filter(type_of=type_of)[:5]
		})
