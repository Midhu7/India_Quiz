# Generated by Django 4.0.6 on 2022-07-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_rename_user_id_highscore_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='submission_date_and_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
