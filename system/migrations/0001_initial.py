# Generated by Django 3.0 on 2019-12-15 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('nickname', models.CharField(max_length=32, verbose_name='昵称')),
                ('phone', models.CharField(max_length=11, null=True, unique=True)),
                ('avatar', models.FileField(default='/avatar/default_avatar.jpg', upload_to='avatar/')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('create_user', models.CharField(max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
