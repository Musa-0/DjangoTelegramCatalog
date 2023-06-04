from django.contrib import admin

from django.contrib.auth.models import Group
from index_page.models import channels, chats, bots, categories, articles, paid_advertising
from django.forms import TextInput, Textarea
from index_page import models

admin.site.unregister(Group)

@admin.register(models.channels)
class ChannelsAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'category', 'subscribers_count']
    save_as = True
    save_on_top = True
@admin.register(models.chats)
class ChatsAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'category', 'subscribers_count']

@admin.register(models.bots)
class BotsAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'description']

@admin.register(models.categories)
class CatigoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'translit_category': ('name_categories',)}
    list_display = ['id','name_categories','count']

@admin.register(models.paid_advertising)
class Paid_AdvertisingAdmin(admin.ModelAdmin):
    list_display = ['id','name','preview','text','active']

@admin.register(models.articles)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','name','preview','content']

@admin.register(models.category_for_chats)
class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'translit_category': ('name_categories',)}
    list_display = ['id','name_categories','count']

