from django.db import migrations

def add_initial_data(apps, schema_editor):
    Schedule = apps.get_model('core', 'Schedule')
    Rule = apps.get_model('core', 'Rule')

    Schedule.objects.create(group='children', days='Пн — Ср — Пт', time_start='17:00', time_end='18:30')
    Schedule.objects.create(group='women',    days='Пн — Ср — Пт', time_start='19:00', time_end='20:30')
    Schedule.objects.create(group='men',      days='Вт — Чт — Сб', time_start='19:00', time_end='20:30')

    rules = [
        ('yes', 'Приходить на тренировку вовремя, в чистой форме (добок)'),
        ('yes', 'Уважать тренера и партнёров по тренировке'),
        ('yes', 'Соблюдать дисциплину и тишину во время занятий'),
        ('yes', 'Снимать обувь перед входом в зал'),
        ('no',  'Запрещено использовать телефон во время тренировки'),
        ('no',  'Запрещено есть и жевать жвачку в зале'),
        ('no',  'Запрещено грубить и провоцировать конфликты'),
        ('no',  'Запрещено приходить в нетрезвом состоянии'),
    ]
    for i, (t, text) in enumerate(rules):
        Rule.objects.create(rule_type=t, text=text, order=i)

class Migration(migrations.Migration):
    dependencies = [('core', '0001_initial')]
    operations = [migrations.RunPython(add_initial_data)]