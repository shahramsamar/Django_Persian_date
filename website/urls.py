from django.urls import path
from website import views


urlpatterns = [
    path('', views.index_views, name='index' ),
    path('templatetags/', views.index_templatetags, name='index_templatetags' ),

]
