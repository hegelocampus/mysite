# Generated by Django 3.0.3 on 2020-02-26 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quetion_text',
            new_name='question_text',
        ),
    ]
