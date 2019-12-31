# Generated by Django 3.0 on 2019-12-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='deleted',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=765, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(null=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]
