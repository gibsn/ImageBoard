#!/bin/bash

rm -f main.aux main.dvi main.log main.ps main.toc
rm -f *.pdf
pdflatex main.tex
pdflatex main.tex
#open main.pdf
