# https://stackoverflow.com/a/2483203
TEX_FILES := $(shell find latex -name '*.tex' -type f)
PDF_FILES = $(patsubst %.tex, output/%.pdf, $(TEX_FILES))
CLEAN_TARGETS = $(addsuffix .clean, $(TEX_FILES))


$(CLEAN_TARGETS):
	rm -rf $(@D)/{_minted-*,*.{aux,fdb_latexmk,fls,log,nav,out,snm,toc,bbl,blg,pdf}}

clean: $(CLEAN_TARGETS)
	rm -rf output

# https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html
output/%.pdf: %.tex
	@echo compiling $(<F)
	(cd $(<D) && latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode -shell-escape $(<F) > /dev/null)
	mkdir -p output/$(<D)
	cp $(patsubst %.tex, %.pdf, $<) $@

pdf: $(PDF_FILES)

html:
	pelican content

html-release:
	pelican content -s publishconf.py

site: clean html pdf

site-release: clean html-release pdf

apt:
	sudo apt update && sudo apt install graphviz

pypi:
	pip install -r requirements.txt


.PHONY: pdf html site html-release site-release clean apt pypi $(CLEAN_TARGETS)

