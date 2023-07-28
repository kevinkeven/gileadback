# Generated by Django 4.2.2 on 2023-07-28 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0002_alter_itineraries_price'),
        ('enquire', '0002_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquire',
            name='itinerary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enquiries', to='itineraries.itineraries'),
        ),
    ]
