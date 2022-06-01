from django.db import models
from decimal import Decimal
# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return "Cliente " + self.nome

    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }

    @staticmethod
    def from_json(json):
        return Cliente(
            nome=json['nome'],
            email=json['email']
        )


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return "Autor " + self.nome

    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }

    @staticmethod
    def from_json(json):
        return Autor(
            nome=json['nome'],
            email=json['email']
        )


class Produto(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return "Produto " + self.nome


class Livro(Produto):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.CharField(max_length=100)
    edicao = models.IntegerField()
    editora = models.CharField(max_length=100)
    preco_venda = models.DecimalField(max_digits=6, decimal_places=2)
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.titulo

    def calcular_imposto(self):
        return Tax_Provider.calcular_imposto(self.genero, self.preco_venda, self.preco_compra)

    def to_json(self):
        imposto = self.calcular_imposto()
        return {
            'id': self.id,
            'titulo': self.nome,
            'autor': self.autor.nome,
            'genero': self.genero,
            'edicao': self.edicao,
            'editora': self.editora,
            'preco_venda': self.preco_venda,
            'preco_compra': self.preco_compra,
            'imposto': imposto
        }

    @staticmethod
    def from_json(json):
        return Livro(
            nome=json['nome'],
            titulo=json['titulo'],
            autor=Autor.objects.get(pk=json['autor']),
            genero=json['genero'],
            edicao=json['edicao'],
            editora=json['editora'],
            preco_venda=json['preco_venda'],
            preco_compra=json['preco_compra']
        )


class Tax_Provider:
    def calcular_imposto(genero, preco_venda, preco_compra):
        """
        O cálculo de imposto pode ser facilmente modificado
        """
        return (preco_venda-preco_compra) * Decimal(0.05)


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def from_json(json):
        return Compra(
            cliente=Cliente.objects.get(pk=json['cliente'])

        )

    def to_json(self):
        items = Item.objects.filter(compra=self)
        item_list = [item.to_json() for item in items]
        return {
            'id': self.id,
            'cliente': self.cliente.id,
            'items': item_list
        }


class Item(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    produto = models.ForeignKey(Livro, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.livro.titulo + " - " + str(self.quantidade)

    @staticmethod
    def from_json(json, compra_id):
        return Item(
            compra=Compra.objects.get(pk=compra_id),
            produto=Livro.objects.get(pk=json['produto_id']),
            quantidade=json['quantidade'],
            preco_unitario=json['preco_unitario']
        )

    def to_json(self):
        return {
            'id': self.id,
            'compra_id': self.compra.id,
            'produto_id': self.produto.id,
            'quantidade': self.quantidade,
            'preco_unitario': self.preco_unitario
        }
