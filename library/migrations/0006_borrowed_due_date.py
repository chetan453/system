# Generated by Django 3.2 on 2021-04-25 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20210425_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
