from django.db import models
from django.contrib.auth.models import User
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# Create your models here.

class Home(Page): ...

class Blog(Page):
    subtitle = models.TextField(max_length=500, blank=True)
    body = RichTextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    content_panels = [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('body'),
        FieldPanel('author')
    ]
