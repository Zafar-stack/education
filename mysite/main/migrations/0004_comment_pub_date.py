# Generated by Django 3.2.5 on 2021-07-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210728_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(blank=True, default=''),
        ),
    ]