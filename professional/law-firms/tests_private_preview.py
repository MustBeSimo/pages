#!/usr/bin/env python3
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
SLUG = 'eastern-suburbs-legal'
PREVIEW = ROOT / SLUG
HTML_PATH = PREVIEW / 'index.html'
LEAD_PATH = PREVIEW / 'lead.json'
DATA_PATH = ROOT / '_data' / 'leads.json'
STYLE_PATH = '../styles/legal-editorial/DESIGN.md'

BLOCKED_IDENTIFIERS = [
    'Boutique Legal',
    'Trent Harris',
    'boutique.legal',
    'boutique@boutique.legal',
    '9808 6396',
]


def read(path):
    assert path.exists(), f'missing file: {path.relative_to(ROOT)}'
    return path.read_text()


def test_private_preview_files_exist_and_are_anonymized():
    html = read(HTML_PATH)
    lead = read(LEAD_PATH)
    joined = html + lead
    assert 'Eastern Suburbs Legal Studio' in html
    assert 'Independent W230 concept preview' in html
    assert 'not affiliated' in html.lower()
    for blocked in BLOCKED_IDENTIFIERS:
        assert blocked.lower() not in joined.lower(), f'exact target identifier leaked: {blocked}'


def test_private_preview_has_required_safety_and_style_contract():
    html = read(HTML_PATH)
    assert '<meta name="robots" content="noindex,nofollow"' in html
    assert STYLE_PATH in html
    for token in ['--w230-ink', '--w230-ivory', '--w230-paper', '--w230-gold', '--w230-muted']:
        assert token in html
    assert 'no fake testimonials' not in html.lower(), 'public page should not sound like internal checklist'
    assert 'mobile app' not in html.lower(), 'preview must not imply W230 is selling/building an app'
    assert 'Responsive mobile website view' in html


def test_private_preview_uses_client_router_not_internal_taxonomy():
    html = read(HTML_PATH)
    for text in [
        'Choose the situation. Then show the next legal step.',
        'data-router-option="buying-property"',
        'data-router-option="will-estate"',
        'data-router-option="lease-dispute"',
        'Generate pathway',
        'Your next-step pathway',
    ]:
        assert text in html, f'missing router marker: {text}'
    assert re.search(r'function\s+updatePathway\s*\(', html), 'missing interactive pathway function'


def test_private_preview_is_not_batten_sacks_reskin():
    html = read(HTML_PATH)
    for forbidden in ['hero-grid', 'hero-card', 'class="proof"', 'mobile-demo', 'phonebar']:
        assert forbidden not in html, f'preview still uses Batten-style structural marker: {forbidden}'
    for required in ['casefile-layout', 'triage-board', 'source-tape', 'decision-dock', 'briefing-column']:
        assert required in html, f'missing distinct layout marker: {required}'
    assert 'W230 Casefile' in html


def test_private_preview_has_editorial_images_not_text_only_or_fake_people():
    html = read(HTML_PATH)
    for required in [
        'visual-evidence-wall',
        'visual-client-journey',
        'legal-image-card',
        '<img ',
        'alt="Abstract legal document stack and intake pathway"',
        'alt="Responsive website preview on a phone beside case notes"',
    ]:
        assert required in html, f'missing image/visual marker: {required}'
    assert html.count('<img ') >= 2, 'preview needs at least two real image elements, not just decorative CSS'
    for unsafe in ['portrait', 'headshot', 'lawyer photo', 'team photo', 'stock people']:
        assert unsafe not in html.lower(), f'avoid fake people imagery: {unsafe}'


def test_private_preview_has_dynamic_motion_layer_with_graceful_fallback():
    html = read(HTML_PATH)
    for required in [
        'motion-hero',
        'case-motion-video',
        '<video ',
        'autoplay muted loop playsinline',
        'assets/casefile-motion.mp4',
        'data-parallax',
        'parallax-layer',
        'IntersectionObserver',
        'prefers-reduced-motion: reduce',
        'reveal-on-scroll',
        'const prefersReducedMotion',
    ]:
        assert required in html, f'missing motion/parallax marker: {required}'
    assert (PREVIEW / 'assets' / 'casefile-motion.mp4').exists(), 'missing motion video asset'
    assert html.count('data-parallax') >= 3, 'needs layered parallax, not one decorative transform'
    assert html.count('reveal-on-scroll') >= 4, 'needs multiple graceful scroll reveals'
    for unsafe in ['controls autoplay', 'soundtrack', 'audio autoplay']:
        assert unsafe not in html.lower(), f'avoid intrusive video/audio behavior: {unsafe}'


def test_private_preview_keeps_public_facts_generic_and_no_outreach():
    lead = json.loads(read(LEAD_PATH))
    data = json.loads(read(DATA_PATH))
    assert lead['slug'] == SLUG
    assert lead['display_name'] == 'Eastern Suburbs Legal Studio'
    assert lead['source_lead_rank'] == 1
    assert lead['status'] == 'private_preview_built_no_outreach'
    assert lead['outreach_sent'] is False
    assert any(item.get('slug') == SLUG for item in data), '_data/leads.json missing private preview'


if __name__ == '__main__':
    tests = [v for k, v in globals().items() if k.startswith('test_')]
    for t in tests:
        t()
    print(f'{len(tests)} private preview tests passed')
