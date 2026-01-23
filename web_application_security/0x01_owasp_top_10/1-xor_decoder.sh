#!/bin/bash
INPUT="$1"

python3 - <<'PY' "$INPUT"
from base64 import b64decode
import sys

# Get argument and remove {xor} prefix
raw = sys.argv[1].replace("{xor}", "")

# Decode base64
data = b64decode(raw)

# XOR with WebSphere legacy key (0x5f = '_')
decoded = bytes(byte ^ 0x5F for byte in data)

# Print result
print(decoded.decode("utf-8"))
PY
