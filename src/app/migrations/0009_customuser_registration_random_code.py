# Generated by Django 3.2.10 on 2022-11-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20221031_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='registration_random_code',
            field=models.CharField(default='asd', max_length=100),
            preserve_default=False,
        ),
    ]