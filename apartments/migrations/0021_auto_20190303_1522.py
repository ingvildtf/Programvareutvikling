# Generated by Django 2.1.5 on 2019-03-03 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0020_auto_20190302_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='latitude',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='longitude',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
