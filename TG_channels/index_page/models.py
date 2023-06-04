from django.db import models
from django.urls import reverse


class categories(models.Model):

    name_categories = models.CharField(max_length=255)
    translit_category = models.CharField(max_length=255, default=None)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name_categories
    def get_absolute_url(self):
        return reverse("channel_by_category", kwargs={"category": self.translit_category})

class category_for_chats(models.Model):
    name_categories = models.CharField(max_length=255)
    translit_category = models.CharField(max_length=255, default=None)
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.name_categories
    def get_absolute_url(self):
        return reverse("chat_by_category", kwargs={"category": self.translit_category})
class channels(models.Model):

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("channel_ditail", kwargs={"page": self.pk})
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(categories, related_name='categories_channel', on_delete=models.SET_NULL,null=True)
    image = models.CharField(max_length=500)
    link_tg = models.CharField(max_length=500)
    subscribers_count = models.IntegerField()

class chats(models.Model):

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("chat_ditail", kwargs={"page": self.pk})
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(category_for_chats, related_name='categories_chat', on_delete=models.SET_NULL,null=True)
    image = models.CharField(max_length=500)
    link_tg = models.CharField(max_length=500)
    subscribers_count = models.IntegerField()

class bots(models.Model):

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("bot_ditail", kwargs={"page": self.pk})
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    link_tg = models.CharField(max_length=500)


class articles(models.Model):

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("article_ditail", kwargs={"page": self.pk})

    name = models.CharField(max_length=255)
    preview = models.CharField(max_length=500)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class paid_advertising(models.Model):

    def __str__(self):
        return self.name


    name = models.CharField(max_length=255)
    preview = models.CharField(max_length=500)
    text = models.TextField(max_length=300)
    link = models.CharField(max_length=255, default="")
    active = models.BooleanField()