# Generated by Django 4.2.7 on 2023-11-30 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_navbar_bolum_navbar_bolum_alt_1_navbar_bolum_alt_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='akademik',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='akademik_alt_1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='akademik_alt_2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='akademik_alt_3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='akademik_alt_4',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='akademik_alt_5',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='akademik_alt_6',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='akademik_alt_7',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]