# Generated by Django 5.1.6 on 2025-03-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_user_program_remove_user_section_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
