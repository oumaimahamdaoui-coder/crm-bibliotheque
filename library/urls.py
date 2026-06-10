from django.urls import path
from . import views
from .views import export_pdf


urlpatterns = [
    path('', views.home, name='home'),
    path('add-livre/', views.add_livre, name='add_livre'),
    path('add-emprunt/', views.add_emprunt, name='add_emprunt'),
    path('export-pdf/' ,  export_pdf, name='export_pdf'),
]
