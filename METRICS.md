# Métricas de Qualidade — REFactor Race Python

## Baseline — Antes da refatoração

| Indicador | Antes |
|---|---|
| Testes aprovados | 4 |
| Total de testes | 4 |
| Cobertura de testes | 85% |
| Complexidade de `process_order` | D (24) |
| Complexidade média | C (10,67) |
| Índice de manutenibilidade | 52,10 |
| Problemas reportados pelo Ruff | 0 |
| Quantidade de testes | 4 |

## Métricas após a refatoração

| Indicador | Depois |
|---|---|
| Testes aprovados | 4 |
| Total de testes | 4 |
| Cobertura de testes | 91% |
| Complexidade de `process_order` | A (1) |
| Complexidade média | A (4,0) |
| Índice de manutenibilidade | 58,34 |
| Problemas reportados pelo Ruff | 0 |
| Quantidade de testes | 4 |

## Análise dos resultados

A comparação das métricas indica melhorias na qualidade do código após a refatoração.

- **Testes:** os quatro testes automatizados continuaram passando.
- **Cobertura:** aumentou de 85% para 91%.
- **Complexidade de `process_order`:** passou de D (24) para A (1).
- **Complexidade média:** passou de C (10,67) para A (4,0).
- **Manutenibilidade:** aumentou de 52,10 para 58,34.
- **Ruff:** permaneceu sem problemas reportados.

As mudanças reduziram a complexidade da função principal e melhoraram a organização e a manutenibilidade do código.