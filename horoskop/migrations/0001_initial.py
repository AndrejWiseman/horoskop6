# Generated by Django 5.0.6 on 2024-05-31 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horoskop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('znak', models.CharField(max_length=50)),
                ('dnevni', models.TextField()),
                ('nedeljni', models.TextField()),
                ('mesecni', models.TextField()),
                ('godisnji', models.TextField()),
            ],
        ),
    ]
