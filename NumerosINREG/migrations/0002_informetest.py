# Generated by Django 4.2.7 on 2023-11-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NumerosINREG', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='informeTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_incrementable', models.IntegerField()),
                ('columna_formato', models.CharField(editable=False, max_length=10)),
            ],
        ),
    ]