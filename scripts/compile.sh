#!/bin/bash
# ensure that every file has a newline at the end

FORMAT=""
EXTRA=""

if [ $# -lt 1 ]; then
  echo "No format specified. Defaulting to PDF."
  FORMAT="pdf"
else
  case $1 in
    pdf)
      FORMAT=pdf
      EXTRA="--toc"
      ;;
    html)
      FORMAT=html
      ;;
    epub)
      FORMAT=epub
      ;;
    *)
      echo "Invalid format or no format provided: " $1
      exit 1
  esac
fi

echo "Compiling book into $FORMAT format."

python ./scripts/get_paths.py ./content > output/file_list.txt
pandoc -s `cat output/file_list.txt` -o output/output.$FORMAT $EXTRA

if [ $FORMAT=html ]; then
  rm -r output/media
  cp -R media output/
fi

echo "Book compliation complete. See output/ directory."
