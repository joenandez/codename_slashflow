#!/usr/bin/env python3

import sys
import json
import re

# Read input and log it for debugging
input_data = sys.stdin.read()

# Log the raw input to debug file
with open('/tmp/hook-debug.log', 'a') as f:
    f.write(f"Raw input: {input_data}\n")

try:
    data = json.loads(input_data)
    command = data.get('tool_input', {}).get('command', '')

    # Log the parsed command
    with open('/tmp/hook-debug.log', 'a') as f:
        f.write(f"Parsed command: {command}\n")

    # Check for dangerous commands (rm and sudo)
    if re.search(r'\b(rm|sudo)\s+', command):
        with open('/tmp/hook-debug.log', 'a') as f:
            f.write(f"BLOCKING: {command}\n")
        sys.exit(2)  # Block the command
    else:
        with open('/tmp/hook-debug.log', 'a') as f:
            f.write(f"ALLOWING: {command}\n")
        sys.exit(0)  # Allow the command

except Exception as e:
    with open('/tmp/hook-debug.log', 'a') as f:
        f.write(f"ERROR: {str(e)}\n")
    sys.exit(2)  # Block on error