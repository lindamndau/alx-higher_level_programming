#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    final_count = 0
    for i in range(len(sys.argv) - 1):
        final_count += int(sys.argv[i + 1])
    print("{}".format(final_count))
