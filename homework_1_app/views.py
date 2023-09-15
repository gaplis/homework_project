from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def main_page(request):
    html = '<h1>Главная</h1><br>' \
           '<p>Это главная страница моего сайта, созданная в рамках домашнего задания по курсу "Фреймворк Django"</p>'
    logger.info('Visited home page')
    return HttpResponse(html)


def about_page(request):
    html = '<h1>Обо мне</h1><br>' \
           '<p>Имя: Илья Чистов</p>' \
           '<p>Контакты: @gaplis</p>'
    logger.info('Visited the page "About me"')
    return HttpResponse(html)
