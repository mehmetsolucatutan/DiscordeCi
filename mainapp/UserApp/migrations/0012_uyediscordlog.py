# Generated by Django 4.1.2 on 2022-11-04 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0011_uyewalletlog_uyewalletlogtarih'),
    ]

    operations = [
        migrations.CreateModel(
            name='UyeDiscordLog',
            fields=[
                ('UyeDiscordLogID', models.AutoField(primary_key=True, serialize=False)),
                ('DiscordID', models.CharField(max_length=18, null=True, unique=True)),
                ('TOKEN', models.CharField(max_length=18)),
                ('TOKENDURUM', models.BooleanField(default=False)),
                ('UyeDiscordLogTARIH', models.DateTimeField(auto_now_add=True)),
                ('UyeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.uye')),
            ],
            options={
                'db_table': 'UyeDiscordLog',
            },
        ),
    ]
