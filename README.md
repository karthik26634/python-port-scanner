# python-port-scanner
# Python Port Scanner

Multithreaded TCP port scanner built with Python.

## Features
- Scans a port range on a target IP
- Detects service names
- Multithreading for fast scans
- Command-line options (argparse)
- Saves results to a file

## Requirements
- Python 3

## Usage
```
python scanner.py <target> -s <start_port> -e <end_port> -o <output_file>
```

Example:
```
python scanner.py 127.0.0.1 -s 1 -e 1024 -o results.txt
```

## Sample Output
```
Port 135 is open (epmap)
Port 445 is open (microsoft-ds)
Scan complete
```

## Disclaimer
For educational use only. Scan only systems you own or have permission to test.
