.PHONY: clean all publish

all: algo.svg

algo.svg: algo.dvi
	dvisvgm -n algo.dvi
	@cp algo.svg ..

algo.dvi: algo.tex
	latex algo.tex
	@rm -rf algo.log algo.aux auto 

clean: 
	@rm -rf algo.log algo.aux auto \
		algo.dvi algo.svg *~
