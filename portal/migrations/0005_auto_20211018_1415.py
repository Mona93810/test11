# Generated by Django 3.2.7 on 2021-10-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20211018_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='students_model',
            name='stdnt_Branch',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students_model',
            name='stdnt_is_Active',
            field=models.BooleanField(default=False),
        ),
    ]