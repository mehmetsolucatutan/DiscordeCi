# Generated by Django 4.1.2 on 2022-11-03 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FirmaApp', '0006_alter_discord_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discord',
            name='FirmaID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirmaApp.firma'),
        ),
    ]
