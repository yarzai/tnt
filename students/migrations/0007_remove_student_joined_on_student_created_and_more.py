# Generated by Django 4.1.7 on 2023-03-15 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_student_joined_on_alter_student_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='joined_on',
        ),
        migrations.AddField(
            model_name='student',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
