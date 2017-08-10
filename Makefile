all: python.html project.html

%.html: %.md
	pandoc --mathjax -s -o $@ $<
