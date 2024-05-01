#!/bin/bash
#Script that takes in a URL, send a GET request to me URL, displays the body the reponse.
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
