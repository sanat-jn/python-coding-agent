# Python Coding Agent - Demo Version

A fun little Python script that acts as a coding helper/agent. Good for learning, quick tasks, or playing around with code.

Not production-ready or state-of-the-art. Just a demo.

## What It Does

Run basic commands from the command line:

- **Math**: `2+2*3` → `8`
- **Text**: reverse, uppercase, lowercase, count words
- **File ops**: read, write, list files
- **Code gen**: get Python/Flask/Django templates or code snippets
- **Convert**: base64, hex <-> ASCII
- **Hash**: md5, sha256, sha1
- **Date**: current time, date differences
- **JSON**: format or parse JSON
- **Grep**: search text in files
- **Stat**: file info (size, modified date)

## Quick Start

```bash
# Make it executable
chmod +x coding_agent.py

# Run commands
./coding_agent.py math "10/3"
./coding_agent.py text upper "hello"
./coding_agent.py code template python
./coding_agent.py file_ops write /tmp/test.txt "hi"
```

Or import it in Python:

```python
from coding_agent import CodingAgent
agent = CodingAgent()
agent.run("math '5*6'")
```

## Features (for Demo Purposes)

| Command | Example |
|---------|---------|
| `math "expr"` | `math "2+2"` → `= 4` |
| `text upper "txt"` | `text upper "hi"` → `HI` |
| `file_ops write path content` | writes file |
| `code template python` | returns Python script skeleton |
| `code snippet fib` | returns Fibonacci code |
| `hash sha256 "text"` | returns hash |
| `date now` | current datetime |
| `convert base64_encode "hi"` | base64 encode |
| `json format path` | format JSON file |
| `grep "pattern" file` | search text |
| `stat path` | file stats |

## How It Works (the short version)

This is a Python script that uses **pattern matching** on your command to decide what to do. Think of it like a simple CLI with a menu of options.

**Under the hood:**
1. You type a command like `math "2+2"` or `file_ops write /tmp/x "hi"`
2. The script splits your input into a **category** (`math`, `file_ops`, etc.) and **arguments**
3. It looks up the right handler function for that category
4. That function does the task and returns the result
5. The result gets printed to your screen

**No magic, no AI** - just a series of `if/elif` checks and Python standard library functions (math, os, json, hashlib, datetime, subprocess, etc.)

**Adding new features** is just a matter of:
- Adding a new handler function to the `CodingAgent` class
- Registering it in the `capabilities` dictionary
- Adding the command pattern to the README

## No Installation Needed

Just Python 3. Uses only standard library. No pip install required.

## Learn & Play

Good for:
- Learning Python basics
- Quick file/math/text operations
- Code snippet templates
- Playing around with CLI tools

Not for production use. Just a demo.

---

Made with Python 🐍