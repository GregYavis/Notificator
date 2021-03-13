#!/bin/bash
phrase=$1
#echo $phrase
termux-notification "$phrase"
termux-vibrate
