# Generated by Django 3.2.3 on 2021-07-03 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0017_merge_20210703_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='pub_dateonly',
            field=models.DateField(default=datetime.date(2021, 7, 4)),
        ),
    ]
