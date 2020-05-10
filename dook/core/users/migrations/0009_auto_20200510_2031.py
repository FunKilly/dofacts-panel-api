# Generated by Django 3.0.4 on 2020-05-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200510_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Invitation with given email already exists.'}, max_length=254, unique=True, verbose_name='e-mail address'),
        ),
    ]