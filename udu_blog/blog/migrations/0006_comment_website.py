# Generated by Django 5.1.7 on 2025-03-11 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='website',
            field=models.TextField(blank=True, null=True),
        ),
    ]
