#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SLUG = 'premium-intake-concept'
PREVIEW = ROOT / SLUG
HTML = PREVIEW / 'index.html'

BLOCKED = ['Boutique Legal', 'Trent Harris', 'boutique.legal', '9808 6396']
OLD_MARKERS = ['eastern-suburbs-legal', 'casefile-layout', 'W230 Casefile', 'docket', 'document-stack.svg', 'desktop-briefing-room.svg', 'client-pathway-board.svg']


def read_html():
    assert HTML.exists(), f'missing new standalone route: {HTML.relative_to(ROOT)}'
    return HTML.read_text()


def test_new_route_is_standalone_not_previous_version():
    html = read_html()
    assert 'Premium Intake Counsel — Standalone Concept' in html
    assert 'independent W230 concept' in html
    assert '<meta name="robots" content="noindex,nofollow"' in html
    for marker in OLD_MARKERS:
        assert marker not in html, f'new build still carries previous-version marker: {marker}'
    for blocked in BLOCKED:
        assert blocked.lower() not in html.lower(), f'target identifier leaked: {blocked}'


def test_new_ui_has_functional_matter_router_and_output_panel():
    html = read_html()
    for required in [
        'app-shell',
        'router-workbench',
        'matter-option active',
        'data-matter="property"',
        'data-matter="estate"',
        'data-matter="business"',
        'data-matter="migration"',
        'id="path-title"',
        'id="path-steps"',
        'const matters =',
        'function setMatter',
        'addEventListener',
        'Book the right first conversation',
    ]:
        assert required in html, f'missing functional router marker: {required}'


def test_new_ui_is_premium_black_gold_original_direction():
    html = read_html()
    for required in [
        '--bg:#050505',
        '--gold:#d8ad54',
        '--sage:#8ea18d',
        '--paper:#fff8ea',
        'Find the right legal path before you call',
        'client-situation router',
        'workflow-orbit',
        'intake-card',
        'signal-strip',
        'No fake team photos. No invented awards. No public naming of the source firm.',
    ]:
        assert required in html, f'missing premium original UI marker: {required}'
    assert 'purple' not in html.lower()
    assert 'gavel' not in html.lower()
    assert 'scales of justice' not in html.lower()


def test_new_ui_is_responsive_mobile_ready_and_accessible():
    html = read_html()
    for required in [
        '<meta name="viewport" content="width=device-width, initial-scale=1.0"',
        '@media (max-width: 920px)',
        '@media (max-width: 620px)',
        'grid-template-columns: 1fr',
        'min-height: 48px',
        'touch-action: manipulation',
        'overflow-x: hidden',
        'aria-live="polite"',
        'aria-pressed="true"',
        'prefers-reduced-motion: reduce',
    ]:
        assert required in html, f'missing mobile/accessibility marker: {required}'
    assert re.search(r'font-size:\s*clamp\(3\.2rem,\s*16vw,\s*8\.8rem\)', html), 'headline must fluid-scale on mobile'


if __name__ == '__main__':
    tests = [v for k, v in globals().items() if k.startswith('test_')]
    for t in tests:
        t()
    print(f'{len(tests)} premium intake concept tests passed')
