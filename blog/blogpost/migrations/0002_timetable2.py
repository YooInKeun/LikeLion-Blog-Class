# Generated by Django 3.0.6 on 2020-05-23 14:16

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_json', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
    ]
