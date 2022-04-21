from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User
from .models import Setting
# Create your views here.

def index(request):
    settings = Setting.objects.filter(user__isnull=True)
    if request.method == 'POST':
        app = request.POST.get('app', None)
        configkeys = request.POST.keys()
        for configkey in configkeys:
            if configkey == 'app' or configkey == 'csrfmiddlewaretoken':
                continue

            configvalue = request.POST.get(configkey)
            print(configvalue)
            try:
                config = settings.get(app=app, configkey=configkey)
                config.configvalue = configvalue
            except Setting.DoesNotExist:
                config = Setting(app=app, configkey=configkey, configvalue=configvalue)
            config.save()

    context = {}

    for setting in settings:
        context[f'{setting.app}_{setting.configkey}'] = setting.configvalue

    return render(request, 'settings/index.html', context)    

def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    settings = Setting.objects.filter(user=user_id)
    if request.method == 'POST':
        app = request.POST.get('app', None)
        configkeys = request.POST.keys()
        for configkey in configkeys:
            if configkey == 'app' or configkey == 'csrfmiddlewaretoken':
                continue

            configvalue = request.POST.get(configkey)
            try:
                config = settings.get(app=app, configkey=configkey)
                config.configvalue = configvalue
            except Setting.DoesNotExist:
                config = Setting(user=user, app=app, configkey=configkey, configvalue=configvalue)
            config.save()

    context = {
        'user': user,
    }

    for setting in settings:
        context[setting.configkey] = setting.configvalue

    return render(request, 'settings/user.html', context)

def app(request, app_id):
    settings = Setting.objects.filter(user__isnull=True, app=app_id)
    return render(request, 'settings/app.html', {'settings':settings})