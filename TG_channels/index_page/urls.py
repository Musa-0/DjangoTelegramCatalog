from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from . import fix
from .views import *

urlpatterns = [
    re_path('sitemap.xml', sitemap_view),
    re_path('sitemap-[0-9]*.xml', sitemap_view),
    path('', cache_page(6000)(HomeView.as_view()), name='index'),
    path('channel/categories/<str:category>/', cache_page(6000)(ChannelViewForCategory.as_view()),name="channel_by_category"),
    path("channel/<int:page>/", channel_ditail, name="channel_ditail"),
    path("search/", channel_search, name="search"),
    path('chats/categories/<str:category>/', cache_page(6000)(ChatViewForCategory.as_view()), name="chat_by_category"),
    path("chats/chat/<int:page>/", chat_ditail, name="chat_ditail"),
    path('chats/', cache_page(6000)(HomeChatsView.as_view()), name="chats"),
    path("bots/bot/<int:page>/", bot_ditail, name='bot_ditail'),
    path("bots/", cache_page(6000)(HomeBotsView.as_view()), name='bots'),
    path("article/<int:page>/", article_ditail, name='article_ditail'),
    path("articles/", cache_page(6000)(HomeArticlesView.as_view()), name='articles'),
    path("update_count/", update_count),
]
