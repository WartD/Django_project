
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')], max_length=100)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('age', models.IntegerField()),
                ('activity', models.CharField(choices=[('Сидячий (мало или отсутствует физическая активность)',
                                                        'Сидячий (мало или отсутствует физическая активность)'),
                                                       ('Легкая активность (1-3 дня в неделю)',
                                                        'Легкая активность (1-3 дня в неделю)'),
                                                       ('Умеренная активность (3-5 дней в неделю)',
                                                        'Умеренная активность (3-5 дней в неделю)'),
                                                       ('Очень активный (6-7 дней в неделю)',
                                                        'Очень активный (6-7 дней в неделю)'),
                                                       ('Супер активный (два раза в день)',
                                                        'Супер активный (два раза в день)')], max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Details',
            },
        ),
    ]