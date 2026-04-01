#!/usr/bin/python3
# Lit la zone heap d'un process et remplace une chaîne ASCII par une autre."""
import sys


def usage():
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)


if len(sys.argv) != 4:
    usage()

pid_arg = sys.argv[1]
search = sys.argv[2]
replace = sys.argv[3]

try:
    pid = int(pid_arg)
    if pid <= 0:
        raise ValueError
except ValueError:
    usage()

try:
    search_b = search.encode("ascii")
    replace_b = replace.encode("ascii")
except UnicodeEncodeError:
    usage()

if len(search_b) == 0 or len(replace_b) > len(search_b):
    usage()

maps_path = "/proc/{}/maps".format(pid)
mem_path = "/proc/{}/mem".format(pid)
heap_start = None
heap_end = None

try:
    with open(maps_path, "r", encoding="utf-8") as maps_file:
        for line in maps_file:
            if "[heap]" in line:
                addr = line.split()[0]
                start, end = addr.split("-")
                heap_start = int(start, 16)
                heap_end = int(end, 16)
                break
except FileNotFoundError:
    print("Process not found")
    sys.exit(1)
except PermissionError:
    print("Permission denied")
    sys.exit(1)

if heap_start is None or heap_end is None:
    print("Heap not found")
    sys.exit(1)

payload = replace_b + b"\x00" * (len(search_b) - len(replace_b))

try:
    with open(mem_path, "rb+") as mem_file:
        mem_file.seek(heap_start)
        heap_data = mem_file.read(heap_end - heap_start)
        index = heap_data.find(search_b)

        if index == -1:
            print("String not found in heap")
            sys.exit(0)

        target = heap_start + index
        mem_file.seek(target)
        mem_file.write(payload)

        print("Done")
        print("Heap:", hex(heap_start), "-", hex(heap_end))
        print("Address:", hex(target))
except FileNotFoundError:
    print("Process not found")
    sys.exit(1)
except PermissionError:
    print("Permission denied")
    sys.exit(1)
