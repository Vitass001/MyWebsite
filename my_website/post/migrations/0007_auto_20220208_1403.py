# Generated by Django 3.1.3 on 2022-02-08 12:03

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20220208_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='money',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='size',
            field=models.CharField(default=2, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=post.models.upload_location, width_field='width_field'),
        ),
    ]
