# Generated by Django 4.1 on 2022-08-06 22:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('companies', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('state', models.BooleanField()),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeSlots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('access_point', models.ManyToManyField(to='companies.accesspoint')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.AddConstraint(
            model_name='timeslots',
            constraint=models.CheckConstraint(check=models.Q(('start__lte', models.F('end'))), name='start_before_end'),
        ),
    ]
