from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from blog.models import Blog
from feedback.models import Feedback
from django.contrib import messages
from feedback.models import StatusFeedback
from feedback.forms.feedback_create import FeedbackcreateForm
from feedback.forms.feedback_update import FeedbackUpdateForm
from utils.pagination import make_pagination
from feedback.filters import FeedbackFilter


def index(request):
    f = FeedbackFilter(request.GET, queryset=Feedback.objects.all().order_by('-id'))
    pagination = make_pagination(
        request=request,
        object_list=f.qs,
        per_page=10
    )
    context = {
        'form':f.form,
        'f':pagination['page_obj'],
        'pages':pagination['pagination_range'],
    }
    return render(
        request, 'feedback/index.html', context=context
    )


def feedback_slug_no_page(request, id):
    f = Feedback.objects.filter(id=id).first()
    context = {
        'no_page':True,
        'f':f
    }
    return render(request, 'feedback/feedback_slug.html', context=context)



def feedback_slug_page(request, id):
    f = Feedback.objects.filter(id=id).first()
    p = Blog.objects.filter(slug=f.slug).first()
    if p is None:
        return redirect('feedback-slug-no-page', id)
    
    owner = True if p.owner==request.user else False
    
    form = FeedbackUpdateForm(instance=f)
    context = {
        'p':p,
        'f':f,
        'owner':owner,
        'id':p.id,
        'form':form,
        'form_action':reverse('feedback-slug-status-update', args=(id,))
    }
    return render(
        request, 'feedback/feedback_slug.html', context=context
    )


def feedback_slug_status_update(request, id):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['feedback_update_form_data'] = POST
    form = FeedbackUpdateForm(data=request.POST or None, instance=Feedback.objects.filter(id=id).first())
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        messages.success(request, 'Status do Feedback atualizado')
    return redirect('feedback-slug', id)

def feedback(request, slug):
    page = Blog.objects.filter(slug=slug).first()
    feedback_form_data = request.session.get('feedback_create_form_data', None)
    form = FeedbackcreateForm(
        feedback_form_data,
        initial={
            'slug':slug,
            'status':StatusFeedback.objects.filter(status='Não respondido').first()
        }
    )

    context = {
        'head_title':f'Feedback - {page.title}',
        'slug':slug,
        'page':page,
        'form':form,
        'text_button':'Enviar',
        'form_action':reverse('feedback_create', args=(slug,))
    }

    return render(
        request, 'feedback/feedback.html', context=context
    )



def feedback_create(request, slug):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['feedback_create_form_data'] = POST
    form = FeedbackcreateForm(POST)
    if form.is_valid():
        messages.success(request, 'Feedback criado')
        form.save()
        del(request.session['feedback_create_form_data'])
    return redirect('feedback', slug)


