# Generated by Django 3.0.3 on 2020-03-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200310_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryStrings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=200)),
            ],
        ),
    ]
