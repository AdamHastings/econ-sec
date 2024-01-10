LECTURENO = 2
NOTES = lecture$(LECTURENO)
HOMEWORK = homework$(LECTURENO)
# TEX = $(wildcard *.tex)
# BIB = references.bib
# FIGS = $(wildcard figures/*.pdf figures/*.png graphs/*.pdf graphs/*.png)
FIGS = figures/

.PHONY: all clean

all: $(NOTES).pdf $(HOMEWORK).pdf

$(NOTES).pdf: $(NOTES).tex $(FIGS)
	pdflatex $(NOTES).tex

$(HOMEWORK).pdf: $(HOMEWORK).tex $(FIGS)
	pdflatex $(HOMEWORK).tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.fdb_latexmk *.fls $(NOTES).pdf $(HOMEWORK).pdf