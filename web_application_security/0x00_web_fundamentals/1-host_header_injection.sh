#!/bin/bash
curl -s -H "Host: $1" -H "X-Forwarded-Host: $1" -d "$3" "$2"