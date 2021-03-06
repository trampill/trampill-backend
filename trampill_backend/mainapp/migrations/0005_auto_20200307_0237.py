# Generated by Django 3.1.dev20200306182808 on 2020-03-06 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20200307_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_home',
            field=models.URLField(blank=True, help_text='External URL about the course paste here', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='desc',
            field=models.TextField(help_text='Make a description of your course is mandatory! :)'),
        ),
        migrations.AlterField(
            model_name='courseitem',
            name='episode_archive',
            field=models.URLField(blank=True, help_text='Please use dropbox or anything similar to attach your files, and hook the url to this field', null=True),
        ),
        migrations.AlterField(
            model_name='courseitem',
            name='episode_note',
            field=models.TextField(help_text='Note for this episode..'),
        ),
        migrations.AlterField(
            model_name='courseitem',
            name='episode_url',
            field=models.URLField(blank=True, help_text='You can use YouTube URL Here..', null=True),
        ),
    ]
