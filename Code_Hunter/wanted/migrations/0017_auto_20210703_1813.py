# Generated by Django 3.2.3 on 2021-07-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wanted', '0016_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quest',
            name='tags',
        ),
        migrations.AlterField(
            model_name='quest',
            name='code',
            field=models.TextField(blank=True, default=''),
        ),
    ]
