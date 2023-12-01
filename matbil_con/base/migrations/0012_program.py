# Generated by Django 4.2.7 on 2023-12-01 12:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_cikti'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(blank=True, max_length=500, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='universite')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
