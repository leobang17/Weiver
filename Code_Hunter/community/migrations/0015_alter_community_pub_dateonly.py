# Generated by Django 3.2.3 on 2021-07-01 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0014_remove_community_today_or_not'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='pub_dateonly',
            field=models.DateField(default=datetime.date(2021, 7, 2)),
        ),
    ]
