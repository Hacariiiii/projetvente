# Generated by Django 5.0.6 on 2024-05-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GP', '0002_user_delete_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mdp',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Username',
            new_name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='repassword',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
