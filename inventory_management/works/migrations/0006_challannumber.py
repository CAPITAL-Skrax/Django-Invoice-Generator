# Generated by Django 2.0.7 on 2018-07-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_auto_20180719_0514'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallanNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challan_number', models.IntegerField()),
            ],
        ),
    ]
