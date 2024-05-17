from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from .views import (
    index,
    solicitacao_page,
    solicitacao_status_update
)

@hooks.register('register_admin_urls')
def register_solicitacao_url():
    return [
        path('solicitacao/', index, name='solicitacao_admin'),
        path('solicitacao/<int:id>/', solicitacao_page, name='solicitacao_page'),
        path('solicitacao/<int:id>/update/', solicitacao_status_update, name='solicitacao_update'),
    ]

@hooks.register('register_admin_menu_item')
def register_solicitacao_menu_item():
    return MenuItem('Solicitacões', reverse('solicitacao_admin'), icon_name='form')
