# Generated by Django 4.1.4 on 2022-12-19 21:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todolist_is_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='date',
        ),
        migrations.AddField(
            model_name='todolist',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
