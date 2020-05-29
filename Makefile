#!/usr/bin/make -f

SHELL := /bin/bash


deb:
	mkdir -p dist
	docker run -ti -e RUN_UID=`id -u` -v `pwd`:/home/bob/build phlax/debian-build bash -c "\
	  cd build \
	  && debuild -b \
	  && cp -a ../*deb dist"

pysh:
	pip install -U pip setuptools termcolor
	pip install -e 'git+https://github.com/phlax/pysh#egg=pysh.test&subdirectory=pysh.test'

publish:
	git checkout master
	git fetch origin
	git rebase origin/master
	make deb
