# Generated by Django 2.0.9 on 2019-02-27 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20190208_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(blank=True, choices=[('dr', 'Dr.'), ('frau', 'Frau.'), ('herr', 'Herr.'), ('mr', 'Mr.'), ('ms', 'Ms.'), ('mrs', 'Mrs.'), ('miss', 'Miss.'), ('prof', 'Prof.')], help_text='Choices: dr, frau, herr, mr, ms, mrs, miss, prof', max_length=16, null=True),
        ),
    ]
