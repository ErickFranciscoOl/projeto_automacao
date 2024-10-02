# Projeto de Automação em Python

Este projeto em Python automatiza uma tarefa repetitiva e cansativa do dia a dia: preencher manualmente informações de produtos (nome, quantidade e valor) em um programa específico. O script lê um arquivo .txt com os dados dos produtos e preenche automaticamente cada campo no programa de registro.

## Arquivos do projeto

* app.exe - O programa em que as informações dos produtos são inseridas. É necessário cadastrar um usuário e, após login, a página do sistema será acessada.
* produtos.txt - Arquivo contendo a lista de produtos a serem lançados no sistema.
* projeto_automacao.py - Código da automação em Python.

## Tecnologias e bibliotecas usadas

PyAutoGUI - Usada para simular movimentos do mouse e teclado.
time.sleep - Usado para evitar que o script rode rápido demais e cause falhas no sistema.
MouseInfo - Ferramenta usada para obter as coordenadas do mouse.

### Como usar o MouseInfo:
* Abra o CMD;
* Digite python;
* Digite from mouseinfo import mouseinfo;
* Digite mouseInfo().

# Passos da automação

A automação foi criada com base nas etapas manuais necessárias para registrar um produto:

 1. Clicar no campo de usuário e digitar o nome de usuário.
 2. Clicar no campo de senha e digitar a senha.
 3. Clicar no botão de "Entrar".
 4. Extrair as informações do produto do arquivo produtos.txt.
 5. Clicar no campo de nome do produto e digitar o nome.
 6. Clicar no campo de quantidade e inserir a quantidade.
 7. Clicar no campo de valor e digitar o valor.
 8. Clicar no botão de "Registrar".

O código foi escrito para seguir essa sequência de ações.
