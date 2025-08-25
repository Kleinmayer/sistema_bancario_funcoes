# 🏦 Sistema Bancário em Python  

Este repositório contém a implementação de um **sistema bancário simples** desenvolvido em **Python**, como parte de um desafio prático.  

O projeto tem como objetivo reforçar conceitos de programação, lógica, funções e manipulação de dados em dicionários e listas.  

---

## 🚀 Funcionalidades  

- **Criar Usuário**: cadastra clientes com nome, CPF, data de nascimento e endereço.  
- **Criar Conta Corrente**: cada conta é vinculada a um usuário já existente.  
- **Depósito**: adiciona valores à conta.  
- **Saque**: permite retiradas respeitando limite diário e valor máximo por saque.  
- **Extrato**: exibe histórico de movimentações e saldo atualizado.  

---

## 📌 Estrutura do Código  

O sistema é composto por funções que simulam operações bancárias:  

- `criar_usuario()` → cadastra usuários.  
- `criar_conta()` → abre novas contas associadas a um CPF válido.  
- `depositar()` → registra depósitos e atualiza o saldo.  
- `sacar()` → realiza saques respeitando regras definidas.  
- `exibir_extrato()` → imprime todas as movimentações e saldo atual.  

Os dados de **usuários** e **contas** são armazenados em listas de dicionários, simulando um banco de dados simples.  
