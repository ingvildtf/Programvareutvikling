# Generated by Django 2.1.5 on 2019-03-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0019_auto_20190302_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='latitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='longitude',
            field=models.CharField(max_length=50),
        ),
    ]