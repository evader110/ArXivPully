import requests
import json

def test_json_output(search_term_one, search_term_two, num_articles_one, num_articles_two):
    # Testing Server was run on Gunicorn on localhost with port 8000
    url = f'http://localhost:8000/api/query?{search_term_one}={num_articles_one}&{search_term_two}={num_articles_two}'

    data = json.loads(requests.get(url).json())

    # Check for all available properties in json output
    assert 'title' in data[search_term_one][0], 'No titles were given'
    assert 'body' in data[search_term_one][0], 'No bodies were given'
    assert 'link' in data[search_term_one][0], 'No links were given'
    assert 'title' in data[search_term_two][0], 'No titles were given'
    assert 'body' in data[search_term_two][0], 'No bodies were given'
    assert 'link' in data[search_term_two][0], 'No links were given'
    # Check that Search term is a key in the output
    assert search_term_one in data, f'No {search_term_one} articles given'
    assert search_term_two in data, f'No {search_term_two} articles given'
    # Check that the number of articles you recieved are correect
    assert len(data[search_term_one]) == num_articles_one, f'We did not get {num_articles_one} articles, instead we got {len(data[search_term_one])}'
    assert len(data[search_term_two]) == num_articles_two, f'We did not get {num_articles_two} articles, instead we got {len(data[search_term_two])}'
    # All tests passed, return success
    return True

assert test_json_output('clustering', 'artifiicial intelligence', 10, 5), 'json output is no longer correct'