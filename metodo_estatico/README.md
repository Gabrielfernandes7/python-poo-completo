# Métodos Estáticos

## Introdução aos Métodos Estáticos

Em Python, os métodos estáticos são definidos dentro de uma classe, mas não requerem acesso aos atributos de instância ou à própria instância. Eles são úteis quando você deseja definir uma função que está logicamente relacionada à classe, mas não precisa acessar ou modificar o estado dos objetos criados a partir dela.

## Exemplo de Criação de um Método Estático

```python
class Erro:
    @staticmethod
    def protocolo():
        print("Erro de protocolo")
```

Neste exemplo, `protocolo()` é um método estático da classe `Erro`. Ele pode ser chamado diretamente a partir da classe, sem a necessidade de criar uma instância da classe `Erro`. Por exemplo:

```python
Erro.protocolo()
```

## Quando Usar Métodos Estáticos?

Você pode precisar de um método estático em situações em que a lógica da função está relacionada à classe como um todo, mas não depende de instâncias específicas da classe. Alguns cenários comuns incluem:

- Funções de utilidade que estão relacionadas à classe, mas não precisam acessar ou modificar o estado dos objetos.
- Implementação de algoritmos independentes de estado, como funções de cálculo ou validação.
- Métodos que operam em argumentos passados explicitamente, sem acessar o estado interno da instância.

## Conclusão

Os métodos estáticos são uma ferramenta poderosa em Python para organizar e encapsular funcionalidades relacionadas a uma classe. Eles ajudam a melhorar a clareza e a coesão do código, garantindo que a lógica da função esteja logicamente associada à classe, mesmo quando não requer acesso aos atributos da instância.