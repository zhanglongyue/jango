# Generated by Django 3.0 on 2019-12-15 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_auto_20191215_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='create_user',
            field=models.IntegerField(default='0'),
        ),
    ]