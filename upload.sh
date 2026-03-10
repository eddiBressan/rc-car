#!/bin/bash
rsync -avz --exclude='.git' ./ pi@192.168.1.135:/home/pi/test