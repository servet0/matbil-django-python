# Generated by Django 4.2.7 on 2023-11-30 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(blank=True, max_length=500, null=True)),
                ('home', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
