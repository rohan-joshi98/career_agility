# Generated by Django 2.1.5 on 2020-03-03 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('people', 'PEOPLE'), ('brand', 'BRAND'), ('operation', 'OPERATION'), ('blank', ' ')], default=' ', max_length=9)),
            ],
        ),
    ]
