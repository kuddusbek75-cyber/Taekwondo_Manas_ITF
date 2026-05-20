from django.db import models

class Schedule(models.Model):
    GROUP_CHOICES = [
        ('children', 'Детская группа'),
        ('women', 'Женская группа'),
        ('men', 'Мужская группа'),
    ]
    group = models.CharField(max_length=20, choices=GROUP_CHOICES, unique=True, verbose_name='Группа')
    days = models.CharField(max_length=100, verbose_name='Дни недели')
    time_start = models.CharField(max_length=10, verbose_name='Начало')
    time_end = models.CharField(max_length=10, verbose_name='Конец')

    def __str__(self):
        return self.get_group_display()

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'


class Rule(models.Model):
    TYPE_CHOICES = [
        ('yes', 'Обязательно ✅'),
        ('no', 'Запрещено ❌'),
    ]
    rule_type = models.CharField(max_length=5, choices=TYPE_CHOICES, verbose_name='Тип')
    text = models.CharField(max_length=300, verbose_name='Текст правила')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['order']
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'