# Generated by Django 4.0 on 2022-01-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tel',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
