#!/bin/bash

log_file="${1:-logs.txt}"

attacker_ip=$(awk '{print $1}' "$log_file" | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}')

awk -v ip="$attacker_ip" '$1 == ip {print}' "$log_file" \
  | awk -F'"' '{print $6}' \
  | sort \
  | uniq -c \
  | sort -nr \
  | head -n 1 \
  | sed 's/^[[:space:]]*[0-9][0-9]*[[:space:]]*//'
