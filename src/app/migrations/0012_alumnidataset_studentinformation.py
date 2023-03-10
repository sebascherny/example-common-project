# Generated by Django 3.2.10 on 2023-02-04 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_customuser_is_sports'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumniDataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='StudentInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_in_sheet', models.IntegerField()),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('employer', models.CharField(blank=True, max_length=500)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('graduation_year', models.IntegerField(blank=True, null=True)),
                ('major', models.CharField(blank=True, max_length=200)),
                ('college', models.CharField(blank=True, max_length=200)),
                ('linkedin_page', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('industry_type', models.CharField(blank=True, max_length=200)),
                ('date_added', models.DateField()),
                ('alumni_dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.alumnidataset')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
