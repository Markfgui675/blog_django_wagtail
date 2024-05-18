from django.apps import AppConfig
from watson import search


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        post = self.get_model("Blog")
        search.register(post, fields=["category__name", "subtitle", "body", "owner__username", "owner__first_name", "owner__last_name", "slug"])
