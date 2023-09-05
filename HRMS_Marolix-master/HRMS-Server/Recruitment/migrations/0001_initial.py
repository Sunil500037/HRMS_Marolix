# Generated by Django 4.2.1 on 2023-07-06 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('dateOfPosting', models.DateField()),
                ('responsibilities', models.TextField()),
                ('qualifications', models.TextField()),
                ('experience', models.IntegerField()),
            ],
        ),
    ]
