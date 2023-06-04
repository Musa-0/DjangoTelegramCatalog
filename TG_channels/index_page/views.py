from django.core.cache import cache
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from index_page.algoritm import get_valide_post, split
from index_page.fix import update_count
from index_page.models import *
from fuzzywuzzy import fuzz
from django.views import View
from random import choice

from django.http import HttpResponse



class HomeView(ListView):
    model = channels
    paginate_by = 31
    template_name = 'index_page/index.html'
    context_object_name = 'channels'
    def get_queryset(self):
        return channels.objects.order_by('-subscribers_count')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = categories.objects.all()
        categ = categories.objects.all()
        context['title'] = 'Tlgram-channels – поиск по Telegram каналам. Каталог телеграмм каналов.'
        context['description'] = 'Tlgram-channels – удобный поиск по телеграмм каналам, а также структурированный каталог, в котором собрано более чем 150000 Telegram каналов.'
        context['keywords'] = 'каталог, телеграм, telegram, канал, тг'
        context['range_categories'] = list(split(categ, round(len(categ)/8)))
        context['articles'] = last_articles = articles.objects.order_by("-id")[:6]
        context['c_c_b'] = 'Телеграм каналы'
        context['canon'] = self.request.build_absolute_uri()
        ads = list(paid_advertising.objects.all())
        try:
            ads = choice(ads)
        except:
            pass
        context['ad'] = ads
        return context
class HomeChatsView(ListView):
    model = chats
    paginate_by = 31
    template_name = 'index_page/index.html'
    context_object_name = 'channels'

    def get_queryset(self):
        return chats.objects.order_by('-subscribers_count')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tlgram-channels – поиск по Telegram чатам. Каталог телеграмм чатов.'
        context['description'] = 'Tlgram-channels – удобный поиск по телеграмм каналам, а также структурированный каталог, в котором собрано более чем 150000 Telegram каналов.'
        context['keywords'] = 'каталог, телеграм, telegram, чат, тг'
        categ = category_for_chats.objects.all()
        context['range_categories'] = list(split(categ, round(len(categ)/8)))
        context['articles'] = last_articles = articles.objects.order_by("-id")[:6]
        context['c_c_b'] = 'Телеграм чаты'
        context['canon'] = self.request.build_absolute_uri()
        ads = list(paid_advertising.objects.all())
        try:
            ads = choice(ads)
        except:
            pass
        context['ad'] = ads
        return context

class HomeBotsView(ListView):
    model = bots
    paginate_by = 31
    template_name = 'index_page/bots.html'
    context_object_name = 'bots'

    def get_queryset(self):
        return bots.objects.order_by('-id')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tlgram-channels – поиск по Telegram ботам. Каталог телеграмм ботов.'
        context['description'] = 'Tlgram-channels – удобный поиск по телеграмм ботам, а также структурированный каталог, в котором собрано множество Telegram ботов.'
        context['keywords'] = 'каталог, телеграм, telegram, бот, тг'
        context['articles'] = last_articles = articles.objects.order_by("-id")[:6]
        context['canon'] = self.request.build_absolute_uri()
        ads = list(paid_advertising.objects.all())
        try:
            ads = choice(ads)
        except:
            pass
        context['ad'] = ads
        return context

class HomeArticlesView(ListView):
    model = articles
    paginate_by = 16
    template_name = 'index_page/articles.html'
    context_object_name = 'articless'

    def get_queryset(self):
        return articles.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tlgram-channels – поиск по Telegram статьям. Каталог телеграмм статей.'
        context['description'] = 'Tlgram-channels – удобный поиск по телеграмм статьям, а также структурированный каталог, в котором собрано множество Telegram статей.'
        context['keywords'] = 'каталог, телеграм, telegram, статьи, тг'
        context['articles'] = last_articles = articles.objects.order_by("-id")[:6]
        return context
class ChannelViewForCategory(ListView):
    model = channels
    paginate_by = 31
    context_object_name = 'channels'
    template_name = 'index_page/index.html'
    def get_queryset(self):
        return channels.objects.select_related('category').filter(category__translit_category=self.kwargs.get("category"))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categ = categories.objects.all()
        cattitle = categories.objects.get(translit_category=self.kwargs.get("category")).name_categories
        context['category_name'] = cattitle
        context['title'] = f'Телеграмм каналы в категории «{cattitle}». Поиск по Telegram каналам. Каталог телеграмм каналов.'
        context['description'] = f'Полный список Телеграмм каналов в категории «{cattitle}», всегда актуальные данные.'
        context['keywords'] = f'поиск, каталог, телеграм, telegram, категория, {cattitle}'
        context['range_categories'] = list(split(categ, round(len(categ)/8)))
        context['articles']  = articles.objects.order_by("-id")[:6]
        context['c_c_b'] = 'Телеграм каналы'
        context['canon'] = self.request.build_absolute_uri()
        ads = list(paid_advertising.objects.all())
        try:
            ads = choice(ads)
        except:
            pass
        context['ad'] = ads
        return context

