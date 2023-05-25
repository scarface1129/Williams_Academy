# Generated by Django 4.2 on 2023-05-22 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_curriculum_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_number', models.IntegerField()),
                ('module_name', models.CharField(max_length=50)),
                ('video', models.FileField(blank=True, null=True, upload_to='media')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.curriculum')),
            ],
        ),
    ]
