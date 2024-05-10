from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'principal':True
    }
    return render(request, 'blog/home.html', context=context)
