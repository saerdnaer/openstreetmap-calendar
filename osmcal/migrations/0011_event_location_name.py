# Generated by Django 2.2.6 on 2019-10-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osmcal', '0010_auto_20191010_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
