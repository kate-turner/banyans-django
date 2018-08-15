from django.urls import path
from . import views

urlpatterns = [
  path('', views.trees_list),
  path('trees/<int:id>/', views.tree_detail, name='tree_detail')
]