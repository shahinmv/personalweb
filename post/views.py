from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')

def post(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'portfolio/post.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'portfolio/post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']