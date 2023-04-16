from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('networkx/', views.networkx_view, name='networkx'),
    path('plotly/', views.plotly_view, name='plotly'),
    path('graphviz/', views.graphviz_view, name='graphviz'),
]
