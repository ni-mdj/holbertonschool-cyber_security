#!/bin/bash
ps -U "$1" -u "$1" u | grep -v " 0 0 "
