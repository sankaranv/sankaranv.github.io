#!/bin/bash

cd ./resume
if [ ! -d "./build" ]; then
  mkdir build
fi
pdflatex -output-directory=./build main.tex
cp ./build/main.pdf ../files/Sankaran_CV.pdf
git add .
git commit -m "Update resume content"
git push