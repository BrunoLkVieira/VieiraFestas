# Generated by Django 4.1.7 on 2023-07-19 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PegeMonte', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='festa',
            old_name='descricacao',
            new_name='descricao',
        ),
    ]
