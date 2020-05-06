from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="game-index"),
    path('<int:id>', views.get_game_by_id, name="game_details"),
]
