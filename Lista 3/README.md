# Lista de Exercícios 3 - Explicação

## Primeira questão (arquivo `question1.py`)

Nesse arquivo, temos uma classe `Materia` que representa uma matéria do ITA que foi lecionada para uma determinada turma. Temos também três subclasses `CES10`, `CES12` e `CES22`. Podemos cada classe possui um método abstrato (`descricao()`), um estático (`apresenta()`) e um de instância (`muda_professor()`).

No final do código, cada uma dessas funções são chamadas. Perceba que há um erro no final do código. Isso é proposital e acontece porque o método abstrato `descricao()` foi intencionalmente deixado de ser implementado na classe `CES10`. Assim, o _Python_ não permite que a classe `CES10` seja instanciada. O output esperado é mostrado abaixo. 

    Sou uma materia do ITA!

    Nome: Algoritmos e Estruturas de Dados
    Sigla: CES12
    Carga Horeria: 5 creditos
    ---------------------------------
    Sou uma materia do ITA!

    Nome: Programacao Orientada a Objetos
    Sigla: CES22
    Carga Horeria: 4 creditos
    ---------------------------------
    Em CES12, voce vai aprender a implementar ervores rubro-negras com o professor Alonso!

    ---------------------------------
    Em CES22, voce vai aprender a programar em Python com o professor Yano!

    Em CES22, voce vai aprender a programar em Python com o professor Karla!
    Traceback (most recent call last):
    File "d:\ITA - 2022.1\CES-22\Lista 3\question1.py", line 80, in <module>

        ces10 = CES10("Armando", "24")
    TypeError: Can't instantiate abstract class CES10 with abstract method descricao