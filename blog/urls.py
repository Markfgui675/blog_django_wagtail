from django.urls import include, path
from blog import views as b
from feedback import views as f

urlpatterns = [
    path('', b.index, name='home-index'),
    path('about/', b.about, name='about'),
    path('acesso/', b.about, name='acesso'),
    path('logout/', b.logout_view, name='logout'),
    path('login/', b.login_view, name='login'),
    path('login/create/', b.login_create, name='login_create'),
    path('register/', b.register_view, name='register'),
    path('register/create', b.register_create, name='register_create'),
    path('<slug>/', b.blog, name='blog-page'),
    path('feedback/<slug>/', f.feedback, name='feedback'),
    path('feedback/<slug>/create/', f.feedback_create, name='feedback_create'),
]

