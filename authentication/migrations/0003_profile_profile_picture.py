# Generated by Django 2.1.5 on 2019-03-13 17:58

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='apartments/'),
        ),
    ]
