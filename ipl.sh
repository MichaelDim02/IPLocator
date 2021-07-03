#!/bin/sh

curl -s ipinfo.io/"$1" | sed 's/"//g' | awk 'NR>2 {print last} {last=$0}'
