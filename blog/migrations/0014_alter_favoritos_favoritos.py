# Generated by Django 5.0.6 on 2024-05-22 17:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_favoritos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritos',
            name='favoritos',
            field=models.ManyToManyField(null=True, related_name='favoritos', to=settings.AUTH_USER_MODEL),
        ),
    ]
