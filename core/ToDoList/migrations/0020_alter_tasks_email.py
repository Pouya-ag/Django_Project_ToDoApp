# Generated by Django 3.2.18 on 2023-03-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0019_alter_tasks_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
