# Python Coding Agent

A versatile command-line Python coding agent framework with multiple capabilities for file operations, math, text processing, code generation, and more.

## Features

### 12+ Built-in Capabilities

| Category | Commands |
|----------|----------|
| **Math** | `math "expression"` - Basic arithmetic with safety filtering |
| **Text** | `reverse`, `upper`, `lower`, `count`, `wordcount`, `capitalize`, `swapcase`, `title`, `replace` |
| **File Ops** | `list`, `read <path>`, `write <path> <content>`, `delete <path>`, `exists <path>` |
| **Code Generation** | `template python/flask/django/cli`, `snippet fib/quick_sort/palindrome/binary_search`, `run <code>` |
| **Data** | `read/write <path>`, `json_parse <path>`, `json_emit <path> <json>` |
| **Convert** | `base64_encode/decode`, `hex_to_ascii`, `ascii_to_hex` |
| **Date/Time** | `now`, `format <pattern>`, `diff <date1> <date2>` |
| **Hash** | `md5`, `sha256`, `sha1` |
| **JSON** | `format <path>`, `parse <json_str>` |
| **Grep** | `grep <pattern> [file]` |
| **Stat** | `stat <path>` - size, modification time, existence |

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/python-coding-agent.git
cd python-coding-agent

# No additional dependencies needed - uses only Python standard library
```

## Usage

### Command Line

```bash
# Math operations
python3 coding_agent.py math "2+2*3"    # → = 8
python3 coding_agent.py math "10/3"     # → = 3.333...

# Text processing
python3 coding_agent.py text upper "hello"  # → HELLO
python3 coding_agent.py text reverse "abc"  # → cba

# File operations
python3 coding_agent.py file_ops list           # List current directory
python3 coding_agent.py file_ops write /tmp/x.txt "content"
python3 coding_agent.py file_ops read /tmp/x.txt

# Code generation
python3 coding_agent.py code template python    # Get Python template
python3 coding_agent.py code snippet fib        # Get Fibonacci snippet

# Hashing
python3 coding_agent.py hash sha256 "secret"    # → hash value

# Date operations
python3 coding_agent.py date now                # Current datetime
python3 coding_agent.py date diff 2023-01-01 2023-12-31

# Convert
python3 coding_agent.py convert base64_encode "test"  # → base64 string
python3 coding_agent.py convert hex_to_ascii "48656c6c6f"  # → "Hello"

# JSON
python3 coding_agent.py json format /path/to/file.json

# System commands
python3 coding_agent.py system "echo hello"

# Grep
python3 coding_agent.py grep "pattern" /path/to/file
```

### As a Python Module

```python
from coding_agent import CodingAgent

agent = CodingAgent()

# Use any capability
result = agent.run("math '5*6'")
print(result)  # → = 30

result = agent.run("code template flask")
print(result)  # → Flask app skeleton

result = agent.run("file_ops write /tmp/test.txt 'hello'")
print(result)  # → Written to /tmp/test.txt
```

## Project Structure

```
python-coding-agent/
├── coding_agent.py    # Main agent framework
├── README.md          # This file
├── LICENSE            # License file (optional)
└── .gitignore         # Git ignore file (optional)
```

## Safety

- Math expressions are validated against a safe character set before evaluation
- No external dependencies required (uses only Python standard library)
- File operations are contained within the script's capability layer

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).