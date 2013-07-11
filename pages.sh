#!/usr/bin/env bash

mkdir -p build
cd build
# Please edit me to fit to your repository URL
git clone git@github.com:brunobord/booklet-boilerplate.git .
git checkout origin/gh-pages -b gh-pages
git branch -d master

