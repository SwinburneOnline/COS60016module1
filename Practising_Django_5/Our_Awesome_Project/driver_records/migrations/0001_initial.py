from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('fuel_type', models.CharField(max_length=20)),
                ('registration', models.CharField(max_length=20)),
                ('power', models.IntegerField(max_length=20)),
                ('transmission', models.CharField(max_length=20)),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('number_of_seats', models.CharField(max_length=20)),
                ('engine_cubic_capacity', models.CharField(max_length=20)),
                ('emission_class', models.CharField(max_length=5)),
                ('fuel_consumption', models.IntegerField()),
                ('production_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DriverRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('valid_driving_licence', models.BooleanField()),
                ('number_of_accidents', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]