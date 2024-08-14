#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_statistics():
    """Prints the statistics computed so far."""
    global total_file_size, status_code_counts

    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handles keyboard interruption (Ctrl + C) to print statistics."""
    print_statistics()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Try to parse the line
        parts = line.split()

        # Check if the line matches the expected format
        if len(parts) < 9:
            continue

        ip_address = parts[0]
        date = parts[3][1:]
        request = parts[5] + " " + parts[6] + " " + parts[7]
        status_code = parts[8]
        try:
            file_size = int(parts[9])
        except ValueError:
            continue

        if not request.startswith('"GET'):
            continue

        # Update total file size
        total_file_size += file_size

        # Update status code counts
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except Exception as e:
    print(f"Error: {e}")

finally:
    # Print final statistics
    print_statistics()

