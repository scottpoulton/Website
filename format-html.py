import re

def pretty_indent(html):
    # This does NOT parse HTML fully, just does a "visual" indent
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
    with open(filename.replace('.html', '.pretty.html'), 'w') as out:
        out.write(pretty)

# USAGE: change 'yourfile.html' below!
process_file('public/about/index.html')