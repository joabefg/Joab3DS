# Testes em Python: Do Assert ao UnitTest

## Público-alvo
Ensino Médio Técnico em Desenvolvimento de Software

## Carga Horária
10 horas (2 aulas de 5 horas)

## Metodologia

Esta sequência foi planejada para uma turma com baixo interesse na disciplina. O foco não será apresentar testes como uma obrigação da Engenharia de Software, mas como uma ferramenta para:

- Encontrar bugs
- Quebrar sistemas
- Ganhar desafios
- Descobrir erros escondidos
- Criar programas mais confiáveis

A maior parte da aula será prática, utilizando desafios, competição entre grupos e atividades gamificadas.

---

# Aula 1 – Caçadores de Bugs

## Duração: 5 horas

## Objetivos

Ao final da aula o aluno deverá ser capaz de:

- Compreender a importância dos testes
- Identificar casos de teste
- Utilizar o comando `assert`
- Criar testes simples para funções
- Encontrar erros em programas utilizando testes
- Entender a ideia básica do TDD

---

# Bloco 1 – O Código Perfeito Que Não Funciona

## Tempo

30 minutos

## Problema Inicial

Apresentar o código:

```python
idade = int(input("Idade: "))

if idade >= 18:
    print("Menor de idade")
else:
    print("Maior de idade")
```

### Pergunta

O programa está correto?

### Testes

Entrada:

```text
18
20
50
```

Resultado observado:

```text
Menor de idade
```

### Discussão

O código aparentemente funciona.

Porém:

- A lógica está errada
- O erro só foi encontrado porque testamos

### Conceito

> Não basta escrever código. É preciso provar que ele funciona.

---

# Bloco 2 – O Que é Um Teste?

## Tempo

40 minutos

### Exemplo

```python
def soma(a, b):
    return a + b
```

### Casos de Teste

```python
soma(2, 2)
```

Resultado esperado:

```text
4
```

---

```python
soma(-2, 2)
```

Resultado esperado:

```text
0
```

---

```python
soma(0, 0)
```

Resultado esperado:

```text
0
```

### Conceito

Caso de teste:

| Entrada | Saída Esperada |
|----------|----------|
| 2,2 | 4 |
| -2,2 | 0 |
| 0,0 | 0 |

---

# Bloco 3 – Introdução ao Assert

## Tempo

60 minutos

### Sintaxe

```python
assert condição
```

### Exemplo

```python
idade = 18

assert idade >= 18
```

Nenhum erro ocorre.

---

### Exemplo Falhando

```python
idade = 15

assert idade >= 18
```

Resultado:

```text
AssertionError
```

---

### Exemplo com Funções

```python
def dobro(numero):
    return numero * 2
```

Testes:

```python
assert dobro(2) == 4
assert dobro(5) == 10
assert dobro(0) == 0
```

---

# Atividade 1

## Tempo

30 minutos

Criar a função:

```python
def quadrado(numero):
    return numero ** 2
```

Criar pelo menos 5 testes usando assert.

Exemplo:

```python
assert quadrado(2) == 4
assert quadrado(3) == 9
```

---

# Intervalo

15 minutos

---

# Bloco 4 – Missão: Encontrar Bugs Escondidos

## Tempo

60 minutos

### Desafio 1

```python
def area_retangulo(base, altura):
    return base + altura
```

Objetivo:

Criar testes que provem que o programa está errado.

---

### Desafio 2

```python
def desconto(valor):
    return valor * 1.1
```

---

### Desafio 3

```python
def media(a, b, c):
    return a + b + c
```

---

## Competição

### Regras

Cada bug encontrado vale:

**1 ponto**

Equipe com mais pontos vence.

---

# Bloco 5 – Mini Projeto RPG

## Tempo

50 minutos

### Função Inicial

```python
def atacar(forca, arma):
    return forca + arma
```

### Testes

```python
assert atacar(10, 5) == 15
assert atacar(0, 5) == 5
assert atacar(10, 0) == 10
```

---

### Novas Funções

```python
def curar(vida, cura):
    pass

def dano(vida, golpe):
    pass
```

Criar implementação e testes.

---

# Introdução ao TDD

## Tempo

15 minutos

### Processo

1. Criar o teste
2. Executar o teste
3. Ver o teste falhar
4. Criar a função
5. Ver o teste passar

### Exemplo

Teste:

