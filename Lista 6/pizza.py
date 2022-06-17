class PizzaComponent:
    def getDescription(self):
        return self.__class__.__name__

    def getTotalcusto(self):
        return self.__class__.custo


class Prato(PizzaComponent):
    custo = 0.0


class Decorator(PizzaComponent):
    def __init__(self, pizza_component):
        self.component = pizza_component

    def getTotalCost(self):
        return self.component.getTotalcusto() + PizzaComponent.getTotalcusto(self)

    def getDescription(self):
        return self.component.getDescription() + " " +PizzaComponent.getDescription(self)


class Queijo(Decorator):
    custo = 0.45

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Presunto(Decorator):
    custo = 0.30

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Frango(Decorator):
    custo = 0.40

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Azeitona(Decorator):
    custo = 0.20

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Molho(Decorator):
    custo = 0.10

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Goiabada(Decorator):
    custo = 0.25

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Catupiry(Decorator):
    custo = 0.10

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


print("Criando pizza de frango com catupiry:\n")
frango_com_catupiry = Catupiry(Frango(Queijo(Prato())))
print(frango_com_catupiry.getDescription()+ ": $" + str(frango_com_catupiry.getTotalCost()))

print("\n--------------------------------------------\n")

print("Criando pizza de Romeu e Julieta:\n")
romeu_e_julieta = Goiabada(Queijo(Prato()))
print(romeu_e_julieta.getDescription()+ ": $" + str(romeu_e_julieta.getTotalCost()))