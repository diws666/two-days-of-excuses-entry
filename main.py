#!/usr/bin/env python3
import os

# Excuse text: exactly 91 characters (UTF-8 bytes).
EXCUSE = "I missed the deadline because I was waiting for you to finish your sentence. You never did."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(EXCUSE)
