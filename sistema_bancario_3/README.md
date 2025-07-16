# Sistema Bancário v3

Este projeto é a terceira versão do sistema bancário desenvolvido na trilha Python da DIO. Agora, o sistema está totalmente orientado a objetos, trazendo mais robustez, organização e facilidade de manutenção em relação à versão anterior (`script_banco_v2`).

## Principais Novidades em Relação ao v2

- **Orientação a Objetos (OOP):**  
  O sistema foi reestruturado usando classes para representar entidades como Banco, Cliente, Conta, Transação, Saque e Depósito. Isso torna o código mais modular, reutilizável e fácil de expandir.

- **Herança e Polimorfismo:**  
  Classes como `ContaCorrente` herdam de `Conta`, e transações como `Saque` e `Deposito` herdam de uma classe abstrata `Transacao`, permitindo especialização e comportamento customizado.

- **Encapsulamento:**  
  Os dados dos clientes e contas agora são atributos privados das classes, acessados por métodos e propriedades, aumentando a segurança e integridade dos dados.

- **Validação Avançada:**  
  CPF, endereço e data de nascimento são validados por métodos específicos, com mensagens claras de erro.

- **Histórico de Transações:**  
  Cada conta mantém um histórico detalhado das operações realizadas, exibido de forma organizada.

- **Processamento de Transações:**  
  Saques e depósitos são tratados como objetos de transação, facilitando o registro e o controle das operações.

- **Interface mais limpa:**  
  Menus e telas são limpos entre operações, proporcionando melhor experiência ao usuário.

## Comparativo: v2 vs v3

| Funcionalidade                | v2 (Procedural)      | v3 (OOP)              |
|-------------------------------|:--------------------:|:---------------------:|
| Paradigma principal           | Procedural           | Orientado a Objetos   |
| Cadastro de múltiplos usuários| ✅                   | ✅                    |
| Múltiplas contas por usuário  | ✅                   | ✅                    |
| Autenticação por CPF          | ✅                   | ✅                    |
| Seleção de conta              | ✅                   | ✅                    |
| Validação de dados            | Básica               | Avançada              |
| Histórico de transações       | Simples (string)     | Detalhado (classe)    |
| Modularização                 | Funções              | Classes e métodos     |
| Extensibilidade               | Limitada             | Alta                  |
| Encapsulamento                | ❌                   | ✅                    |
| Herança/Polimorfismo          | ❌                   | ✅                    |
| Processamento de transações   | Função               | Objetos               |
| Pronto para persistência      | Parcial              | Facilitado            |

## Como Executar

1. Certifique-se de ter Python 3 instalado.
2. Navegue até a pasta `sistema_bancario_3` no terminal.
3. Execute o script:

```bash
python script_banco_v3.py
```

## Próximos Passos

- Implementar persistência dos dados (salvar clientes e contas em arquivos).
- Adicionar testes automatizados.
- Melhorar a interface para múltiplas operações sem reiniciar o menu.

---

**Desenvolvido para o desafio da DIO -