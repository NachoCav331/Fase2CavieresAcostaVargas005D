# Generated by Django 3.1.2 on 2020-10-29 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_tipo_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipo',
            old_name='status',
            new_name='tipos',
        ),
    ]