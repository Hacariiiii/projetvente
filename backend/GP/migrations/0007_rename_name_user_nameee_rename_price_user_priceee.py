# Generated by Django 5.0.6 on 2024-05-28 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GP', '0006_rename_passcmd_user_name_user_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='nameee',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='price',
            new_name='priceee',
        ),
    ]
