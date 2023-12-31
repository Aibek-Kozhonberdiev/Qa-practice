# Generated by Django 4.2.5 on 2023-10-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_front_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datasets',
            options={'verbose_name': 'Набор данных', 'verbose_name_plural': 'Наборы данных'},
        ),
        migrations.AlterModelOptions(
            name='gratitude',
            options={'verbose_name': 'Картинку', 'verbose_name_plural': 'Благодарности'},
        ),
        migrations.AlterModelOptions(
            name='mentors',
            options={'verbose_name': 'Наставника', 'verbose_name_plural': 'Наставники'},
        ),
        migrations.AlterModelOptions(
            name='offers',
            options={'verbose_name': 'предложение', 'verbose_name_plural': 'Предложении'},
        ),
        migrations.AlterModelOptions(
            name='offersblack',
            options={'verbose_name': 'предложение', 'verbose_name_plural': 'Черные предложении'},
        ),
        migrations.AlterModelOptions(
            name='statistics',
            options={'verbose_name': 'Статистику', 'verbose_name_plural': 'Статистики'},
        ),
        migrations.AddField(
            model_name='speakers',
            name='link_1',
            field=models.CharField(default=1, max_length=50, verbose_name='ссылка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speakers',
            name='link_10',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ссылка'),
        ),
        migrations.AddField(
            model_name='speakers',
            name='link_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ссылка'),
        ),
        migrations.AddField(
            model_name='speakers',
            name='link_3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ссылка'),
        ),
        migrations.AddField(
            model_name='speakers',
            name='link_4',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ссылка'),
        ),
        migrations.AddField(
            model_name='speakers',
            name='link_5',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ссылка'),
        ),
        migrations.AddField(
            model_name='speakers',
            name='link_6',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ссылка'),
        ),
        migrations.AddField(
            model_name='speakers',
            name='link_7',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ссылка'),
        ),
        migrations.AddField(
            model_name='speakers',
            name='link_8',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ссылка'),
        ),
        migrations.AddField(
            model_name='speakers',
            name='link_9',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ссылка'),
        ),
        migrations.AlterField(
            model_name='speakers',
            name='offer_1',
            field=models.CharField(max_length=100, verbose_name='Предложение'),
        ),
        migrations.AlterField(
            model_name='speakers',
            name='offer_10',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Предложение 10'),
        ),
        migrations.AlterField(
            model_name='speakers',
            name='offer_2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Предложение 2'),
        ),
        migrations.AlterField(
            model_name='speakers',
            name='offer_3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Предложение 3'),
        ),
        migrations.AlterField(
            model_name='speakers',
            name='offer_4',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Предложение 4'),
        ),
        migrations.AlterField(
            model_name='speakers',
            name='offer_5',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Предложение 5'),
        ),
        migrations.AlterField(
            model_name='speakers',
            name='offer_6',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Предложение 6'),
        ),
        migrations.AlterField(
            model_name='speakers',
            name='offer_7',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Предложение 7'),
        ),
        migrations.AlterField(
            model_name='speakers',
            name='offer_8',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Предложение 8'),
        ),
        migrations.AlterField(
            model_name='speakers',
            name='offer_9',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Предложение 9'),
        ),
    ]
