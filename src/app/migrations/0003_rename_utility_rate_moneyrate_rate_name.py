# Generated by Django 3.2.10 on 2022-11-29 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_moneyrate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moneyrate',
            old_name='utility_rate',
            new_name='rate_name',
        ),
    ]