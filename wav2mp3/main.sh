#!/bin/sh
#
#  PROGRAM: main.sh
# 
#  This is the main panel for data uploader
#  
#
#
#
#
#
function menu(){
    echo "#### MENU ####\n1) upload \n2) upload+intents \n3) wav2mp3+upload \n4) intents \n5) Exit"
}

PS3="select item: "
select VAR in upload  upload+intents wav2mp3+upload intents exit 
do
    case $VAR in
	"upload" ) 
           python uploadfiles.py
           menu
           ;;
	"upload+intents" ) 
           python uploadfiles.py
           ./intent_gen.sh
           menu
           ;;
	"wav2mp3+upload" ) 
           python wav2mp3.py
           python uploadfiles.py
           menu
           ;;
	"intents" )
           ./intent_gen.sh
           menu
           ;;
	"exit" ) break ;;
#	* ) menu
    esac
done
