.PHONY: clean all 

all: diagram.svg

diagram.svg: diagram.dvi
	dvisvgm -n diagram.dvi
	@cp diagram.svg ..

diagram.dvi: diagram.tex
	latex diagram.tex
	@rm -rf diagram.log diagram.aux auto 

clean: 
	@rm -rf diagram.log diagram.aux auto \
		diagram.dvi diagram.svg *~
