# Generated by Django 4.1.3 on 2022-11-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeNoteRelease',
            fields=[
                ('type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
    ]
