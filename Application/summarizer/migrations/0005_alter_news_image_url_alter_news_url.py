# Generated by Django 5.0.6 on 2024-07-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summarizer', '0004_rename_content_news_full_text_remove_news_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_url',
            field=models.URLField(max_length=700),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.URLField(max_length=700),
        ),
    ]
