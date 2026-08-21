#!/usr/bin/env python3
"""Enhanced Python Coding Agent Framework with many capabilities"""

import sys
import json
import os
import argparse
import subprocess
import urllib.request
import re
import hashlib
import json as json_mod
from datetime import datetime as dt_datetime


class CodingAgent:
    def __init__(self):
        self.capabilities = {
            "file_ops": self.handle_file_ops,
            "math": self.handle_math,
            "text": self.handle_text,
            "web": self.handle_web,
            "system": self.handle_system,
            "code": self.handle_code,
            "data": self.handle_data,
            "convert": self.handle_convert,
            "date": self.handle_date,
            "hash": self.handle_hash,
            "json": self.handle_json,
            "grep": self.handle_grep,
            "stat": self.handle_stat,
        }
        self.history = []

    def run(self, input_data):
        if isinstance(input_data, str):
            parts = input_data.split()
            if not parts:
                return "No input provided"
            command = parts[0].lower()
            args = parts[1:]
        elif isinstance(input_data, dict):
            command = input_data.get("command", "").lower()
            args = input_data.get("args", [])
        else:
            return "Unsupported input format"

        if command in self.capabilities:
            result = self.capabilities[command](args)
            self.history.append({"command": command, "args": args, "result": result})
            return result
        return f"Unknown command: {command}. Available: {', '.join(self.capabilities.keys())}"

    # ---- File Operations ----
    def handle_file_ops(self, args):
        if not args:
            return "Usage: file_ops <list|read <path>|write <path> <content>>"
        subcmd = args[0].lower()
        if subcmd == "list":
            try:
                return os.listdir(".")
            except Exception as e:
                return f"Error: {e}"
        elif subcmd == "read":
            if len(args) < 2:
                return "Usage: file_ops read <path>"
            try:
                with open(args[1], "r") as f:
                    return f.read()
            except Exception as e:
                return f"Error reading file: {e}"
        elif subcmd == "write":
            if len(args) < 3:
                return "Usage: file_ops write <path> <content>"
            try:
                with open(args[1], "w") as f:
                    f.write(args[2])
                return f"Written to {args[1]}"
            except Exception as e:
                return f"Error writing file: {e}"
        elif subcmd == "delete":
            if len(args) < 2:
                return "Usage: file_ops delete <path>"
            try:
                os.remove(args[1])
                return f"Deleted {args[1]}"
            except Exception as e:
                return f"Error deleting file: {e}"
        elif subcmd == "exists":
            if len(args) < 2:
                return "Usage: file_ops exists <path>"
            return os.path.exists(args[1])
        return f"Unknown file ops subcommand: {subcmd}"

    # ---- Math ----
    def handle_math(self, args):
        try:
            if not args:
                return "Usage: math <expression>"
            expr = " ".join(args)
            allowed = set("0123456789+-*/(). sqrt")
            if any(c not in allowed and not c.isspace() for c in expr):
                return "Unsafe expression"
            result = eval(expr)
            return f"= {result}"
        except Exception as e:
            return f"Math error: {e}"

    # ---- Text Operations ----
    def handle_text(self, args):
        if not args:
            return "Usage: text <operation> [text]"
        op = args[0].lower()
        text = " ".join(args[1:]) if len(args) > 1 else ""
        if op == "reverse":
            return text[::-1]
        elif op == "upper":
            return text.upper()
        elif op == "lower":
            return text.lower()
        elif op == "count":
            return len(text)
        elif op == "wordcount":
            return len(text.split())
        elif op == "capitalize":
            return text.capitalize()
        elif op == "swapcase":
            return text.swapcase()
        elif op == "title":
            return text.title()
        elif op == "replace":
            if len(args) < 3:
                return "Usage: text replace <old> <new>"
            return text.replace(args[1], args[2])
        return f"Unknown text op: {op}"

    # ---- Web ----
    def handle_web(self, args):
        try:
            url = args[0] if args else "https://example.com"
            with urllib.request.urlopen(url, timeout=15) as response:
                content = response.read().decode("utf-8", errors="replace")
                return content[:800]
        except Exception as e:
            return f"Web error: {e}"

    # ---- System ----
    def handle_system(self, args):
        if not args:
            return "Usage: system <command>"
        try:
            result = subprocess.run(args, capture_output=True, text=True, timeout=30)
            return f"stdout: {result.stdout[-500:]}\nstderr: {result.stderr[-500:]}\nreturncode: {result.returncode}"
        except Exception as e:
            return f"System error: {e}"

    # ---- Code Generation ----
    def handle_code(self, args):
        if not args:
            return "Usage: code <template|snippet|run> [name]"
        subcmd = args[0].lower()
        if subcmd == "template":
            if len(args) < 2:
                return "Usage: code template <name>"
            templates = {
                "python": "#!/usr/bin/env python3\nimport sys\n\ndef main():\n    print(\"Hello from Python!\")\n\n\nif __name__ == \"__main__\":\n    main()",
                "flask": "from flask import Flask\napp = Flask(__name__)\n\n@app.route(\"/\")\ndef hello():\n    return \"Hello!\"\n\n\nif __name__ == \"__main__\":\n    app.run(debug=True)",
                "django": "from django.http import HttpResponse\nfrom django.urls import path\ndef index(request):\n    return HttpResponse(\"Hello\")\n\nurlpatterns = [path(\"\", index)]",
                "cli": "#!/usr/bin/env python3\nimport argparse\nimport sys\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--name\", default=\"World\")\n    args = parser.parse_args()\n    print(f\"Hello, {args.name}!\")\n\n\nif __name__ == \"__main__\":\n    main()",
            }
            name = args[1].lower()
            if name in templates:
                return templates[name]
            return f"Template '{name}' not found. Available: {', '.join(templates.keys())}"
        elif subcmd == "snippet":
            if len(args) < 2:
                return "Usage: code snippet <name>"
            snippets = {
                "fib": "def fib(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a + b\n    return a",
                "quick_sort": "def quick_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = quick_sort([x for x in arr if x < pivot])\n    middle = quick_sort([x for x in arr if x == pivot])\n    right = quick_sort([x for x in arr if x > pivot])\n    return left + middle + right",
                "palindrome": "def is_palindrome(s):\n    return s == s[::-1]",
                "binary_search": "def binary_search(arr, x):\n    low, high = 0, len(arr) - 1\n    while low <= high:\n        mid = (low + high) // 2\n        if arr[mid] < x:\n            low = mid + 1\n        elif arr[mid] > x:\n            high = mid - 1\n        else:\n            return mid\n    return -1",
            }
            name = args[1].lower()
            if name in snippets:
                return snippets[name]
            return f"Snippet '{name}' not found. Available: {', '.join(snippets.keys())}"
        elif subcmd == "run":
            if len(args) < 2:
                return "Usage: code run <python_code>"
            try:
                exec(args[1])
                return "Code executed successfully"
            except Exception as e:
                return f"Execution error: {e}"
        return f"Unknown code subcommand: {subcmd}"

    # ---- Data Operations ----
    def handle_data(self, args):
        if not args:
            return "Usage: data <operation> [args...]"
        op = args[0].lower()
        if op == "read":
            if len(args) < 2:
                return "Usage: data read <path>"
            try:
                with open(args[1], "r") as f:
                    return f.read()
            except Exception as e:
                return f"Error: {e}"
        elif op == "write":
            if len(args) < 3:
                return "Usage: data write <path> <content>"
            try:
                with open(args[1], "w") as f:
                    f.write(args[2])
                return f"Written to {args[1]}"
            except Exception as e:
                return f"Error: {e}"
        elif op == "json_parse":
            if len(args) < 2:
                return "Usage: data json_parse <path>"
            try:
                with open(args[1], "r") as f:
                    return json_mod.load(f)
            except Exception as e:
                return f"Error: {e}"
        elif op == "json_emit":
            if len(args) < 3:
                return "Usage: data json_emit <path> <json_str>"
            try:
                with open(args[1], "w") as f:
                    f.write(args[2])
                return f"Written to {args[1]}"
            except Exception as e:
                return f"Error: {e}"
        return f"Unknown data op: {op}"

    # ---- Convert ----
    def handle_convert(self, args):
        if not args:
            return "Usage: convert <operation> [args...]"
        op = args[0].lower()
        if op == "base64_encode":
            if len(args) < 2:
                return "Usage: convert base64_encode <text>"
            import base64
            return base64.b64encode(args[1].encode()).decode()
        elif op == "base64_decode":
            if len(args) < 2:
                return "Usage: convert base64_decode <text>"
            import base64
            return base64.b64decode(args[1]).decode()
        elif op == "hex_to_ascii":
            if len(args) < 2:
                return "Usage: convert hex_to_ascii <hex>"
            try:
                return bytes.fromhex(args[1]).decode()
            except:
                return "Invalid hex"
        elif op == "ascii_to_hex":
            if len(args) < 2:
                return "Usage: convert ascii_to_hex <text>"
            return args[1].encode().hex()
        return f"Unknown convert op: {op}"

    # ---- Date/Time ----
    def handle_date(self, args):
        if not args:
            return f"Current date: {dt_datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        op = args[0].lower()
        if op == "now":
            return f"{dt_datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        elif op == "format":
            if len(args) < 2:
                return "Usage: date format <pattern>"
            try:
                return dt_datetime.now().strftime(args[1])
            except:
                return "Invalid format pattern"
        elif op == "diff":
            if len(args) < 3:
                return "Usage: date diff <date1> <date2>"
            try:
                d1 = dt_datetime.strptime(args[1], "%Y-%m-%d")
                d2 = dt_datetime.strptime(args[2], "%Y-%m-%d")
                return f"{abs((d2 - d1).days)} days"
            except:
                return "Invalid date format (use YYYY-MM-DD)"
        return f"Unknown date op: {op}"

    # ---- Hash ----
    def handle_hash(self, args):
        if not args:
            return "Usage: hash <operation> [text]"
        op = args[0].lower()
        import hashlib
        if op == "md5":
            if len(args) < 2:
                return "Usage: hash md5 <text>"
            return hashlib.md5(args[1].encode()).hexdigest()
        elif op == "sha256":
            if len(args) < 2:
                return "Usage: hash sha256 <text>"
            return hashlib.sha256(args[1].encode()).hexdigest()
        elif op == "sha1":
            if len(args) < 2:
                return "Usage: hash sha1 <text>"
            return hashlib.sha1(args[1].encode()).hexdigest()
        return f"Unknown hash op: {op}"

    # ---- JSON ----
    def handle_json(self, args):
        if not args:
            return "Usage: json <operation> [args...]"
        op = args[0].lower()
        if op == "format":
            if len(args) < 2:
                return "Usage: json format <path>"
            try:
                with open(args[1], "r") as f:
                    data = json_mod.load(f)
                return json_mod.dumps(data, indent=2)
            except Exception as e:
                return f"Error: {e}"
        elif op == "parse":
            if len(args) < 2:
                return "Usage: json parse <json_str>"
            try:
                return json_mod.loads(args[1])
            except:
                return "Invalid JSON"
        return f"Unknown json op: {op}"

    # ---- Grep ----
    def handle_grep(self, args):
        if not args:
            return "Usage: grep <pattern> [file]"
        pattern = args[0]
        filepath = args[1] if len(args) > 1 else None
        try:
            if filepath:
                with open(filepath, "r") as f:
                    lines = f.readlines()
            else:
                lines = sys.stdin.read().splitlines()
            matches = [line for line in lines if re.search(pattern, line)]
            return "\n".join(matches) if matches else "No matches found"
        except Exception as e:
            return f"Error: {e}"

    # ---- File Stats ----
    def handle_stat(self, args):
        if not args:
            return "Usage: stat <path>"
        try:
            path = args[0]
            if os.path.exists(path):
                stat = os.stat(path)
                return f"Size: {stat.st_size} bytes\nModified: {dt_datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M')}\nExists: True"
            return "File not found"
        except Exception as e:
            return f"Error: {e}"


def main():
    agent = CodingAgent()
    parser = argparse.ArgumentParser(description="Python Coding Agent")
    parser.add_argument("input", nargs="*", help="Input command and args")
    args = parser.parse_args()
    input_str = " ".join(args.input) if args.input else ""
    result = agent.run(input_str)
    print(result)


if __name__ == "__main__":
    main()