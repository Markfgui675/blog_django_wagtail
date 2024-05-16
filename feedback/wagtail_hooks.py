from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem


from .views import (
    index,
    feedback_slug_page,
    feedback_slug_no_page,
    feedback_slug_status_update
)

@hooks.register('register_admin_urls')
def register_feedback_urls():
    return [
        path('feedbacks/', index, name='feedbacks'),
        path('feedbacks/<int:id>/', feedback_slug_page, name='feedback-slug'),
        path('feedbacks/no-page/<int:id>/', feedback_slug_no_page, name='feedback-slug-no-page'),
        path('feedbacks/<int:id>/update/', feedback_slug_status_update, name='feedback-slug-status-update')
    ]

@hooks.register('register_admin_menu_item')
def register_feedback_menu_item():
    return MenuItem('Feedbacks', reverse('feedbacks'), icon_name='comment')
