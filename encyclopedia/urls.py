from django.urls import path, include


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<str:title>/', views.pages, name="pages"),
    path("search", views.search, name="search"),
    path("newpage", views.newpage, name="newpage")
]
