# Django Tree Menu

# Описание проекта

Проект представляет собой веб-приложение, основанное на фреймворке Django, которое реализует систему древовидного меню с следующей функциональностью:

1. **Создание Меню**: Пользователи могут создавать различные меню и заполнять их элементами через стандартную административную панель Django.

2. **Древовидная Структура**: Меню построено как древовидная структура, где каждый элемент меню может иметь дочерние элементы, что позволяет создавать иерархию меню.

3. **Подсветка Активного Пункта Меню**: Активный пункт меню подсвечивается на основе текущего URL страницы, обеспечивая навигацию по сайту.

4. **Использование Шаблонных Тегов**: Для включения меню в разные части сайта используется шаблонный тег Django.

5. **Множество Меню на Одной Странице**: Поддерживается отображение нескольких меню на одной странице, и каждое меню идентифицируется по имени.

6. **Настройка URL и Именованных URL**: Меню может быть настроено с использованием явных URL-адресов или ссылок на именованные URL в Django.

7. **Оптимизация БД**: Для минимизации запросов к базе данных используются методы `select_related`, что позволяет эффективно загружать связанные данные.

8. **Эффективная Отрисовка Меню**: Для каждого меню требуется только 1 запрос к базе данных при его отрисовке.

9. **Удобный Интерфейс Для Пользователей**: Пользователи могут видеть и навигироваться по древовидным меню, которое динамически адаптируется под текущий контекст страницы.

В итоге, проект предоставляет гибкую и производительную систему управления древовидными меню на веб-сайте, что делает навигацию пользователя более удобной и эффективной.


## Задача

Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.

## Библиотеки

1. [Django](https://docs.djangoproject.com/en/4.2/)
2. [Python стандартная библиотека](https://www.python.org/)

## Инструкции по запуску

1. Клонируйте репозиторий на ваш компьютер:

   ```bash
   git clone https://github.com/Tap1x1/TreeMenuTestTask
    ```
2. Установите зависимости, используя `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3. Выполните миграции: 

    ```python
    python manage.py migrate
    ```
4. Запустите сервер: 
   ```python
    python manage.py runserver
   ```
7. Создайте суперпользователя БД: 
    ```python
    python manage.py createsuperuser
    ```
8. Создайте меню, для этого необходимо войти в административную панель.
9. Для перехода в административную панель http://127.0.0.1:8000/admin/
10. Для перехода в меню http://127.0.0.1:8000/tree_menu/


## Лицензия
MIT License

