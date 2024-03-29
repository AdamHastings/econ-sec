LECTURENO = 3
NOTES = lecture
HOMEWORK = homework
# TEX = $(wildcard *.tex)
# BIB = references.bib
# FIGS = $(wildcard figures/*.pdf figures/*.png graphs/*.pdf graphs/*.png)
FIGS = figures/

.PHONY: all clean

all: $(NOTES).pdf $(HOMEWORK)$(LECTURENO).pdf

$(NOTES).pdf: $(NOTES).tex $(FIGS)
	pdflatex $(NOTES).tex

$(HOMEWORK)$(LECTURENO).pdf: $(HOMEWORK).tex $(FIGS)
	pdflatex $(HOMEWORK).tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.fdb_latexmk *.fls *.synctex.gz $(NOTES).pdf $(HOMEWORK)$(LECTURENO).pdf