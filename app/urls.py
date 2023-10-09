from django.urls import path

from .views import IndexPageView

urlpatterns = [
    path('tree_menu/', IndexPageView.as_view(), name='index')
]
