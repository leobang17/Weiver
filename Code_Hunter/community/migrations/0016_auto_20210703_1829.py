# Generated by Django 3.2.3 on 2021-07-03 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0015_alter_community_pub_dateonly'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='comment_count',
        ),
        migrations.AlterField(
            model_name='community',
            name='pub_dateonly',
            field=models.DateField(default=datetime.date(2021, 7, 3)),
        ),
    ]
