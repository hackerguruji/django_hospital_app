# Generated by Django 3.2 on 2021-05-31 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=122)),
                ('lname', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('age', models.CharField(max_length=122)),
                ('work', models.TextField(max_length=122)),
                ('worktype', models.TextField(max_length=122)),
                ('pain', models.TextField(max_length=122)),
                ('bleeding', models.TextField(max_length=122)),
                ('burning', models.TextField(max_length=122)),
                ('itching', models.TextField(max_length=122)),
                ('constipation', models.TextField(max_length=122)),
                ('discharge', models.TextField(max_length=122)),
                ('prolepse', models.TextField(max_length=122)),
                ('anus', models.TextField(max_length=122)),
                ('othercom', models.TextField(max_length=122)),
                ('familyten', models.TextField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]
