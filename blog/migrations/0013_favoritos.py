# Generated by Django 5.0.6 on 2024-05-22 17:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_delete_email'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favoritos', models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]