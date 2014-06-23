
site: content/geopython.html content/unixshell.html content/index.html content/requirements.html
	hyde gen

content/geopython.html: content/geopython.pytml
	pytml --disable-cache $< >$@

PDF=pandoc -o $@ $<

docs: qgis.pdf unixshell.pdf geopython.pdf

qgis.pdf: qgis.html
	$(PDF)

unixshell.pdf: unixshell.html
	$(PDF)

geopython.pdf: geopython.html
	$(PDF)
