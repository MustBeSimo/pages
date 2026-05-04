#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
HTML = (ROOT / 'batten-sacks' / 'index.html').read_text()


def assert_contains(text):
    assert text in HTML, f"missing: {text}"


def test_hero_promises_client_outcome_not_architecture():
    assert_contains('Clients arrive confused. They should leave booked.')
    assert 'clearer front door' not in HTML.lower()


def test_public_proof_signals_are_visible_but_marked_as_source_claims():
    for text in ['4.9', '191 Google reviews', '100+ years combined experience', 'Law Institute Victoria', 'Migration Institute of Australia', 'PEXA']:
        assert_contains(text)
    assert_contains('Proof signals from original public website')


def test_buying_property_router_is_a_real_interactive_path():
    for text in ['data-router-option="buying-property"', 'Buying property flow', 'Are you buying or selling?', 'Contract reviewed yet?', 'Generate next step', 'Your conveyancing pathway']:
        assert_contains(text)
    assert re.search(r'function\s+updatePropertyPath\s*\(', HTML), 'missing interactive router function'
    assert '#services' not in re.search(r'<section[^>]+id="top".*?</section>|<header.*?</header>', HTML, re.S).group(0), 'hero router should not just anchor to services'


def test_four_decisions_remain_primary_architecture_not_six_equal_cards():
    assert_contains('property-flow')
    assert_contains('decision-architecture')
    # Practice list can exist, but not as six equal numbered tiles immediately contradicting router.
    assert 'practice-grid' not in HTML
    assert '01</small><h3>Conveyancing' not in HTML


def test_no_spelling_jab_or_condescending_copy():
    bad = ['spelling', 'Ligitation', 'typo', 'cleaned up']
    lowered = HTML.lower()
    for word in bad:
        assert word.lower() not in lowered, f'condescending/jab copy present: {word}'


def test_mobile_first_demo_and_sticky_bar_present():
    for text in ['mobile-demo', '15-second mobile flow', 'mobile-bar', 'Book review', 'Call now']:
        assert_contains(text)


def test_concept_handoff_is_mocked_not_hedged():
    assert 'For a live client site, this section would connect' not in HTML
    for text in ['Mock intake', 'Preferred contact method', 'Matter type', 'Book a contract review']:
        assert_contains(text)

if __name__ == '__main__':
    tests = [v for k,v in globals().items() if k.startswith('test_')]
    for t in tests:
        t()
    print(f'{len(tests)} law preview tests passed')
