# Generated by Django 5.0.3 on 2024-04-03 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usuarios',
                'managed': False,
            },
        ),
    ]
