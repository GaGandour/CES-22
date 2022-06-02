from django.db import models
from decimal import Decimal
from abc import abstractmethod
# Create your models here.


class Cliente(models.Model):
    """
    Um cliente possui um nome e um email.
    Um cliente pode possuir várias compras,
    que pode ter vários itens.
    """
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
    """
    Um autor possui um nome e um email e pode ter vários livros.
    """
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
    """
    Classe de produto
    """
    nome = models.CharField(max_length=100)
    preco_venda = models.DecimalField(max_digits=6, decimal_places=2)
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "Produto " + self.nome

    @abstractmethod
    def calcular_imposto(self):
        return 2


class Livro(Produto):
    """
    Um Livro é um Produto. Podem ser adicionados novos tipos de produtos posteriormente.
    """
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.CharField(max_length=100)
    edicao = models.IntegerField()
    editora = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

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

    def calcular_imposto(self):
        return Tax_Provider.calcular_imposto(self.genero, self.preco_venda, self.preco_compra)



class Tax_Provider:
    @staticmethod
    def calcular_imposto(genero, preco_venda, preco_compra):
        """
        O cálculo de imposto pode ser facilmente modificado
        """
        return (preco_venda-preco_compra) * Decimal(0.05)


class Compra(models.Model):
    """
    Uma compra possui um cliente e vários Itens
    """
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
            'nome do cliente': self.cliente.nome,
            'items': item_list
        }


class Item(models.Model):
    """
    Item geral, que pode abrigar qualquer tipo de produto.
    """
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.produto.nome + " - " + str(self.quantidade)

    @staticmethod
    def from_json(json, compra_id):
        produto = Produto.objects.get(pk=json['produto_id'])
        preco = produto.preco_venda
        return Item(
            compra=Compra.objects.get(pk=compra_id),
            produto=produto,
            quantidade=json['quantidade'],
            preco_unitario=preco
        )

    def to_json(self):
        return {
            'id': self.id,
            'compra_id': self.compra.id,
            'produto_id': self.produto.id,
            'nome do produto': self.produto.nome,
            'quantidade': self.quantidade,
            'preco_unitario': self.preco_unitario
        }
