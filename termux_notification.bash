#!/bin/bash
phrase=$1
#echo $phrase
termux-notification -g top $phrase
termux-vibrate