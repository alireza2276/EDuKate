from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 3


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    blog.views += 1
    blog.save()
    return render(request, 'blog/blog_detail.html', context={'blog': blog})
