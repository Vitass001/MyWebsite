# Generated by Django 3.1.3 on 2022-02-08 11:10

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field=100, null=True, upload_to=post.models.upload_location, width_field=100),
        ),
    ]