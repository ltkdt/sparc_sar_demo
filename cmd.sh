#!/bin/bash

# Linux system: 
cd ~/esa-snap/bin
./snap --nosplash --nogui --modules --list --refresh

# Windows: snap54.exe

:'
SLC file in zip format

This will loop through and apply the graph processing to all the products in our data folder, and output
the orbit corrected, IW1 swath images into our folder titled iw1.

'

mkdir iw1; for f in *.zip; do gpt myGraph.xml -PinputFile=$f -PoutputFile=”iw1/$f”; done