TARGET = TCC_FGA.pdf

BIBTEX = bibtex
LATEX = pdflatex

VERSION = 0.1.0

FIXOS_DIR = fixos
FIXOS_SOURCES = informacoes.tex fichaCatalografica.tex \
        folhaDeAprovacao.tex pacotes.tex comandos.tex setup.tex \
        listasAutomaticas.tex indiceAutomatico.tex

FIXOS_FILES = $(addprefix $(FIXOS_DIR)/, $(FIXOS_SOURCES))

EDITAVEIS_DIR = editaveis
EDITAVEIS_SOURCES = informacoes.tex dedicatoria.tex \
                    agradecimentos.tex epigrafe.tex resumo.tex abstract.tex \
                    abreviaturas.tex simbolos.tex introducao.tex \
                    referencial-teorico.tex revisao-estruturada-literatura.tex \
                    planejamento.tex \
                    

EDITAVEIS_FILES = $(addprefix $(EDITAVEIS_DIR)/, $(EDITAVEIS_SOURCES))

MAIN_FILE = tcc.tex
AUX_FILE  = $(addsuffix .aux, $(basename $(MAIN_FILE)))
PDF_FILE  = $(addsuffix .pdf, $(basename $(MAIN_FILE)))

SOURCES = $(FIXOS_FILES) $(EDITAVEIS_FILES)

.PHONY: all clean dist-clean

all: 
	@make $(TARGET)
     
$(TARGET): $(MAIN_FILE) $(SOURCES) bibliografia.bib
	$(LATEX) -shell-escape $(MAIN_FILE)
	$(BIBTEX) $(AUX_FILE)
	$(LATEX) -shell-escape $(MAIN_FILE)
	$(LATEX) -shell-escape $(MAIN_FILE)
	@cp $(PDF_FILE) $(TARGET)

clean:
	rm -f *~ *.dvi *.ps *.backup *.aux *.log
	rm -f *.lof *.lot *.bbl *.blg *.brf *.toc *.idx
	rm -f *.pdf
	
dist: clean
	tar vczf tcc-fga-latex-$(VERSION).tar.gz *

dist-clean: clean
	rm -f $(PDF_FILE) $(TARGET)