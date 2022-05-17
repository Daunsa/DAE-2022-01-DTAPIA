from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('productos',views.ProductosView.as_view(),name='productos'),
    path('producto/<int:producto_id>',views.ProductoDetailView.as_view())
]
