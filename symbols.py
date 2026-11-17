import re
def classes(text):
    return [(m.group(1),m.start(1)) for m in re.finditer(r'\bclass\s+([A-Za-z_][A-Za-z0-9_]*)',text)]
