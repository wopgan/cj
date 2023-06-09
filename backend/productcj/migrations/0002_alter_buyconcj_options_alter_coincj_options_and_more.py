# Generated by Django 4.1.7 on 2023-03-28 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productcj', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyconcj',
            options={'verbose_name': 'BuyCoinCJ', 'verbose_name_plural': 'BuyCoinsCJ'},
        ),
        migrations.AlterModelOptions(
            name='coincj',
            options={'verbose_name': 'CoinCJ', 'verbose_name_plural': 'CoinsCJ'},
        ),
        migrations.AlterField(
            model_name='buyconcj',
            name='buying',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productcj.coincj', verbose_name='Produto'),
        ),
    ]
