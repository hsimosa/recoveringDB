#!/bin/bash

# From TIFF to TXT using TESSERACT
# Usage: ./TESS2TXT.sh imagefile [textfile]
# creates a plain text file with the text found in imagefile
# Taken from: https://help.ubuntu.com/community/OCR

if [ "$1" ] && [ -e "$1" ]; then
  TMPF=$(mktemp --tmpdir=/home/USER/Desktop/ALG/recoveringBD/tmp XXXXXXXX.tif)
  DEST="$2"
  if [ ! "$DEST" ]; then
    DEST="${1%.*}.txt"
    if [ -e "$DEST" ]; then
      echo "$DEST already exists; please provide a new textfile name" >&2
      exit 1
    fi
  fi
  /usr/bin/convert "$1" -colorspace Gray -depth 1 $TMPF 
  cp $1 $TMPF && /usr/bin/tesseract $TMPF "$DEST"  -l spa -psm 6  
  EX=$?
  /bin/rm -f $TMPF
  [ $EX -eq 0 ] && [ "$TERM" ] && echo "created $DEST"
  exit $EX
else
  echo "Usage: $0 imagefile [textfile]" >&2
  echo " creates a plain text file with the text found in imagefile" >&2
  exit 1
fi
