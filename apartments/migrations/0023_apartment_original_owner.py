# Generated by Django 2.1.5 on 2019-03-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0022_auto_20190303_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='original_owner',
            field=models.EmailField(max_length=255, null=True, verbose_name='email address'),
        ),
    ]
