# Generated by Django 4.0.5 on 2022-11-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_event_contract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='sales_contact',
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_signed',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='payement_due',
            field=models.DateTimeField(),
        ),
    ]
