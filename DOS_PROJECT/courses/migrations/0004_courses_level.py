# Generated by Django 4.2 on 2023-04-30 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_courses_options_alter_courses_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='Level',
            field=models.CharField(default='BEGINNER', max_length=100),
        ),
    ]
