from rest_framework import serializers
from livraria_app.models import Cliente, Compra, Livro, Autor

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ('nome', 'titulo', 'autor', 'genero', 'edicao', 'editora', 'preco_venda', 'preco_compra')

    def create(self, validated_data):
        author_id = validated_data.pop('autor')
        author = Autor.objects.get(pk=author_id)
        livro = Livro.objects.create(author=author, **validated_data)
        return livro



class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'