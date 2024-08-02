# Generated by Django 5.0.6 on 2024-08-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_roundmodel_is_front_9_roundmodel_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='roundmodel',
            name='fairways',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roundmodel',
            name='greens',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roundmodel',
            name='putts',
            field=models.IntegerField(default=0),
        ),
    ]
