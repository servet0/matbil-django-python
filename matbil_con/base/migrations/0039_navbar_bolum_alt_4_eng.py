# Generated by Django 4.2.7 on 2023-12-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_navbar_bolum_alt_1_eng_navbar_bolum_alt_2_eng_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='bolum_alt_4_eng',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]