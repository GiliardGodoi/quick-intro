# Decorators

Basicamente um decorator é uma função que recebe uma função e retorna uma função decorada, isto é, com uma funcionalidade adicionada.

```python
def decorator(func):

    def wrapper(*args, **kwargs):
        # do something before
        result = func(*args, **kwargs)

        # do somethin after

        return result

    return wrapper

@decorator
def concrete_func():
    # do your own stuff
    pass
```

Essa sintaxe é equivalente a

```python
concrete_func = decorator(concrete_func)
```

## Modelo mental alternativo para entendermos *decorators*

Podemos pensar o símbolo `@` como um operador que receberá a função que será utilizada para decorar a função que estamos decorando. Quando escrevemos:

```python
@decorator
def my_function(*args):
    # do something
    return False
```

Podemos pensar que a função `decorator` será atribuída a `@` e o símbolo `my_function` receberá o retorno de `@(my_function)`.

Esse modelo é útil quando queremos implementar decorators com parâmetros e os `decorators factories`.

## Decorators com parâmetros

## Classes que implementam decorators

## Referências

Mais detalhes ver ppgi-steiner-gpx-crossover.

**Real Python**. [Primer on Decorators](https://realpython.com/primer-on-python-decorators/#simple-decorators). Acessado em 15/06/2020. Disponível em <https://realpython.com/primer-on-python-decorators>
