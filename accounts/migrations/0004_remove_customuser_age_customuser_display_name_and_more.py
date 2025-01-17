# Generated by Django 4.2.7 on 2025-01-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_api_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='display_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='draws',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='losses',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='wins',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
