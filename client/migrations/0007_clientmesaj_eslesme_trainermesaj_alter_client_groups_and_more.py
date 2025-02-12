# Generated by Django 4.2.7 on 2023-11-29 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0004_alter_trainer_options_alter_trainer_managers_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('client', '0006_alter_clientprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientMesaj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icerik', models.TextField()),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('alan_trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='Eslesme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TrainerMesaj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icerik', models.TextField()),
                ('tarih', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='groups',
            field=models.ManyToManyField(related_name='client_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='client',
            name='user_permissions',
            field=models.ManyToManyField(related_name='client_permissions', to='auth.permission'),
        ),
        migrations.DeleteModel(
            name='ClientProfile',
        ),
        migrations.AddField(
            model_name='trainermesaj',
            name='alan_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trainermesaj',
            name='gonderen_trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.trainer'),
        ),
        migrations.AddField(
            model_name='eslesme',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eslesme',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.trainer'),
        ),
        migrations.AddField(
            model_name='clientmesaj',
            name='gonderen_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
