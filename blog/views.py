from django.shortcuts import render
from blog.models import Home, Blog

# Create your views here.
def index(request):

    page = Home.objects.all().order_by('-id').first()
    children = Blog.objects.live()

    print(children)

    context = {
        'page':page,
        'children':children
    }
    return render(request, 'blog/home.html', context=context)


def blog(request, slug):

    page = Blog.objects.filter(slug=slug).first()

    context = {
        'page':page,
        'single': True
    }

    return render(
        request, 'blog/blog.html', context=context
    )


def about(request):

    context = {
        'about':True
    }

    return render(
        request, 'blog/about.html', context=context
    )

