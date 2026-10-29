"""Prepare public metadata and a transparent venue-format adapter.

This script does not authenticate or submit to a service. The canonical PDF and
Markdown retain their abstract. Publish.fun receives that same abstract as a
separate metadata field, so only the duplicate body abstract is removed here.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'submissions'
OUT.mkdir(exist_ok=True)
body = (ROOT / 'paper/manuscript.md').read_text(encoding='utf-8')
title = body.splitlines()[0].removeprefix('# ')
before, tail = body.split('## Abstract\n', 1)
abstract, after = tail.split('## 1. Introduction\n', 1)
abstract = abstract.strip()
repo = 'https://github.com/Teylersf/multiscale-reconnection-audit'
adapted = re.sub(r'^## Abstract\n\n.+?(?=\n## )', '', body, count=1, flags=re.M|re.S)
adapted = adapted.replace('../figures/', repo + '/raw/main/figures/')
assert adapted.count('## Abstract') == 0
assert body.count('## Abstract\n') == 1
assert adapted.count('## References\n') == 1
assert len(re.findall(r'^\[\d+\]', body, re.M)) == 9
(OUT / 'manuscript.md').write_text(adapted, encoding='utf-8', newline='\n')
metadata = dict(title=title, abstract=abstract, author='Taylor Kalin',
    orcid='0009-0003-9000-9315', version='1.0.0',
    scientific_code_commit='e3119e6ee98f6d4bfc760a7c851d33f90b3a7d6b',
    code_doi='10.5281/zenodo.23774456',
    keywords=['magnetic reconnection', 'particle energization', 'first passage',
        'regional attribution', 'reproducibility', 'particle-in-cell'],
    repository=repo)
(OUT / 'metadata.json').write_text(json.dumps(metadata, indent=2)+'\n', encoding='utf-8')
receipt = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
    canonical_markdown_sha256=hashlib.sha256(body.encode()).hexdigest(),
    submitted_body_sha256=hashlib.sha256(adapted.encode()).hexdigest(),
    abstract_sha256=hashlib.sha256(abstract.encode()).hexdigest(),
    transformations=['Remove duplicate body abstract; identical abstract supplied as metadata.',
        'Expand relative figure links to public repository URLs.'],
    all_scientific_body_and_references_preserved=True,
    canonical_abstract_retained=True, reference_count=9)
(OUT / 'publishfun-format-adapter.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print({'title': title, 'abstract_words': len(abstract.split()),
       'body_characters': len(adapted), 'references': 9})
