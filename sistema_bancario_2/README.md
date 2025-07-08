# Sistema Bancário v2

Este projeto é uma evolução do desafio bancário proposto na trilha Python da DIO. O arquivo principal é o `script_banco_v2.py`, que implementa um sistema bancário simples, porém mais robusto e modular, permitindo cadastro de múltiplos usuários e contas, autenticação, operações de depósito, saque e extrato.

## Como executar

1. Certifique-se de ter o Python 3 instalado.
2. No terminal, navegue até a pasta `sistema_bancario_2`.
3. Execute o script:

```bash
python script_banco_v2.py
```

## Funcionalidades

- **Cadastro de Usuários:** Permite criar novos usuários com CPF, nome, data de nascimento e endereço.
- **Cadastro de Contas:** Cada usuário pode ter uma ou mais contas bancárias.
- **Autenticação:** Usuário faz login pelo CPF e seleciona a conta para operar.
- **Depósito:** Realiza depósitos em contas selecionadas.
- **Saque:** Permite saques respeitando limite diário e de valor.
- **Extrato:** Exibe o histórico de movimentações e saldo da conta.
- **Interface de Menu:** Menus interativos e navegação amigável.
- **Validações:** CPF, valores e limites são validados em todas as operações.
- **Limpeza de Tela:** A interface limpa a tela entre menus para melhor experiência.

## Estrutura do Código

- O código é modular, com funções para cada operação.
- Não utiliza variáveis globais: listas de usuários e contas são passadas entre funções.
- Pronto para ser evoluído para orientação a objetos (OOP) em versões futuras.

---

## Comparativo: `script_banco_v2.py` vs `desafio_banco_1.py`

| Funcionalidade                | `desafio_banco_1.py` | `script_banco_v2.py` |
|-------------------------------|:--------------------:|:--------------------:|
| Múltiplos usuários            | ❌                   | ✅                   |
| Múltiplas contas por usuário  | ❌                   | ✅                   |
| Cadastro de usuário           | ❌                   | ✅                   |
| Autenticação                  | ❌                   | ✅                   |
| Seleção de conta              | ❌                   | ✅                   |
| Modularização (funções)       | Básica               | Avançada             |
| Validação de CPF              | ❌                   | ✅                   |
| Limpeza de tela               | ❌                   | ✅                   |
| Pronto para OOP               | ❌                   | ✅                   |

### Resumo dos Adicionais

- **Usuários e contas:** Agora é possível cadastrar vários usuários, cada um com múltiplas contas.
- **Autenticação:** O sistema exige login por CPF e seleção de conta.
- **Validações:** CPF, limites de saque e depósito são validados.
- **Interface:** Menus mais claros, tela limpa entre operações e mensagens mais amigáveis.
- **Código modular:** Funções separadas para cada responsabilidade, facilitando manutenção e evolução.

---

## Próximos Passos

A próxima versão (`v3`) irá migrar o sistema para orientação a objetos, tornando o código ainda mais organizado e escalável.

---

**Desenvolvido para o desafio da DIO - Trilha Python**