# Generated by Django 4.0.6 on 2022-07-28 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_answer_correct_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attempt',
            old_name='user_id',
            new_name='user',
        ),
    ]
