# Generated by Django 3.1.3 on 2020-11-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_text',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.TextField(null=True),
        ),
    ]