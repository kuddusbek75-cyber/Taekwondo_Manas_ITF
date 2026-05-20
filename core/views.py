from django.shortcuts import render, redirect
from .models import Schedule, Rule

# Твой пароль для входа в админку
ADMIN_PASSWORD = '504126'

def index(request):
    """Главная страница сайта"""
    schedules = Schedule.objects.all()
    rules = Rule.objects.all().order_by('order')
    return render(request, 'index.html', {
        'schedules': schedules,
        'rules': rules,
    })

def admin_login(request):
    """Страница логина в админку"""
    error = ''
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password == ADMIN_PASSWORD:
            request.session['is_admin'] = True
            return redirect('admin_panel')
        else:
            error = 'Неверный пароль!'
    return render(request, 'admin_login.html', {'error': error})

def admin_logout(request):
    """Выход из админки"""
    request.session.flush()
    return redirect('index')

def admin_panel(request):
    """Панель управления расписанием и правилами"""
    # Проверка авторизации
    if not request.session.get('is_admin'):
        return redirect('admin_login')

    success = ''

    if request.method == 'POST':
        action = request.POST.get('action')

        # 1. СОХРАНЕНИЕ РАСПИСАНИЯ
        if action == 'save_schedule':
            for schedule in Schedule.objects.all():
                days_key = f'days_{schedule.id}'
                start_key = f'start_{schedule.id}'
                end_key = f'end_{schedule.id}'
                
                if days_key in request.POST:
                    schedule.days = request.POST.get(days_key, '').strip()
                    schedule.time_start = request.POST.get(start_key, '').strip()
                    schedule.time_end = request.POST.get(end_key, '').strip()
                    schedule.save()
            success = 'Расписание успешно обновлено!'

        # 2. ДОБАВЛЕНИЕ НОВОГО ПРАВИЛА
        elif action == 'add_rule':
            text = request.POST.get('rule_text', '').strip()
            rule_type = request.POST.get('rule_type', 'yes')
            if text:
                # Создаем правило и ставим его в конец очереди
                Rule.objects.create(
                    text=text, 
                    rule_type=rule_type, 
                    order=Rule.objects.count()
                )
                success = 'Новое правило добавлено!'

        # 3. УДАЛЕНИЕ ПРАВИЛА
        elif action == 'delete_rule':
            rule_id = request.POST.get('rule_id')
            if rule_id:
                Rule.objects.filter(id=rule_id).delete()
                success = 'Правило удалено!'

    # Загружаем свежие данные для отображения в таблицах
    schedules = Schedule.objects.all()
    rules = Rule.objects.all().order_by('order')

    return render(request, 'admin_panel.html', {
        'schedules': schedules,
        'rules': rules,
        'success': success,
    })