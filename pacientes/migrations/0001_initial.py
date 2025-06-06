# Generated by Django 5.1.6 on 2025-02-16 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefone', models.CharField(blank=True, max_length=255, null=True)),
                ('queixa', models.CharField(choices=[('TDAH', 'TDAH'), ('D', 'Depressão'), ('A', 'Ansiedade'), ('TAG', 'Transtorno de ansiedade generalizada')], default='TDAH', max_length=4)),
                ('foto', models.ImageField(upload_to='fotos')),
                ('pagamento_em_dia', models.BooleanField(default=True)),
            ],
        ),
    ]
