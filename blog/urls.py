from django.urls import path
from blog import views as b
from feedback import views as f
from solicitacao import views as s

urlpatterns = [
    path('', b.index, name='home-index'),
    path('search/', b.search, name='search'),
    path('search/category/<category>/', b.search_category, name='search-category'),
    path('search/user/<user>/', b.search_user, name='search-user'),
    path('favoritos/', b.favoritos, name='favoritos'),
    path('favoritos/create/<int:id>/', b.create_favoritos, name='create-favoritos'),
    path('favoritos/delete/<int:id>/', b.delete_favoritos, name='delete-favoritos'),
    path('favoritos/search/', b.search_favoritos, name='search-favoritos'),
    path('solicitacao/', s.acesso_view, name='solicitacao'),
    path('solicitacao/create/', s.acesso_solicitacao, name='solicitacao_create'),
    path('logout/', b.logout_view, name='logout'),
    path('login/', b.login_view, name='login'),
    path('login/create/', b.login_create, name='login_create'),
    path('register/', b.register_view, name='register'),
    path('register/create', b.register_create, name='register_create'),
    path('<slug>/', b.blog, name='blog-page'),
    path('feedback/<slug>/', f.feedback, name='feedback'),
    path('feedback/<slug>/create/', f.feedback_create, name='feedback_create'),
]

