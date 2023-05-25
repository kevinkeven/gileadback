# Generated by Django 4.2 on 2023-05-24 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destination', '0001_initial'),
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='accommodation_images/')),
                ('activities', models.ManyToManyField(limit_choices_to=models.Q(('destination', models.F('destination'))), to='shared.activity')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accommodations', to='destination.destination')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accommodation', to='shared.gallery')),
            ],
        ),
        migrations.CreateModel(
            name='InsiderTip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insidertip', to='accommodation.accommodation')),
            ],
            options={
                'verbose_name_plural': 'InsiderTips',
            },
        ),
        migrations.CreateModel(
            name='Glance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='accommodation/glance_images/')),
                ('description', models.TextField()),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='glance', to='accommodation.accommodation')),
            ],
            options={
                'verbose_name_plural': 'Glances',
            },
        ),
        migrations.CreateModel(
            name='ExpertView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expertview', to='accommodation.accommodation')),
            ],
            options={
                'verbose_name_plural': 'ExpertViews',
            },
        ),
    ]
