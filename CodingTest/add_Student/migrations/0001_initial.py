# Generated by Django 3.2.8 on 2021-10-19 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_Student.classroom')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_Student.level')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_Student.school')),
            ],
        ),
        migrations.AddField(
            model_name='level',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_Student.school'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_Student.level'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_Student.school'),
        ),
    ]
