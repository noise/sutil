all: pro/*.snap

*.snap:
	snapcraft

pro/prime: *.snap
	cp -pr prime pro/

pro/*.snap: pro/prime
	cd pro && snapcraft

.PHONY: clean
clean:
	snapcraft clean
	cd pro && snapcraft clean
	rm *.snap pro/*.snap

