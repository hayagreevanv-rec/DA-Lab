# to_uppercase.py
import sys

def main():
    for line in sys.stdin:
        # Process each line from stdin
        fields = line.strip().split('\t')
        if len(fields) > 1:
            fields[1] = fields[1].upper()  # Convert the second field to uppercase
        print('\t'.join(fields))

if __name__ == "__main__":
    main()
