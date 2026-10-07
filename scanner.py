import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser(description="Simple Port Scanner")
parser.add_argument("target", help="Target IP address")
parser.add_argument("-s", "--start", type=int, default=1, help="Start port")
parser.add_argument("-e", "--end", type=int, default=1024, help="End port")
parser.add_argument("-o", "--output", help="Save results to file")
args = parser.parse_args()

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((args.target, port))
    s.close()
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except OSError:
            service = "unknown"
        print(f"Port {port} is open ({service})")
        if args.output:
            with open(args.output, "a") as f:
                f.write(f"Port {port} is open ({service})\n")

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(args.start, args.end + 1))

print("Scan complete")