# Generated by Django 3.0 on 2019-12-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_auto_20191215_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='/avatar/default_avatar.jpg', upload_to='avatar/'),
        ),
    ]
