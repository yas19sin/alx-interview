#!/usr/bin/python3
"""
Log parsing script
"""
import sys


def print_stats(current_total_size, current_status_codes):
    """Prints the computed statistics"""
    print("File size: {}".format(current_total_size))
    for code in sorted(current_status_codes.keys()):
        if current_status_codes[code] > 0:
            print("{}: {}".format(code, current_status_codes[code]))


total_size = 0
status_codes = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}
num_valid_lines_processed = 0
program_interrupted = False

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        is_line_valid_and_processed = False
        try:
            if not (len(parts) == 9 and
                    parts[4] == '"GET' and
                    parts[5] == '/260' and
                    parts[6] == 'HTTP/1.1"'):
                pass
            else:
                status_code = int(parts[7])
                file_size = int(parts[8])

                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                is_line_valid_and_processed = True
        except (ValueError, IndexError):
            pass

        if not is_line_valid_and_processed:
            continue

        num_valid_lines_processed += 1

        if num_valid_lines_processed > 0 and \
                num_valid_lines_processed % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    program_interrupted = True
    print_stats(total_size, status_codes)
    raise

finally:
    if not program_interrupted and \
       num_valid_lines_processed > 0 and \
       (num_valid_lines_processed % 10 != 0):
        print_stats(total_size, status_codes)
