#!/bin/bash

inotifywait -q -m -e close_write -r *.py | while read -r filename event;
do
	clear
	echo -e "\n\n\033[1;7;37mRunning script because $filename was $event\033[0;1;0m"
	./${filename} 'abc'
done;
