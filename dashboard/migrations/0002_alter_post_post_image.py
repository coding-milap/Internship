# Generated by Django 4.2.2 on 2023-06-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, default='static/dashboard/images/img1.jpg', null=True, upload_to='posts'),
        ),
    ]