# Generated by Django 4.1.2 on 2022-11-03 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FirmaApp', '0006_alter_discord_options'),
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uye',
            options={'verbose_name': 'Uye', 'verbose_name_plural': 'Uyeler'},
        ),
        migrations.CreateModel(
            name='UyeAcc',
            fields=[
                ('UyeAccID', models.AutoField(primary_key=True, serialize=False)),
                ('UyeAccTOKEN', models.CharField(max_length=128)),
                ('FirmaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirmaApp.firma')),
                ('UyeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.uye')),
            ],
            options={
                'db_table': 'UyeAcc',
            },
        ),
    ]
