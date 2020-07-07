PDF=pdflatex
BIB=bibtex
LATEXOBJS= *.aux *.log *.out *.pdf *.bbl *.blg

RHEADER=report
RSRCS=$(RHEADER).tex

.PHONY: clean report

all: report-no-bib

report:
	$(PDF) $(RSRCS)
	$(BIB) $(RHEADER)
	$(PDF) $(RSRCS)
	$(PDF) $(RSRCS)

report-no-bib:
	$(PDF) $(RSRCS)

clean:
	rm -rf $(LATEXOBJS)
