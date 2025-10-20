# TDE2 — Mapeamento de Memória Cache

> Trabalho em grupo (até 4 pessoas): pesquisar e explicar em vídeo (até 10 min) os algoritmos **FIFO, LRU e MRU** de substituição de páginas.

> **Link do Vídeo:** https://youtu.be/WsOhkRPPsTE

## 📑 Índice

1. [Objetivo](#objetivo)
2. [Integrantes](#integrantes)
3. [Escopo e Requisitos](#escopo-e-requisitos)
4. [Conceitos e Políticas de Substituição](#conceitos-e-políticas-de-substituição)
    - [FIFO](#fifo)
    - [LRU](#lru)
    - [MRU](#mru)
5. [Diretórios de entrega](#diretórios-de-entrega)
6. [Sequência A](#sequência-a)
7. [Sequência B](#sequência-b)
8. [Sequência C](#sequência-c)
9. [Discussão: Qual a melhor política?](#discussão-qual-a-melhor-política)

---

## Objetivo

Demonstrar, comparar e explicar as políticas **FIFO**, **LRU** e **MRU** de substituição de páginas em memória cache, avaliando **page faults** e o **quadro final** de cada sequência de acesso, com **8 quadros**.

## Integrantes

-   Rodrigo da Silva Alves
-   Richard Mickaell
-   Marco Alija Ramos
-   Lucas Bruno

## Escopo e Requisitos

-   Implementar **FIFO, LRU e MRU**.
-   Testar com **8 quadros** e as sequências fornecidas.
-   Responder:
    -   **A)** Em qual quadro estará a **página 7**?
    -   **B)** Em qual quadro estará a **página 11**?
    -   **C)** Em qual quadro estará a **página 11**?

---

## Conceitos e Políticas de Substituição

### FIFO

**First-In, First-Out**: remove a página que **está há mais tempo** na memória (ordem de chegada).  
**Intuição**: fila simples; não considera recência de uso.

### LRU

**Least Recently Used**: remove a página **menos recentemente usada**.  
**Intuição**: se não uso há muito, é menos provável que eu precise agora (localidade temporal).

### MRU

**Most Recently Used**: remove a página **mais recentemente usada**.  
**Intuição**: em certos padrões sequenciais, a página recém-usada é a **menos provável** de ser reutilizada imediatamente.

---

### Diretórios de entrega

/com_comentarios/
/sem_comentarios/

### Sequência A

> 4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7

**Pergunta A**: Em qual quadro na memória possuirá a **página 7**?

-   **FIFO**: página **7** no **quadro → 5**
-   **LRU**: página **7** no **quadro → 6**
-   **MRU**: página **7** no **quadro → 3**

---

### Sequência B

> 4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11

**Pergunta B**: Em qual quadro na memória possuirá a **página 11**?

-   **FIFO**: página **11** no **quadro → 6**
-   **LRU**: página **11** no **quadro → 3**
-   **MRU**: página **11** no **quadro → 7**

---

### Sequência C

> 4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11

**Pergunta C**: Em qual quadro na memória possuirá a **página 11**?

-   **FIFO**: página **11** no **quadro → 5**
-   **LRU**: página **11** no **quadro → 6**
-   **MRU**: página **11** no **quadro → 8**

---

## Discussão: Qual a melhor política?

> Se o critério de melhor, for a menor quantidade de **Page Fault**, então tivemos o seguinte resultado:

-   **FIFO**: Page Fault em cada sequência **A)** 13 - **B)** 14 - **C)** 13
-   **LRU**: Page Fault em cada sequência **A)** 12 - **B)** 16 - **C)** 11
-   **MRU**: Page Fault em cada sequência **A)** 11 - **B)** 14 - **C)** 12

> Conclusão: **MRU** se saiu melhor com esses 3 conjuntos de dados..
