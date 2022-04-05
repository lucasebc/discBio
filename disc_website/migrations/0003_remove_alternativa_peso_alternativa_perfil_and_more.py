# Generated by Django 4.0.2 on 2022-03-21 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disc_website', '0002_aluno_teste_turma_resultado_aluno_turma_alternativa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alternativa',
            name='peso',
        ),
        migrations.AddField(
            model_name='alternativa',
            name='perfil',
            field=models.IntegerField(choices=[(1, 'dominância'), (2, 'influência'), (3, 'cautela'), (4, 'estabilidade')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resultado',
            name='data_fim',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='data_ini',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='turma',
            name='curso',
            field=models.CharField(max_length=50),
        ),
    ]