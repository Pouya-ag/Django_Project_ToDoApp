# Generated by Django 3.2.18 on 2023-03-03 08:10

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0003_alter_tasks_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=accounts.models.User),
        ),
    ]
