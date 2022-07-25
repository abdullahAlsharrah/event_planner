# Generated by Django 4.0.6 on 2022-07-25 21:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_name_alter_event_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='email',
            field=models.CharField(max_length=250, validators=[django.core.validators.EmailValidator(message='invalid email')]),
        ),
    ]