from django.urls import include, path
from blog import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('register/', views.register_view, name='register'),
    path('register/create', views.register_create, name='register_create'),
    path('<slug>/', views.blog, name='blog-page')
]

