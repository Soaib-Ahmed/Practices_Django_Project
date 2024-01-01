# Generated by Django 3.2 on 2023-12-31 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_moneytransfer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moneytransfer',
            name='receiver',
        ),
        migrations.AddField(
            model_name='moneytransfer',
            name='receiver_account_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='moneytransfer',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
