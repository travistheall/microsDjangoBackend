# Generated by Django 3.0.6 on 2020-05-25 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recurapp', '0005_auto_20200525_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutdesc',
            fields=[
                ('nutrient_code', models.SmallIntegerField(db_column='Nutrient_code', primary_key=True, serialize=False)),
                ('nutrient_description', models.CharField(db_column='Nutrient_description', max_length=45)),
                ('tagname', models.CharField(blank=True, db_column='Tagname', max_length=15, null=True)),
                ('unit', models.CharField(db_column='Unit', max_length=10)),
                ('decimals', models.SmallIntegerField(db_column='Decimals')),
            ],
            options={
                'db_table': 'nutdesc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Fnddsnutval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nutrient_value', models.DecimalField(db_column='Nutrient_value', decimal_places=3, max_digits=8)),
                ('start_date', models.DateTimeField(db_column='Start_date')),
                ('end_date', models.DateTimeField(db_column='End_date')),
                ('food_code', models.ForeignKey(db_column='Food_code', on_delete=django.db.models.deletion.CASCADE, to='recurapp.MainDesc')),
                ('nutrient_code', models.ForeignKey(blank=True, db_column='Nutrient_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='recurapp.Nutdesc')),
            ],
            options={
                'db_table': 'fnddsnutval',
                'managed': True,
            },
        ),
    ]
