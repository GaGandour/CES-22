from django.urls import path

from . import views

urlpatterns = [
    path('cliente/', views.ClientView, name='cliente'),
    path('cliente/<int:pk>/', views.SingleClientView, name='cliente'),
    path('autor/', views.AuthorView, name='autor'),
    path('autor/<int:pk>/', views.SingleAuthorView, name='autor'),
    path('livro/', views.BookView, name='livro'),
    path('livro/<int:pk>/', views.SingleBookView, name='livro'),
    path('compra/', views.PurchaseView, name='compra'),
    path('compra/<int:pk>/', views.SinglePurchaseView, name='compra'),
]