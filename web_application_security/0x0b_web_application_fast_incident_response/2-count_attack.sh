#!/bin/bash

log_file="${1:-logs.txt}"

awk '{ print $1 }' "$log_file" | sort | uniq -c | sort -nr | head -n 1 | awk '{print $1}'
