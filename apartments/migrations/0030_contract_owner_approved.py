# Generated by Django 2.1.5 on 2019-03-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0029_remove_contract_owner_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='owner_approved',
            field=models.BooleanField(null=True),
        ),
    ]
