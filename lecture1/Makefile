LECTURENO = 1
NOTES = lecture$(LECTURENO)
HOMEWORK = homework$(LECTURENO)
# TEX = $(wildcard *.tex)
# BIB = references.bib
# FIGS = $(wildcard figures/*.pdf figures/*.png graphs/*.pdf graphs/*.png)

.PHONY: all clean

all: NOTES HOMEWORK

$(NOTES).pdf: $(NOTES).tex
	pdflatex $(NOTES).tex

$(HOMEWORK).pdf: $(HOMEWORK).tex
	pdflatex $(HOMEWORK).tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.fdb_latexmk *.fls $(NOTES).pdf $(HOMEWORK).pdf