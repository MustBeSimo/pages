#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
STYLES = ROOT / 'styles'
LEGAL = STYLES / 'legal-editorial'
LAW_FIRMS = ROOT / 'law-firms'


def read(path):
    assert path.exists(), f'missing file: {path.relative_to(ROOT)}'
    return path.read_text()


def test_general_style_registry_exists():
    read(STYLES / 'README.md')
    assert LEGAL.is_dir(), 'legal editorial style should live under professional/styles/'
    for required in ['DESIGN.md', 'tailwind.theme.json', 'tokens.dtcg.json']:
        assert (LEGAL / required).exists(), f'missing legal editorial style artifact: {required}'


def test_legal_editorial_is_reusable_style_not_vertical_contract():
    text = read(LEGAL / 'DESIGN.md')
    assert 'name: W230 Legal Editorial' in text
    assert 'premium website rebuilds for boutique professional firms' in text
    assert 'Legal preview guardrails' not in text, 'style DESIGN.md should not own legal/compliance rules'
    assert 'noindex,nofollow' not in text, 'robots/compliance rules belong in vertical templates/tests'
    assert 'Reply STOP' not in text, 'outreach rules belong outside style tokens'


def test_style_exports_parse_and_include_core_tokens():
    tailwind = json.loads(read(LEGAL / 'tailwind.theme.json'))
    dtcg = json.loads(read(LEGAL / 'tokens.dtcg.json'))
    encoded = json.dumps(tailwind) + json.dumps(dtcg)
    for token in ['#111111', '#F7F2EA', '#B68A35', '#DDE8EF', '#879B88']:
        assert token.lower() in encoded.lower(), f'token missing from style exports: {token}'


def test_law_firms_reference_general_style_registry():
    readme = read(LAW_FIRMS / 'README.md')
    template = read(LAW_FIRMS / '_template' / 'legal-firm-template.html')
    batten = read(LAW_FIRMS / 'batten-sacks' / 'index.html')
    for text in [readme, template, batten]:
        assert '../styles/legal-editorial/DESIGN.md' in text, 'law-firm assets should point to the reusable style registry'
    assert 'Legal preview guardrails' in readme
    assert 'noindex,nofollow' in readme


if __name__ == '__main__':
    tests = [v for k, v in globals().items() if k.startswith('test_')]
    for t in tests:
        t()
    print(f'{len(tests)} style registry tests passed')
