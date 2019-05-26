#!/bin/bash

file_prefix="BICKER"
re='^[0-9]+$'

if [ -z "$1" ]; then
    echo "error: Argument 1 is required" >&2; exit 1
    exit 1
fi

if ! [[ $1 =~ $re ]] ; then
    echo "error: Argument ${1} is not a number" >&2; exit 1
    exit 1
fi

num_files=$1

for i in $(seq -f '%07g' 1 $num_files); do
    touch "${PWD}/${file_prefix}${i}.pdf";
done
