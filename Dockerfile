FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
    ghostscript \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-lang-portuguese \
    texlive-publishers \
    texlive-font-utils \
    make

WORKDIR /home/latex