# Generated by Django 4.2 on 2023-05-25 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquire',
            name='adults',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='enquire',
            name='children',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
