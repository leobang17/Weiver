# Generated by Django 3.2.3 on 2021-07-03 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0021_remove_communitycomment_author_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitycomment',
            name='tag',
            field=models.CharField(default='공지', max_length=16),
        ),
    ]
