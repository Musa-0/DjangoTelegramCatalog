from django.http import HttpResponse
from django.shortcuts import render
from index_page.models import *
from django.core.cache import cache

#
def fix():
    for i in bots.objects.all():
        i.category = categories.objects.get(name_categories=i.category).pk
        i.save()
def update_count(request):
    cache.clear()
    for i in categories.objects.all():
        i.count = channels.objects.filter(category_id=i.id).count()
        i.save()
    for i in category_for_chats.objects.all():
        i.count = chats.objects.filter(category_id=i.id).count()
        i.save()
    return HttpResponse("<h1>Счетчик обновлен!!</h1>")
