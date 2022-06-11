from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    # ORDER BY DATE; MOST RECENT FIRST; LIMITED BY 5 ENTRIES
    blogs = Blog.objects.order_by('-date') [:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


