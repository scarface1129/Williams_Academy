# Generated by Django 4.2 on 2023-05-28 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_reviews_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
