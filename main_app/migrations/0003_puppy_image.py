# Generated by Django 5.0.4 on 2024-04-12 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_age_puppy_age_in_months'),
    ]

    operations = [
        migrations.AddField(
            model_name='puppy',
            name='image',
            field=models.CharField(default='https://www.thesprucepets.com/thmb/1', max_length=100),
        ),
    ]