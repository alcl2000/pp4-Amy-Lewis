# Generated by Django 3.2.18 on 2023-03-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen_detectives', '0012_auto_20230317_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
