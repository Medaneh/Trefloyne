# Generated by Django 5.0.6 on 2024-07-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hole',
            name='hole',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='hole',
            name='putts',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hole',
            name='score',
            field=models.IntegerField(max_length=2),
        ),
    ]
