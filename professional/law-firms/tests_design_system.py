#!/usr/bin/env python3
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
PROFESSIONAL = ROOT.parent
STYLE = PROFESSIONAL / 'styles' / 'legal-editorial'
DESIGN = STYLE / 'DESIGN.md'
TAILWIND = STYLE / 'tailwind.theme.json'
DTCG = STYLE / 'tokens.dtcg.json'
TEMPLATE = ROOT / '_template' / 'legal-firm-template.html'
BATTEN = ROOT / 'batten-sacks' / 'index.html'
README = ROOT / 'README.md'


def read(path):
    try:
        label = path.relative_to(ROOT)
    except ValueError:
        label = path.relative_to(PROFESSIONAL)
    assert path.exists(), f'missing file: {label}'
    return path.read_text()


def test_design_md_exists_and_declares_w230_legal_editorial():
    text = read(DESIGN)
    assert text.startswith('---\n'), 'DESIGN.md must use YAML front matter'
    for required in [
        'version: alpha',
        'name: W230 Legal Editorial',
        'description:',
        'colors:',
        'typography:',
        'components:',
        '## Overview',
        '## Colors',
        '## Typography',
        '## Layout',
        '## Elevation & Depth',
        '## Shapes',
        '## Components',
        "## Do's and Don'ts",
    ]:
        assert required in text, f'missing DESIGN.md marker: {required}'


def test_design_md_encodes_simo_taste_constraints():
    text = read(DESIGN).lower()
    for required in [
        'premium website rebuilds for boutique professional firms',
        'client-intake-first',
        'matter router',
        'proof rail',
        'mobile sticky cta',
        'independent concept disclaimer',
        'purple ai slop',
        'fake luxury',
        'do not invent',
    ]:
        assert required in text, f'missing taste constraint: {required}'


def test_token_exports_exist_and_are_valid_json():
    tailwind = json.loads(read(TAILWIND))
    dtcg = json.loads(read(DTCG))
    assert isinstance(tailwind, dict) and tailwind, 'tailwind export empty'
    assert isinstance(dtcg, dict) and dtcg, 'dtcg export empty'
    encoded = json.dumps(tailwind) + json.dumps(dtcg)
    for token in ['#111111', '#F7F2EA', '#B68A35', '#DDE8EF', '#879B88']:
        assert token.lower() in encoded.lower(), f'token missing from exports: {token}'


def test_template_and_batten_reference_design_contract():
    template = read(TEMPLATE)
    batten = read(BATTEN)
    for html in [template, batten]:
        assert 'DESIGN.md' in html, 'HTML should reference the design contract'
        assert '--w230-ink' in html, 'HTML should expose W230 token variable names'
        assert '--w230-gold' in html, 'HTML should expose W230 token variable names'


def test_readme_documents_design_md_workflow():
    text = read(README)
    for required in [
        '../styles/legal-editorial/DESIGN.md',
        'npx -y @google/design.md lint professional/styles/legal-editorial/DESIGN.md',
        'tailwind.theme.json',
        'tokens.dtcg.json',
        'W230 Legal Editorial',
    ]:
        assert required in text, f'missing README design workflow marker: {required}'


if __name__ == '__main__':
    tests = [v for k, v in globals().items() if k.startswith('test_')]
    for t in tests:
        t()
    print(f'{len(tests)} design system tests passed')
