# Generated by Django 5.0.6 on 2024-08-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0007_alter_roundmodel_tees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roundmodel',
            name='tees',
            field=models.CharField(choices=[('all', 'All Tees'), ('yellow', 'Yellow'), ('white', 'White'), ('red', 'Red')], default='yellow', max_length=6),
        ),
    ]
