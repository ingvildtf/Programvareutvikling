# Generated by Django 2.1.5 on 2019-03-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0036_apartment_vote_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='review_made',
            field=models.BooleanField(default=False),
        ),
    ]
