# Generated by Django 3.2 on 2021-11-28 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_userprofile_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['-score']},
        ),
        migrations.AddField(
            model_name='task',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
