from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.models import Home, Blog, Category
from blog.forms.login import LoginForm
from blog.forms.create_user import RegisterForm
from blog import groups
from utils.pagination import make_pagination
from utils.http_error import HttpPostError
from django.contrib import messages
from watson import search as watson_search
from typing import List

# Create your views here.
def index(request):

    page = Home.objects.all().order_by('-id').first()
    children = Blog.objects.order_by('-id').live()
    pagination = make_pagination(
        request=request,
        object_list=children,
        per_page=12
    )

    resultado = True if len(children) > 0 else False

    context = {
        'head_title':'Home',
        'page':page,
        'home':True,
        'resultado':resultado,
        'text_button':'Enviar',
        'pages':pagination['pagination_range'],
        'children':pagination['page_obj']
    }
    return render(request, 'blog/home.html', context=context)



def blog(request, slug):

    page = Blog.objects.filter(slug=slug).first()
    similar_posts = Blog.objects.filter(category=page.category)[:6]
    similar = True if len(similar_posts) > 1 else False
    
    context = {
        'head_title': f'Home - {page.title}',
        'page':page,
        'home':True,
        'single': True,
        'similar':similar,
        'similar_posts':similar_posts
    }

    return render(
        request, 'blog/blog.html', context=context
    )


def search(request):

    blogs: List[Blog] = []
    pesquisa = request.GET.get('q')

    if len(pesquisa.strip()) <= 0:
        blogs = Blog.objects.all()
    else:
        resultados = watson_search.search(pesquisa)
        for r in resultados:
            blogs.append(Blog.objects.filter(title=r.title).first())
    
    resultado = True if len(blogs) > 0 else False

    print(blogs)

    pagination = make_pagination(
        request=request,
        object_list=blogs,
        per_page=9
    )
    context = {
        'search':True,
        'pesquisa':pesquisa,
        'head_title':f"Resultados para - {pesquisa}",
        'home':True,
        'resultado':resultado,
        'pages':pagination['pagination_range'],
        'children':pagination['page_obj']
    }
    return render(request, "blog/home.html", context=context)


def search_category(request, category):
    blogs: List[Blog] = Blog.objects.filter(category=category)
    category = blogs[0].category.name
    resultado = True if len(blogs) > 0 else False
    pagination = make_pagination(
        request=request,
        object_list=blogs,
        per_page=9
    )
    context = {
        'search':True,
        'pesquisa':category,
        'head_title':f'Resultados para - {category}',
        'home':True,
        'resultado':resultado,
        'pages':pagination['pagination_range'],
        'children':pagination['page_obj']
    }
    return render(
        request, 'blog/home.html', context=context
    )


def search_user(request, user: User):
    blogs: List[Blog] = Blog.objects.filter(owner=user)
    user = f'{blogs[0].owner.first_name} {blogs[0].owner.last_name}'
    resultado = True if len(blogs) > 0 else False
    pagination = make_pagination(
        request=request,
        object_list=blogs,
        per_page=9
    )
    context = {
        'search':True,
        'pesquisa':user,
        'head_title':f'Resultados para - {user}',
        'home':True,
        'resultado':resultado,
        'pages':pagination['pagination_range'],
        'children':pagination['page_obj']
    }
    return render(
        request, 'blog/home.html', context=context
    )


def about(request):

    context = {
        'head_title':'About',
        'about':True
    }

    return render(
        request, 'blog/about.html', context=context
    )


def register_view(request):

    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    context = {
        'form':form,
        'text_button':'Criar conta',
        'head_title':'Criar conta',
        'form_action':reverse('register_create')
    }

    return render(request, 'blog/register.html', context=context)


def register_create(request):

    HttpPostError(request)

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        messages.success(request, 'login')
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', '')
        )
        login(request, authenticated_user)
        del(request.session['register_form_data'])
        groups.addEditorGroup(user)
        return redirect(reverse('home-index'))
    else:
        messages.error(request, 'Não foi possível criar a conta.')
        return redirect(reverse('register'))


def login_view(request):

    form = LoginForm()

    context = {
        'form':form,
        'text_button':'Entrar',
        'head_title':'Login',
        'form_action':reverse('login_create')
    }

    return render(
        request, 'blog/login.html', context=context
    )


def login_create(request):

    HttpPostError(request)

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', '')
        )

        if authenticated_user is not None:
            messages.success(request, 'Você está logado')
            login(request, authenticated_user)
            return redirect(reverse('home-index'))
        else:
            messages.error(request, 'Credenciais inválidas')
    else:
        messages.error(request, 'Username ou password inválidos')

    return redirect(reverse('login'))


@login_required(login_url='login', redirect_field_name='next')
def logout_view(request):

    if not request.POST:
        return redirect(reverse('login'))
    
    if request.POST.get('username') != request.user.username:
        return redirect(reverse('login'))
    
    logout(request)
    return redirect(reverse('home-index'))
