#!/bin/bash
phrase=$1
#echo $phrase
termux-notification --title "$phrase"
termux-vibrate
