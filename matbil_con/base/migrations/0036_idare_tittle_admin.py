# Generated by Django 4.2.7 on 2023-12-13 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0035_idare_text_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='idare',
            name='tittle_admin',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]