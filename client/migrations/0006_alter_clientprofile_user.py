# Generated by Django 4.2.7 on 2023-11-28 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_clientprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
    ]
