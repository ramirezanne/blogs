from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import blog
from django.urls import reverse_lazy
from .forms import BlogForm



# Create your views here.

def index(request):
    template = 'index.html'
    blogs = blog.objects.all()
    context = {
         'blogs': blogs,
    }
    return render(request, template, context)

def add_blog(request):
	template = "add_blog.html"

	if request.method == "POST":
		form = BlogForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
			'blog_form': BlogForm(),
		}
		return render(request, template, context)

def delete_blog(request, blog_id):
    blogs = blog.objects.get(id=int(blog_id))
    blogs.delete()
    return HttpResponseRedirect(reverse_lazy('blog:index'))

def update_blog(request, blog_id):
	template = "update_blog.html"
	blogs = blog.objects.get(id=int(blog_id))

	if request.method == "POST":
		form = BlogForm(request.POST, instance=blogs)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
			'blog_form':BlogForm(instance=blogs),
		}
		return render(request, template, context)

def view_blog(request,blog_id):
	template ="content.html"
	blogs = blog.objects.filter(id=blog_id)
	context = {
        'blogs':blogs,
    }
	return render(request,template,context)