class ChatViewForCategory(ListView):
    model = chats
    paginate_by = 31
    context_object_name = 'channels'
    template_name = 'index_page/index.html'
    def get_queryset(self):
        return chats.objects.select_related('category').filter(category__translit_category=self.kwargs.get("category"))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categ = category_for_chats.objects.all()
        cattitle = category_for_chats.objects.get(translit_category=self.kwargs.get("category")).name_categories
        context['title'] = f'Телеграмм чаты в категории «{cattitle}». Поиск по Telegram чатам. Каталог телеграмм чатов.'
        context['description'] = f'Полный список Телеграмм чатов в категории «{cattitle}», всегда актуальные данные.'
        context['keywords'] = f'поиск, каталог, чат, телеграм, telegram, категория, {cattitle}'
        context['range_categories'] = list(split(categ, round(len(categ)/8)))
        context['articles']  = articles.objects.order_by("-id")[:6]
        context['category_name_chat'] = cattitle
        context['canon'] = self.request.build_absolute_uri()
        context['c_c_b'] = 'Телеграм чаты'
        ads = list(paid_advertising.objects.all())
        try:
            ads = choice(ads)
        except:
            pass
        context['ad'] = ads
        return context

def channel_ditail(request, page):
    dit_channel = channels.objects.get(pk=page)
    chnls = channels.objects.filter(category=dit_channel.category, subscribers_count__range=[0,dit_channel.subscribers_count*2]).exclude(pk=page)[:16]
    ad = paid_advertising.objects.all()
    ads = []
    for i in ad:
        if i.active:
            ads.append(i)
    try:
        ads = choice(ads)
    except:
        pass
    title = f'Телеграмм канал «{dit_channel.name}». Поиск по Telegram каналам. Каталог телеграмм каналов.'
    description = f"Телеграмм канал «{dit_channel.name}». {dit_channel.description}"
    keywords = f"поиск, каталог, телеграм, telegram, канал, {dit_channel.name}"
    context = {
        'dit_channel':dit_channel,
        'channels': chnls,
        "ad": ads,
        'title': title,
        'description': description,
        'keywords': keywords,
        'simil': " Похожие каналы",
        'canon': request.build_absolute_uri(),
    }
    return render(request, 'index_page/channel_ditail.html', context)

def chat_ditail(request, page):
    dit_channel = chats.objects.get(pk=page)
    chnls = chats.objects.filter(category_id=dit_channel.category, subscribers_count__range=[0,dit_channel.subscribers_count*2]).exclude(pk=page)[:16]
    ad = paid_advertising.objects.all()
    ads = []
    for i in ad:
        if i.active:
            ads.append(i)
    try:
        ads = choice(ads)
    except:
        pass
    title = f'Телеграмм чат «{dit_channel.name}». Поиск по Telegram чатам. Каталог телеграмм чатов.'
    description = f"Телеграмм чат «{dit_channel.name}». {dit_channel.description}"
    keywords = f"поиск, каталог, телеграм, telegram, чат, {dit_channel.name}"
    context = {
        'dit_channel':dit_channel,
        'channels': chnls,
        "ad": ads,
        'title':title,
        'description':description,
        'keywords':keywords,
        'simil': " Похожие чаты",
        'canon': request.build_absolute_uri(),
    }
    return render(request, 'index_page/channel_ditail.html', context)
def article_ditail(request, page):
    dit_article = articles.objects.get(pk=page)
    articless = articles.objects.order_by('created_at')[:1]
    title = f'Телеграмм статья «{dit_article.name}». Поиск по Telegram чтатьям. Каталог телеграмм чтатей.'
    description = f"Телеграмм статья «{dit_article.name}». {dit_article.content}"
    keywords = f"поиск, каталог, телеграм, telegram, статья, {dit_article.name}"
    context = {
        'article':dit_article,
        'articles':articless,
        'title':title,
        'description':description,
        'keywords':keywords,
        'canon': request.build_absolute_uri(),
    }
    return render(request, 'index_page/article_ditail.html', context)
def bot_ditail(request, page):
    dit_bot = bots.objects.get(pk=page)
    botss = bots.objects.order_by('id').exclude(pk=page)[:16]
    ad = paid_advertising.objects.all()
    ads = []
    for i in ad:
        if i.active:
            ads.append(i)
    try:
        ads = choice(ads)
    except:
        pass
    title = f'Телеграмм бот «{dit_bot.name}». Поиск по Telegram ботам. Каталог телеграмм ботам.'
    description = f"Телеграмм бот «{dit_bot.name}». {dit_bot.description}"
    keywords = f"поиск, каталог, телеграм, telegram, бот, {dit_bot.name}"
    context = {
        'bot':dit_bot,
        'bots': botss,
        "ad": ads,
        'title':title,
        'description':description,
        'keywords':keywords,
        'canon': request.build_absolute_uri(),
    }
    return render(request, 'index_page/bot_ditail.html', context)

def channel_search(request):
    search = request.GET.get('text', False)
    context = {}
    categ = categories.objects.all()
    last_articles = articles.objects.order_by("-id")[:6]
    title = f'Результаты поиска по запросу «{search}».'
    description = f"Результаты поиска по запросу «{search}». Tlgram-channels – удобный поиск по телеграмм каналам."
    keywords = f"поиск, каталог, телеграм, telegram, канал, {search}"
    if search:
        posts = get_valide_post(channels.objects.all(), search)
        context = {'channels': posts, "articles": last_articles,'canon': request.build_absolute_uri(), "range_categories": list(split(categ, len(categ)//8)),'title':title,'description':description,'keywords':keywords, 'search_words':search}
    return render(request, 'index_page/index.html', context)

def sitemap_view(request):
    url = request.build_absolute_uri().split('/')[-1]
    print(url)
    return render(request, f'sitemaps/{url}',content_type="application/xml")
