from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('networkx/', views.networkx_view, name='networkx'),
    path('plotly/', views.plotly_view, name='plotly'),
    path('graphviz/', views.graphviz_view, name='graphviz'),
    path('d3/', views.d3_view, name='d3'),
    path('ete3/', views.ete3_view, name='ete3'),

]
