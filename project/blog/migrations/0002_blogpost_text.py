# Generated by Django 4.0.4 on 2022-04-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
