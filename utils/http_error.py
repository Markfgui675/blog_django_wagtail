from django.http import Http404

def HttpPostError(request):
    if not request.POST:
        raise Http404()
