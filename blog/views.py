from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from blog.models import Home, Blog
from blog.forms.login import LoginForm
from django.contrib import messages

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


def login_view(request):

    form = LoginForm()

    context = {
        'form':form,
        'form_action':reverse('login_create')
    }

    return render(
        request, 'blog/login.html', context=context
    )


def login_create(request):

    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', '')
        )

        if authenticated_user is not None:
            messages.success(request, 'Você está logado')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Credenciais inválidas')
    else:
        messages.error(request, 'Username ou password inválidos')

    return redirect(reverse('home-index'))

