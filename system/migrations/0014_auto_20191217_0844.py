# Generated by Django 3.0 on 2019-12-17 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0013_remove_user_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar/default_avatar.jpg', upload_to='avatar/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=320, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(null=True),
        ),
    ]
