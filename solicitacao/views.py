from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from blog.groups import addGroup
from solicitacao.forms.create_solicitacao import SolicitacaoCreateForm
from solicitacao.forms.update_solicitacao import SolicitacaoUpdateForm
from solicitacao.models import Solicitacao, StatusSolicitacao
from utils.http_error import HttpPostError


def index(request):
    s = Solicitacao.objects.all().order_by('-id')
    context = {
        's':s
    }
    return render(
        request, 'solicitacao/index.html', context=context
    )


def acesso_view(request):
    auth = False
    if request.user.is_authenticated:
        auth = True
        solicitacao_form_data = request.session.get('solicitacao_create_form_data', None)
        form = SolicitacaoCreateForm(
            solicitacao_form_data,
            initial={
                'user':request.user,
                'status':StatusSolicitacao.objects.filter(status='Pendente').first()
            }
        )
        context = {
            'auth':auth,
            'form':form,
            'head_title':'Solicitação de nível de acesso',
            'text_button':'Enviar',
            'form_action':reverse('solicitacao_create')
        }
        return render(
            request, 'solicitacao/acesso.html', context=context
        )
    context = {
        'auth':auth,
        'head_title':'Solicitação de nível de acesso'
    }
    return render(
        request, 'solicitacao/acesso.html', context=context
    )


def acesso_solicitacao(request):
    HttpPostError(request)
    POST = request.POST
    request.session['solicitacao_create_form_data'] = POST
    form = SolicitacaoCreateForm(POST)
    if form.is_valid():
        messages.success(request, 'Solicitação enviada')
        form.save()
        del(request.session['solicitacao_create_form_data'])
    return redirect('solicitacao')


def solicitacao_page(request, id):
    s = Solicitacao.objects.filter(id=id).first()
    user = User.objects.filter(id=s.user.id).first()
    form = SolicitacaoUpdateForm(instance=s)
    context = {
        's':s,
        'user':user,
        'form':form,
        'form_action':reverse('solicitacao_update', args=(id,))
    }
    return render(
        request, 'solicitacao/solicitacao_page.html', context=context
    )

def solicitacao_status_update(request, id):
    HttpPostError(request)
    POST = request.POST
    request.session['solicitacao_update_form_data'] = POST
    form = SolicitacaoUpdateForm(data=request.POST or None, instance=Solicitacao.objects.filter(id=id).first())
    if form.is_valid():
        data = form.save(commit=False)
        status = str(data.status)
        if status == 'Aprovado':
            data.user.groups.clear()
            addGroup(data.user, data.group)
            messages.success(request, 'Nível de acesso de usuário aprovado com sucesso.')
        elif status == 'Rejeitado':
            messages.success(request, 'Nível de acesso rejeitado')
        data.save()
    return redirect('solicitacao_page', id)


