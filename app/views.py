from django.db import connection
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView

from app.models import Menu, MenuItem


class IndexPageView(TemplateView):
    """
        Вид главной страницы, отображающий древовидное меню.
    """
    template_name = "app/home.html"

    def get_context_data(self, **kwargs) -> dict:
        """
        Получить данные контекста для вида.

        :return: словарь данных контекста
        """
        context = super().get_context_data(**kwargs)
        menu_slug = 'main_menu'

        # Получаем меню и его элементы с одним запросом к базе данных
        menu = Menu.objects.filter(slug=menu_slug).first()
        menu_items = MenuItem.objects.filter(menu=menu).select_related('menu', 'parent')

        context['menu'] = menu
        context['menu_items'] = menu_items
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """
        Обработать GET-запрос для главной страницы.

        :param request: объект HttpRequest
        :return: объект HttpResponse
        """
        response = super().get(request, *args, **kwargs)

        # Check the number of database queries executed for debugging purposes
        print("Количество запросов к базе данных: ", len(connection.queries))

        return response
