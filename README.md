# Sobre o projeto
Meu projeto tem como objetivo auxiliar no levantamento de aparelhos eletrônicos de uma residência. Esse levantamento pode ser usado tanto para inventário patrimonial quanto para auxiliar no cálculo do balanceamento elétrico ao se fazer um quadro de luz.

# Como executar

Copiar o repositório para uma pasta local e executar os comandos abaixo pelo terminal após entrar no diretório do repositório:

1- Criar uma virtualenv
```
virtualenv nome_da_virtualenv
```

2- Ativar a virtualenv
```
nome_da_virtualenv\Scripts\Activate
```

3- Instalar as bibliotecas do arquivo requirements.txt 
```
(env)$ pip install -r requirements.txt
```

4- Executar a API:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```
5- Após uma mudança no código fonte:

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

6 - Abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
