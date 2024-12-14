from django.urls import path
from website import views


urlpatterns = [
    path('', views.index_views, name='index' ),
    path('temp/', views.index_temp, name='index_temp' ),

]
