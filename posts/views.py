from django.shortcuts import render, render_to_response, get_object_or_404
from django.shortcuts import render_to_response, get_object_or_404
from posts.models import BlogCategories, BlogPost, TypeOfEntry, BlogAuthor
from locations.models import BjjLocation, BjjInstructor


# Create your views here.
def index(request):
	return render_to_response('index.html', {
		'categories': BlogCategories.objects.all(),
		'posts': BlogPost.objects.all(),
		'author': BlogAuthor.objects.all(),
		'locations': BjjLocation.objects.all()
		})

# Blog posts views ===========================
def blog_posts(request):
	return render_to_response('blogs.html', {
		'posts': BlogPost.objects.all(),
		'category': BlogCategories.objects.all(),
		'author': BlogAuthor.objects.all()
		})

def view_post(request, slug):
	return render_to_response('view_post.html', {
		'post': get_object_or_404(BlogPost, slug=slug),
		'category': BlogCategories.objects.all(),
		'author': BlogAuthor.objects.all()
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

def view_author(request, slug):
	author = get_object_or_404(BlogAuthor, slug=slug)
	return render_to_response('author.html', {
		'category': BlogCategories.objects.all(),
		'post': BlogPost.objects.all()
		})

# Locations ==============================
def locations(request):
	return render_to_response('location.html', {
		'locations': BjjLocation.objects.all(),
		'post': BlogPost.objects.all(),
		'category': BlogCategories.objects.all(),
		'type': TypeOfEntry.objects.all()
		})

def location_spec(request, slug):
	locations = get_object_or_404(BjjLocation, slug=slug)
	return render_to_response('locations.html', {
		'locations': BjjLocation.objects.all(),
		'post': BlogPost.objects.all(),
		'category': BlogCategories.objects.all()
		})

# Instructors ===============================
def instructors(request):
	return render_to_response('instructors.html', {
		'instructor': BjjInstructor.objects.all(),
		'locations': BjjLocation.objects.all(),
		'post': BlogPost.objects.all(),
		'category': BlogCategories.objects.all(),
		'type': TypeOfEntry.objects.all()
		})
