import os
import re

def pretty_indent(html):
    # Simple visual parser - not a true HTML parser!
    indent_level = 0
    output = []
    tag_regex = re.compile(r'(</?[^>]+>)')

    for line in html.splitlines():
        parts = tag_regex.split(line)
        for part in parts:
            if part.startswith('</'):
                indent_level -= 1
            if part.strip():
                output.append('  ' * max(indent_level,0) + part.strip())
            if part.startswith('<') and not part.startswith('</') and not part.endswith('/>') and not part.startswith('<!'):
                indent_level += 1
    return '\n'.join(output)

def process_file(filename):
    with open(filename) as f:
        html = f.read()
    pretty = pretty_indent(html)
    out_filename = filename.replace('.html', '.pretty.html')
    with open(out_filename, 'w') as out:
        out.write(pretty)
    print(f'Processed: {filename} -> {out_filename}')

def process_folder(folder):
    for root, _, files in os.walk(folder):
        for name in files:
            if name.endswith('.html'):
                process_file(os.path.join(root, name))

# USAGE: Run from your repo root
if __name__ == "__main__":
    process_folder('public')