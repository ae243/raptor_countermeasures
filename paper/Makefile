NAME=paper

TARGET=$(NAME)
BIBTEX := bibtex
TGIF   := tgif
XFIG   := xfig
GNUPLOT:= gnuplot

SOURCES=$(NAME).tex \
	sigproc.bib
# FIGS=	data/one.pdf \
#	data/two.pdf

all: $(TARGET).ps
pdf: all

$(TARGET).pdf: Makefile  $(SOURCES) $(FIGS)
	pdflatex  $(TARGET).tex
	-bibtex --min-crossrefs=100    $(TARGET)
	pdflatex  $(TARGET).tex

color: $(TARGET).pdf
	pdflatex $(TARGET).tex
	pdftops $(TARGET).pdf

$(TARGET).ps: $(TARGET).pdf
	pdflatex "\newcommand{\wantBW}{} \input{$(TARGET).tex}"
	pdftops $(TARGET).pdf

%.pdf : %.fig #Makefile
	fig2dev -L pdf -b 1 $< $@

%.eps : %.dia #Makefile
	dia --nosplash -e $@ $<

%.eps : %.obj
	TMPDIR=/tmp $(TGIF) -print -eps $<

%.pdf : %.eps #Makefile
	epstopdf $<

clean:
	rm -f *.aux *.log *.out *.bbl *.blg *~ *.bak $(FIGS) $(TARGET).ps $(TARGET).pdf
