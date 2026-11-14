FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
    ghostscript \
    texlive-publishers \
    texlive-lang-portuguese \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-base \
    make

WORKDIR /home/latex