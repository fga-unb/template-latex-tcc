Template TCC FGA-UnB
====================

Template para Trabalhos de Conclusão de Cursos (TCC) na Faculdade do
Gama (FGA) em Latex.

Licenciado em Creative Commons Atribuição 3.0:
http://creativecommons.org/licenses/by/3.0/

Desenvolvido e adaptado pelo professor Edson Alves <edsomjr@gmail.com>.

## Instalação

### Ubuntu 12.10 ou superior

Uma vez que a versão recomendada do Tex Live é a 2012 ou superior, o processo de
instalação via apt-get funciona apenas a partir da versão 7.0 do Debian (também 
conhecida como Wheezy) e suas derivadas, como por exemplo Ubuntu 12.10 (também 
conhecida como Quantal Quetzal), Linux Mint 14, entre outras.

Para instalar o abnTeX2 (e as respectivas dependências, como o próprio TeXLive) 
em uma distribuição Debian ou derivada, utilize a instalação via apt-get (ou 
outro gerenciador de pacotes que preferir):

1. Adicione a seguinte linha ao arquivo /etc/apt/sources.list:
	deb http://distrib.abntex2.googlecode.com/hg/debian/ testing main

	Opcionalmente, adicione a linha abaixo caso deseje baixar os fontes:
	deb-src http://distrib.abntex2.googlecode.com/hg/debian/ testing main

2. Adicione a chave pública ao chaveiro do apt:
	$ wget -O - http://distrib.abntex2.googlecode.com/hg/debian/89C55467.asc|sudo apt-key add - 

3. Instale o abntex2:
	$ sudo apt-get update && sudo apt-get install abntex2

4. Para atualizar uma instalação já existente, feita a partir do repositório:
	$ sudo apt-get update && sudo apt-get upgrade

Após o processo de instalação, você poderá ler os manuais e testar os exemplos 
que estarão disponíveis nos diretórios /usr/share/doc/abntex2/pdf e 
/usr/share/doc/abntex2/latex respectivamente.


