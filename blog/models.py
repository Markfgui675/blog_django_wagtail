from django.db import models
from django.contrib.auth.models import User
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class Category(models.Model):
    name = models.CharField('Categoria', max_length=250)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.__str__()

class Home(Page): ...

class Blog(Page):
    date = models.DateField('Data')
    image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", help_text="Imagem principal do blog"
    )
    subtitle = models.TextField(max_length=500, blank=True)
    body = RichTextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    content_panels = [
        FieldPanel('date'),
        FieldPanel('title'),
        FieldPanel('category'),
        FieldPanel('image'),
        FieldPanel('subtitle'),
        FieldPanel('body')
    ]

class Email(models.Model):
    email = models.EmailField('E-mail')
