# Generated by Django 2.1.5 on 2019-03-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0035_auto_20190315_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='vote_sum',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
