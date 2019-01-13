# Generated by Django 2.1.2 on 2019-01-01 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cutting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=15)),
                ('macro_name', models.CharField(max_length=15)),
                ('macro_code', models.CharField(max_length=30)),
                ('distance', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField(blank=True, default=None)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['material'],
            },
        ),
        migrations.CreateModel(
            name='Macro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=15)),
                ('macro_name', models.CharField(max_length=30)),
                ('macro_code', models.CharField(max_length=100)),
                ('canvas_code', models.TextField(blank=True)),
                ('rnc_code', models.TextField(blank=True)),
                ('cad_code', models.TextField(blank=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['macro_name'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=1)),
                ('kind', models.CharField(max_length=30)),
                ('standards', models.CharField(max_length=30)),
                ('texture', models.CharField(default='ss400', max_length=30)),
                ('length', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('macros', models.TextField(blank=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=30)),
                ('project', models.CharField(max_length=30)),
                ('workpackage', models.CharField(max_length=30)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('workpiece', models.CharField(max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='material',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='macro.Order'),
        ),
        migrations.AddField(
            model_name='cutting',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='macro.Material'),
        ),
    ]
