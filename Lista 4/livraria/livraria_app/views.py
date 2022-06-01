from .models import *
import livraria_app.api.viewsets as viewsets

# Create your views here.

SingleClientView = viewsets.ClientViewSet.as_view({
    'put': 'modify_single_client',
    'delete': 'delete_single_client',
    'get': 'show_single_client',
})

ClientView = viewsets.ClientViewSet.as_view({
    'get': 'list_all_clients',
    'post': 'post_new_client'
})

SingleAuthorView = viewsets.AuthorViewSet.as_view({
    'put': 'modify_single_author',
    'delete': 'delete_single_author',
    'get': 'show_single_author',
})

AuthorView = viewsets.AuthorViewSet.as_view({
    'get': 'list_all_authors',
    'post': 'post_new_author'
})

SingleBookView = viewsets.BookViewSet.as_view({
    'put': 'modify_single_book',
    'delete': 'delete_single_book',
    'get': 'show_single_book',
})

BookView = viewsets.BookViewSet.as_view({
    'get': 'list_all_books',
    'post': 'post_new_book'
})

SinglePurchaseView = viewsets.PurchaseViewSet.as_view({
    'put': 'modify_single_purchase',    
    'delete': 'delete_single_purchase',
    'get': 'show_single_purchase',
})

PurchaseView = viewsets.PurchaseViewSet.as_view({
    'get': 'list_all_purchases',
    'post': 'post_new_purchase'
})