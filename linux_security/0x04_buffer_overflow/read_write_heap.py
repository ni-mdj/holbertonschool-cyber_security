#!/usr/bin/python3
"""Find and replace an ASCII string in the heap of a running process."""

import sys


def usage_exit():
    """Print usage on stdout and exit with status 1."""
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)


def parse_heap_bounds(pid):
    """Return (heap_start, heap_end) from /proc/<pid>/maps."""
    maps_path = f"/proc/{pid}/maps"
    with open(maps_path, "r", encoding="utf-8") as maps_file:
        for line in maps_file:
            if "[heap]" not in line:
                continue
            region = line.split()[0]
            start_s, end_s = region.split("-")
            return int(start_s, 16), int(end_s, 16)
    raise RuntimeError("Heap not found")


def main():
    """Program entry point."""
    if len(sys.argv) != 4:
        usage_exit()

    pid_s, search_s, replace_s = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        pid = int(pid_s)
        if pid <= 0:
            raise ValueError
    except ValueError:
        usage_exit()

    try:
        search_b = search_s.encode("ascii")
        replace_b = replace_s.encode("ascii")
    except UnicodeEncodeError:
        usage_exit()

    if len(search_b) == 0 or len(replace_b) > len(search_b):
        usage_exit()

    try:
        heap_start, heap_end = parse_heap_bounds(pid)
        mem_path = f"/proc/{pid}/mem"
        payload = replace_b + (b"\x00" * (len(search_b) - len(replace_b)))

        with open(mem_path, "rb+") as mem_file:
            mem_file.seek(heap_start)
            heap_data = mem_file.read(heap_end - heap_start)
            offset = heap_data.find(search_b)
            if offset == -1:
                print("String not found in heap")
                return

            write_addr = heap_start + offset
            mem_file.seek(write_addr)
            mem_file.write(payload)

            print(f"Heap: {hex(heap_start)}-{hex(heap_end)}")
            print(f"Found at: {hex(write_addr)}")
            print(f"Replaced '{search_s}' with '{replace_s}'")
    except FileNotFoundError:
        print("Process not found")
        sys.exit(1)
    except PermissionError:
        print("Permission denied")
        sys.exit(1)
    except RuntimeError as err:
        print(err)
        sys.exit(1)


if __name__ == "__main__":
    main()
