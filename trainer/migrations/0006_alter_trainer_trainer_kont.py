# Generated by Django 4.2.7 on 2023-12-01 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0005_trainer_groups_trainer_trainer_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='trainer_kont',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
