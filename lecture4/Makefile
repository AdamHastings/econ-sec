LECTURENO = 3
NOTES = lecture
HOMEWORK = homework
# TEX = $(wildcard *.tex)
# BIB = references.bib
# FIGS = $(wildcard figures/*.pdf figures/*.png graphs/*.pdf graphs/*.png)
FIGS = figures/

.PHONY: all clean

all: $(NOTES).pdf $(HOMEWORK)3.pdf

$(NOTES).pdf: $(NOTES).tex $(FIGS)
	pdflatex $(NOTES).tex

$(HOMEWORK)3.pdf: $(HOMEWORK).tex $(FIGS)
	pdflatex $(HOMEWORK).tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.fdb_latexmk *.fls $(NOTES).pdf $(HOMEWORK).pdf