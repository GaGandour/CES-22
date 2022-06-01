from ..models import *
from . import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

# Create your views here.


class ClientViewSet(ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = Cliente.objects.all()

    def list_all_clients(self, request):
        clientes = Cliente.objects.all()
        clientes_json = [cliente.to_json() for cliente in clientes]
        return Response(clientes_json)

    def show_single_client(self, request, pk=None):
        clientes = Cliente.objects.filter(pk=pk)
        if clientes:
            return Response(clientes[0].to_json())
        else:
            return Response(status=404)

    def post_new_client(self, request):
        cliente = Cliente.from_json(request.data)
        cliente.save()
        return Response(cliente.to_json())

    def modify_single_client(self, request, pk=None):
        clientes = Cliente.objects.filter(pk=pk)
        if clientes:
            cliente = clientes[0]
        else:
            return Response(status=404)
        nome = request.data.get('nome')
        email = request.data.get('email')
        if nome:
            cliente.nome = nome
        if email:
            cliente.email = email
        cliente.save()
        return Response(cliente.to_json())


    def delete_single_client(self, request, pk=None):
        """
        deleta um cliente
        """
        cliente = Cliente.objects.filter(pk=pk)
        if cliente:
            cliente.delete()
            response = dict()
            response = {'status': 'ok'}
            return Response(response)
        else:
            return Response(status=404)


class AuthorViewSet(ModelViewSet):
    serializer_class = serializers.AutorSerializer
    queryset = Autor.objects.all()

    def list_all_authors(self, request):
        autores = Autor.objects.all()
        autores_json = [autor.to_json() for autor in autores]
        return Response(autores_json)

    def show_single_author(self, request, pk=None):
        autores = Autor.objects.filter(pk=pk)
        if autores:
            return Response(autores[0].to_json())
        else:
            return Response(status=404)

    def post_new_author(self, request):
        autor = Autor.from_json(request.data)
        autor.save()
        return Response(autor.to_json())

    def modify_single_author(self, request, pk=None):
        autores = Autor.objects.filter(pk=pk)
        if autores:
            autor = autores[0]
        else:
            return Response(status=404)
        nome = request.data.get('nome')
        email = request.data.get('email')
        if nome:
            autor.nome = nome
        if email:
            autor.email = email
        autor.save()
        return Response(autor.to_json())

    def delete_single_author(self, request, pk=None):
        """
        deleta um autor
        """
        autores = Autor.objects.filter(pk=pk)
        if autores:
            autor = autores[0]
            autor.delete()
            response = dict()
            response = {'status': 'ok'}
            return Response(response)
        else:
            return Response(status=404)


class BookViewSet(ModelViewSet):
    serializer_class = serializers.LivroSerializer
    queryset = Livro.objects.all()

    def list_all_books(self, request):
        livros = Livro.objects.all()
        livros_json = [livro.to_json() for livro in livros]
        return Response(livros_json)

    def show_single_book(self, request, pk=None):
        livros = Livro.objects.filter(pk=pk)
        if livros:
            return Response(livros[0].to_json())
        else:
            return Response(status=404)

    def post_new_book(self, request):
        livro = Livro.from_json(request.data)
        livro.save()
        return Response(livro.to_json())

    def modify_single_book(self, request, pk=None):
        livros = Livro.objects.filter(pk=pk)
        if livros:
            livro = livros[0]
        else:
            return Response(status=404)
        nome = request.data.get('nome')
        if nome:
            livro.nome = nome

        titulo = request.data.get('titulo')
        if titulo:
            livro.titulo = titulo

        autor = request.data.get('autor')
        if autor:
            livro.autor = autor

        genero = request.data.get('genero')
        if genero:
            livro.genero = genero

        edicao = request.data.get('edicao')
        if edicao:
            livro.edicao = edicao

        editora = request.data.get('editora')
        if editora:
            livro.editora = editora

        preco_venda = request.data.get('preco_venda')
        if preco_venda:
            livro.preco_venda = preco_venda

        preco_compra = request.data.get('preco_compra')
        if preco_compra:
            livro.preco_compra = preco_compra
        livro.save()
        return Response(livro.to_json())


    def delete_single_book(self, request, pk=None):
        """
        deleta um livro
        """
        livros = Livro.objects.filter(pk=pk)
        if livros:
            livro = livros[0]
            livro.delete()
            response = dict()
            response = {'status': 'ok'}
            return Response(response)
        else:
            return Response(status=404)


class PurchaseViewSet(ModelViewSet):
    serializer_class = serializers.CompraSerializer
    queryset = Compra.objects.all()

    def list_all_purchases(self, request):
        compras = Compra.objects.all()
        compras_json = [compra.to_json() for compra in compras]
        return Response(compras_json)

    def show_single_purchase(self, request, pk=None):
        compras = Compra.objects.filter(pk=pk)
        if compras:
            return Response(compras[0].to_json())
        else:
            return Response(status=404)

    def post_new_purchase(self, request):
        compra = Compra.from_json(request.data)
        compra.save()
        compra_id = compra.id
        items = request.data.get('items')
        if items:
            for item in items:
                elem = Item.from_json(item, compra_id)
                elem.save()
        
        return Response(compra.to_json())


    def modify_single_purchase(self, request, pk=None):
        compras = Compra.objects.filter(pk=pk)
        if not compras:
            return Response(status=404)
        
        compra = compras[0]
        client_id = request.data.get('cliente_id')
        itens = request.data.get('itens')
        if client_id:
            clientes = Cliente.objects.filter(pk=client_id)
            if clientes:
                compra.cliente = clientes[0]
        if itens:
            current_items = Item.objects.all()
            for item in current_items:
                item.delete()
            for item in itens:
                elem = Item.from_json(item, compra.id)
                elem.save()
        compra.save()
        return Response(compra.to_json())

    def delete_single_purchase(self, request, pk=None):
        """
        deleta um compra
        """
        compras = Compra.objects.filter(pk=pk)
        if compras:
            compra = compras[0]
            compra.delete()
            response = dict()
            response = {'status': 'ok'}
            return Response(response)
        else:
            return Response(status=404)