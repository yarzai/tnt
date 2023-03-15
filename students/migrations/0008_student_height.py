# Generated by Django 4.1.7 on 2023-03-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_remove_student_joined_on_student_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='height',
            field=models.DecimalField(decimal_places=2, default=150.3, max_digits=5),
        ),
    ]
