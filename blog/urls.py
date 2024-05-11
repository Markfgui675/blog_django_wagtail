from django.urls import include, path
from blog import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('<slug>/', views.blog, name='blog-page'),
    path('about/', views.about, name='about')
]

