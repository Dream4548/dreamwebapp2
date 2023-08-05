# Generated by Django 4.2.2 on 2023-08-03 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='major',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webpage.major'),
        ),
        migrations.AlterField(
            model_name='student',
            name='prefix',
            field=models.IntegerField(),
        ),
    ]