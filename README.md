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
