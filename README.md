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
### FAQ

Caso você encontre algum erro na execução dos comandos acima, siga as instruções abaixo:

1. Adicione o grupo `docker` ao seu usuário com o comando
```
sudo usermod -a -G docker $USER
```

1. Altere as permissões do arquivo `/var/run/docker.sock` com o comando:
```
sudo chown $USER /var/run/docker.sock
```

1. Caso o Docker não esteja rodando, inicie o serviço (e agende o início automático no _boot_) com os comandos:
```
sudo systemctl enable docker
sudo systemctl start docker
```
