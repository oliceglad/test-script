import sys
from collections import defaultdict

def read_config(config):
    replacements = {}
    with open(config, "r") as f:
        for line in f:
            key,value = line.strip().split('=')
            replacements[key] = value

    return replacements

def process_text(text, replacements):
    with open(text, 'r') as f:
        lines = f.readlines()

    changed_lines = []
    for line in lines:
        original_line = line
        for key, value in replacements.items():
            line = line.replace(key,value)
        num_replacements = sum(original_line.count(key) for key in replacements.keys())
        changed_lines.append((line.strip(), num_replacements))

    changed_lines.sort(key=lambda x: x[1], reverse=True)
    return changed_lines

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <config_file> <text_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    text_file = sys.argv[2]

    replacements = read_config(config_file)
    changed_lines =  process_text(text_file, replacements)

    for line, _ in changed_lines:
        print(line)

if __name__ == "__main__":
    main()
