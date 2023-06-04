from time import sleep

from django.http import HttpResponse
from rest_framework.views import APIView
from index_page.models import channels
from index_page.models import chats
from index_page.models import bots
from index_page.models import categories
from transliterate import translit


class index_api(APIView):

    def get(self, request):
        try:
            type_req = request.POST.get("type_request")
            if type_req == "add_channel":
                name = request.POST.get("name")
                description = request.POST.get("des")
                category = request.POST.get("category")
                #categories.objects.get(name_categories=request.POST.get("category")).pk
                image = request.POST.get("image")
                link_tg = request.POST.get("link_tg")
                subscribers_count = request.POST.get("subscribers_count")

                channel_exists = channels.objects.filter(link_tg=link_tg).exists()
                category_exists = categories.objects.filter(name_categories=category)
                if not category_exists:
                    categ = categories.objects.create(
                            name_categories=category,
                            translit_category=translit(category, 'ru', reversed=True).replace(" ", "-"),
                            count=1
                        )

                else:
                    cat = categories.objects.get(name_categories=category)
                    cat.count +=1
                    cat.save()


                if channel_exists:
                    channel = channels.objects.get(link_tg=link_tg)
                    channel.name = name
                    channel.description = description
                    channel.category_id = categories.objects.get(name_categories=category).pk
                    channel.image = image
                    channel.link_tg = link_tg
                    channel.subscribers_count = subscribers_count
                    channel.save()
                else:
                    channel = channels.objects.create(
                        name=name,
                        description=description,
                        category_id=categories.objects.get(name_categories=category).pk,
                        image=image,
                        link_tg=link_tg,
                        subscribers_count=subscribers_count
                    )


                return HttpResponse(str({"status": "ok", "message": "Канал добавлен!"}))
        #     elif type_req == "add_bot":
        #         name = request.POST.get("name")
        #         description = request.POST.get("des")
        #         # category = categories.objects.get(name_categories=request.POST.get("category")).pk
        #         image = request.POST.get("image")
        #         link_tg = request.POST.get("link_tg")
        #
        #         bot_exists = bots.objects.filter(name=name).exists()
        #         # category_exists = categories.objects.filter(name_categories=category)
        #         #
        #         # if not category_exists:
        #         #     categ = categories.objects.create(
        #         #             name_categories=category,
        #         #             translit_category=translit(category, 'ru', reversed=True).replace(" ", "-"),
        #         #             count=1
        #         #         )
        #         # else:
        #         #     cat = categories.objects.get(name_categories=category)
        #         #     cat.count +=1
        #         #     cat.save()
        #
        #         if bot_exists:
        #             bot = bots.objects.get(name=name)
        #             bot.name = name
        #             bot.description = description
        #             bot.category = category
        #             bot.image = image
        #             bot.link_tg = link_tg
        #             bot.save()
        #         else:
        #             bot = bots.objects.create(
        #                 name=name,
        #                 description=description,
        #                 category=category,
        #                 image=image,
        #                 link_tg=link_tg
        #             )
        #         return HttpResponse(str({"status": "ok", "message": "Бот добавлен!"}))
        #     elif type_req == "add_chat":
        #         name = request.POST.get("name")
        #         description = request.POST.get("des")
        #         category = categories.objects.get(name_categories=request.POST.get("category")).pk
        #         image = request.POST.get("image")
        #         link_tg = request.POST.get("link_tg")
        #         subscribers_count = request.POST.get("subscribers_count")
        #
        #         chat_exists = chats.objects.filter(name=name).exists()
        #         category_exists = categories.objects.filter(name_categories=category)
        #
        #         if not category_exists:
        #             categ = categories.objects.create(
        #                     name_categories=category,
        #                     translit_category=translit(category, 'ru', reversed=True).replace(" ", "-"),
        #                     count=1
        #                 )
        #         else:
        #             cat = categories.objects.get(name_categories=category)
        #             cat.count +=1
        #             cat.save()
        #
        #         if chat_exists:
        #             chat = chats.objects.get(name=name)
        #             chat.name = name
        #             chat.description = description
        #             chat.category = category
        #             chat.image = image
        #             chat.link_tg = link_tg
        #             chat.subscribers_count = subscribers_count
        #             chat.save()
        #         else:
        #             chat = chats.objects.create(
        #                 name=name,
        #                 description=description,
        #                 category=category,
        #                 image=image,
        #                 link_tg=link_tg,
        #                 subscribers_count=subscribers_count
        #             )
        #
        #         return HttpResponse(str({"status": "ok", "message": "Чат добавлен!"}))
        #
        #     else:
        #         return HttpResponse(str({"error": "Invalid type request"}))
        except Exception as err:
            return HttpResponse(str({"error": err}))
