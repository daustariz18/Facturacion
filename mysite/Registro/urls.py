from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListClienteAPIView.as_view(), name='cliente_list'),
    path('create/', views.CreateClienteAPIView.as_view(),
         name='cliente_create'),
    path('update/<int:pk>/', views.UpdateClienteAPIview.as_view(),
         name='cliente_update'),
]
