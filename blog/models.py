from django.db import models
from django.contrib.auth.models import User
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# Create your models here.

class Home(Page): ...

class Blog(Page):
    image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", help_text="Imagem principal do blog"
    )
    subtitle = models.TextField(max_length=500, blank=True)
    body = RichTextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    content_panels = [
        FieldPanel('title'),
        FieldPanel('image'),
        FieldPanel('subtitle'),
        FieldPanel('body'),
        FieldPanel('author')
    ]
