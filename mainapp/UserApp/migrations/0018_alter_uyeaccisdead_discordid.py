# Generated by Django 4.1.2 on 2022-11-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0017_uyeaccisdead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uyeaccisdead',
            name='DiscordID',
            field=models.CharField(max_length=25),
        ),
    ]
