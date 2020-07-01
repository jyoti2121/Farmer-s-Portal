# Generated by Django 2.2.10 on 2020-04-28 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0007_labour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('task_date', models.DateField()),
                ('task_priority', models.CharField(max_length=50)),
                ('task_complete', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='labour',
            name='labour_salary',
            field=models.IntegerField(),
        ),
    ]
