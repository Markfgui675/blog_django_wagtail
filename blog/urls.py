from django.urls import include, path
from blog import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('<slug>/', views.blog, name='blog-page')
]

