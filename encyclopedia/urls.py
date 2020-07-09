from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("newpage", views.new_page, name="newpage"),
    path("savepage", views.save_page, name="savepage")
]