```python
assert multiplicar(2, 3) == 6
```

Função:

```python
def multiplicar(a, b):
    return a * b
```

---

# Encerramento

Pergunta para discussão:

> Você confia mais no seu código agora do que no início da aula?

---

# Aula 2 – Criando Robôs Testadores com UnitTest

## Duração

5 horas

## Objetivos

Ao final da aula o aluno deverá:

- Conhecer o módulo unittest
- Criar classes de teste
- Utilizar os principais métodos de validação
- Organizar testes de forma profissional
- Aplicar conceitos básicos de TDD

---

# Bloco 1 – Revisão Gamificada

## Tempo

30 minutos

### Quiz

O que acontece?

```python
assert 2 + 2 == 4
```

---

```python
assert 2 + 2 == 5
```

---

```python
assert True
```

---

### Pontuação

Cada resposta correta:

**1 ponto**

---

# Bloco 2 – Conhecendo o UnitTest

## Tempo

60 minutos

### Problema

Imagine:

```python
assert soma(2,2) == 4
assert soma(3,3) == 6
assert soma(5,5) == 10
```

Agora imagine:

- 100 testes
- 500 testes
- 1000 testes

Fica difícil organizar.

---

### Solução

```python
import unittest
```

---

### Primeiro Exemplo

```python
import unittest

def soma(a, b):
    return a + b

class TesteSoma(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(
            soma(2, 2),
            4
        )

unittest.main()
```

---

# Bloco 3 – Principais Métodos

## Tempo

60 minutos

### assertEqual

```python
self.assertEqual(2 + 2, 4)
```

---

### assertTrue

```python
self.assertTrue(10 > 5)
```

---

### assertFalse

```python
self.assertFalse(10 < 5)
```

---

### assertIn

```python
inventario = ["espada", "escudo"]

self.assertIn(
    "espada",
    inventario
)
```

---

# Atividade Prática

## Tempo

30 minutos

### Exercício 1

```python
def eh_par(numero):
    return numero % 2 == 0
```

Criar testes utilizando unittest.

---

### Exercício 2

```python
def login(usuario, senha):
    return usuario == "admin" and senha == "123"
```

Criar testes positivos e negativos.

---

# Intervalo

15 minutos

---

# Bloco 4 – Projeto Apocalipse Zumbi

## Tempo

80 minutos

### Objetivo

Criar um mini sistema de sobrevivência.

---

### Funções

```python
def encontrar_item():
    pass
```

---

```python
def lutar():
    pass
```

---

```python
def fugir():
    pass
```

---

```python
def usar_medicina():
    pass
```

---

## Organização

Equipe A:

- Desenvolve

Equipe B:

- Testa

Depois trocam.

---

## Desafio

Encontrar o maior número possível de bugs.

---

# Bloco 5 – Introdução ao TDD

## Tempo

50 minutos

### Etapa 1

Criar teste.

```python
self.assertEqual(
    multiplicar(2, 3),
    6
)
```

Executar.

Resultado:

```text
Falhou
```

---

### Etapa 2

Criar a função.

```python
def multiplicar(a, b):
    return a * b
```

Executar novamente.

Resultado:

```text
Passou
```

---

### Etapa 3

Adicionar novos testes.

```python
self.assertEqual(
    multiplicar(0, 5),
    0
)
```

---

### Conceito

TDD significa:

**Test Driven Development**

Ou seja:

> Desenvolvimento Orientado por Testes

---

# Projeto Final

## Tempo

20 minutos

Criar um jogo simples contendo:

- 3 funções
- 10 testes
- assertEqual
- assertTrue
- assertFalse
- assertIn

---

## Critérios de Avaliação

| Critério | Pontos |
|-----------|---------|
| Programa funciona | 3 |
| Possui testes | 3 |
| Todos os testes passam | 2 |
| Encontrou bugs de outro grupo | 2 |

Total:

**10 pontos**

---

# Fechamento Geral

## Mensagem Final

Testar não é apenas encontrar erros.

Testar é criar confiança.

Quando um programa cresce, torna-se impossível lembrar de tudo.

Os testes se tornam uma rede de segurança que ajuda o programador a modificar o código sem medo de quebrar funcionalidades que já funcionavam.

Programadores profissionais não confiam apenas nos próprios olhos.

Eles utilizam testes automatizados para garantir que seus programas continuem funcionando corretamente.