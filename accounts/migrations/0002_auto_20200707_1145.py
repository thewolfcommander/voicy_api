# Generated by Django 3.0.7 on 2020-07-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='following',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followers_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='following_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
