from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# Create your models here.

class Home(Page): ...

class Blog(Page):
    subtitle = models.TextField(max_length=500, blank=True)
    body = RichTextField(blank=False)

    content_panels = [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('body')
    ]
