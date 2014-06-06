
site: content/geopython.html content/unixshell.html content/index.html content/requirements.html
	hyde gen

content/geopython.html: content/geopython.pytml
	pytml --disable-cache $< >$@
