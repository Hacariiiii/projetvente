# Generated by Django 5.0.6 on 2024-05-29 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GP', '0010_rename_userr_user_remove_product_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namee', models.CharField(blank=True, max_length=200, null=True)),
                ('numeroo', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
