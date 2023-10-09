from typing import Dict, Any

from django import template
from django.core.exceptions import ObjectDoesNotExist

from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        # Получаем меню и его элементы с одним запросом к БД
        menu = MenuItem.objects.filter(menu__title=menu_name).select_related('menu', 'parent')
        menu_items = {item.id: item for item in menu}

        # Определяем ID выбранного элемента меню из параметров запроса
        selected_item_id = int(context['request'].GET.get(menu_name, menu.first().id))
        selected_item = menu_items.get(selected_item_id)

        # Получаем список ID выбранных элементов меню
        selected_item_id_list = get_selected_item_id_list(selected_item, menu_items, selected_item_id)

        # Добавляем дочерние элементы для каждого выбранного элемента меню
        items = get_child_items(menu_items, selected_item_id_list)

        # Исключаем выбранный элемент из списка верхнего уровня
        top_level_items = [item for item in items if not item.parent_id]

        result_dict = {'items': top_level_items}

    except (KeyError, ObjectDoesNotExist):
        # В случае ошибки, возвращаем список элементов меню без родительских элементов
        items = [item for item in menu_items.values() if not item.parent]
        result_dict = {'items': items}

    # Добавляем имя меню и дополнительные параметры строки запроса в result_dict
    result_dict['menu'] = menu_name
    result_dict['other_querystring'] = build_querystring(context, menu_name)

    return result_dict


def build_querystring(context, menu_name):
    # Инициализируем список для аргументов строки запроса
    querystring_args = []

    # Перебираем все параметры текущего запроса
    for key in context['request'].GET:
        # Если ключ текущего параметра не соответствует переданному параметру 'menu'
        if key != menu_name:
            # Добавляем пару "ключ=значение" в список аргументов строки запроса
            querystring_args.append(f"{key}={context['request'].GET[key]}")

    # Объединяем аргументы из списка в одну строку запроса, разделяя символом '&'
    querystring = '&'.join(querystring_args)

    # Возвращаем построенную строку запроса
    return querystring


def get_child_items(menu_items, selected_item_id_list):
    # Возвращаем список дочерних элементов для выбранных элементов меню

    child_items = []

    for item_id in selected_item_id_list:
        item = menu_items[item_id]
        if item:
            item.child_items = [child for child in menu_items.values() if child.parent_id == item_id]
            child_items.append(item)

    return child_items


def get_selected_item_id_list(selected_item, menu_items, selected_item_id):
    # Возвращаем список ID выбранных элементов меню, начиная с выбранного элемента

    selected_item_id_list = []

    while selected_item:
        selected_item_id_list.append(selected_item.id)
        selected_item = menu_items.get(selected_item.parent_id)

    return selected_item_id_list