from django.urls import path
from . import views

urlpatterns = [
  path('', views.trees_list),
  path('/<int:show>/', views.tree_show)
]