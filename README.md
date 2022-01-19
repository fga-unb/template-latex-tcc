# Template TCC FGA-UnB

Template para Trabalhos de Conclusão de Cursos (TCC) na Faculdade do
Gama (FGA) em Latex.

Licenciado em Creative Commons Atribuição 3.0:
http://creativecommons.org/licenses/by/3.0/

Desenvolvido e adaptado pelo professor Edson Alves <edsomjr@gmail.com>.

## Dependências
Para utilizar, certifique-se de ter instalados no seu ambiente o [Docker](https://docs.docker.com/engine/install/) e o [Docker-compose](https://docs.docker.com/compose/install/).

## Construindo imagem
Construa a imagem Docker que será utilizada com o comando:
```
docker-compose build latex
```

## Edição do template
Os arquivos para edição do template de TCC estão localizados na pasta `latex`. Depois de alterá-los utilizando um editor de texto, basta compilar os arquivos.

## Compilando o template de TCC e gerando o PDF
Execute o comando:
```
docker-compose up
```

Pronto! o PDF do seu projeto estará disponível em `latex/tcc.pdf`.


## Limpando 
Para limpar os arquivos gerados pelo latex:
```
docker-compose run latex bash -c 'make clean'
```
