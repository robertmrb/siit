# Generated by Django 4.0.2 on 2022-02-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacienti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacient',
            name='nrgestiune',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
