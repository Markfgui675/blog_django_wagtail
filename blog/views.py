from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import Home, Blog
from blog.forms.login import LoginForm
from blog.forms.email import EmailForm
from blog.forms.create_user import RegisterForm
from blog import groups
from utils.pagination import make_pagination
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def index(request):

    page = Home.objects.all().order_by('-id').first()
    children = Blog.objects.order_by('-id').live()
    pagination = make_pagination(
        request=request,
        object_list=children,
        per_page=12
    )
    form = EmailForm()

    context = {
        'page':page,
        'form':form,
        'form_action':reverse('email-send'),
        'pages':pagination['pagination_range'],
        'children':pagination['page_obj']
    }
    return render(request, 'blog/home.html', context=context)


def email_send(request):

    if not request.POST:
        raise Http404()
    
    form = EmailForm(request.POST)

    if form.is_valid():
        form.save()
        send_mail('Assunto', 'Esse é o email que estou te enviando', 'caio@pythonando.com.br', ['caio.h.sampaio@outlook.com'])
        messages.success(request, 'E-mail enviado com sucesso!')
    else:
        messages.error(request, 'Não foi possível enviar o e-mail')
    
    return redirect(reverse('home-index'))

def blog(request, slug):

    page = Blog.objects.filter(slug=slug).first()
    similar_posts = Blog.objects.filter(category=page.category)[:6]
    similar = True if len(similar_posts) > 1 else False

    context = {
        'head_title': f'- {page.title}',
        'page':page,
        'single': True,
        'similar':similar,
        'similar_posts':similar_posts
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


def register_view(request):

    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    context = {
        'form':form,
        'form_action':reverse('register_create')
    }

    return render(request, 'blog/register.html', context=context)


def register_create(request):

    if not request.POST:
        raise Http404()

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
