# Generated by Django 4.0.2 on 2022-03-01 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacienti', '0002_alter_pacient_nrgestiune'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacient',
            name='observatii',
            field=models.TextField(blank=True),
        ),
    ]
