# Generated by Django 4.1.6 on 2023-02-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_verify_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='new_password',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='новый пароль'),
        ),
    ]
