from django.urls import path
from .views import index, articles

urlpatterns = [
    path("", index, name="index"),
    path("<str:full_name>/", articles, name="article")
]
