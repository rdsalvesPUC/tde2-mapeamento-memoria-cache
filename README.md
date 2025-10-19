# TDE2 — Mapeamento de Memória Cache

> Trabalho em grupo (até 4 pessoas): pesquisar e explicar em vídeo (até 10 min) os algoritmos **FIFO, LRU e MRU** de substituição de páginas.  
> Implementação em linguagem de preferência **(sem uso de IA)**. Variáveis e comentários **em português**.

## 📑 Índice

1. [Objetivo](#objetivo)
2. [Integrantes](#integrantes)
3. [Escopo e Requisitos](#escopo-e-requisitos)
4. [Conceitos e Políticas de Substituição](#conceitos-e-políticas-de-substituição)
    - [FIFO](#fifo)
    - [LRU](#lru)
    - [MRU](#mru)
5. [Metodologia e Implementação](#metodologia-e-implementação)
    - [Regras comuns](#regras-comuns)
    - [Estruturas de dados sugeridas](#estruturas-de-dados-sugeridas)
    - [Diretórios de entrega](#diretórios-de-entrega)
6. [Como testar (8 quadros)](#como-testar-8-quadros)
    - [Sequência A](#sequência-a)
    - [Sequência B](#sequência-b)
    - [Sequência C](#sequência-c)
7. [Resultados e Respostas](#resultados-e-respostas)
8. [Discussão: Qual a melhor política?](#discussão-qual-a-melhor-política)
9. [Roteiro do Vídeo (até 10 min)](#roteiro-do-vídeo-até-10-min)
10. [Conformidade e Observações do Professor](#conformidade-e-observações-do-professor)
11. [Licença](#licença)

---

## Objetivo

Demonstrar, comparar e explicar as políticas **FIFO**, **LRU** e **MRU** de substituição de páginas em memória cache, avaliando **page faults** e o **quadro final** de cada sequência de acesso, com **8 quadros**.

## Integrantes

-   Rodrigo da Silva Alves
-   Richard Mickael
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

## Metodologia e Implementação

### Regras comuns

-   **Acerto (hit)**: página já está na memória → **não há page fault**.
-   **Falta (fault)**: página não está na memória → **carrega** a página; se a memória estiver cheia, **remove** conforme a política.
-   **8 quadros** (índices 0..7 ou 1..8, defina padrão e mantenha).

### Estruturas de dados sugeridas

_(Sugestão, não código pronto; escolha a que dominar na sua linguagem):_

-   **FIFO**: fila/índice circular para o “próximo a sair”.
-   **LRU**: lista atualizada a cada acesso (move para “mais recente”) **ou** mapa com “timestamp” de último uso.
-   **MRU**: igual ao LRU para rastrear ordem, mas remove o **mais recente**.

> **Dica de implementação manual**: mantenha, junto aos quadros, um **registro de uso** (contador crescente ou “posição de recência”). Em **LRU**, remove o **menor**; em **MRU**, remove o **maior**.

### Diretórios de entrega
