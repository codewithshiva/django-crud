# Generated by Django 3.1.3 on 2022-07-09 13:12

import crud.models
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenreModel',
            fields=[
                ('Genre', models.CharField(max_length=60, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MoviesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=60, validators=[django.core.validators.MinLengthValidator(3)])),
                ('ReleaseDate', models.DateField(default=datetime.date.today)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Ratings', models.DecimalField(decimal_places=1, max_digits=3, validators=[crud.models.MoviesModel.validate_Ratings])),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.genremodel')),
            ],
        ),
    ]
