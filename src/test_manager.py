import os, json

from src.test import Test


def get_tests():
    tests = {}
    files = [file for file in os.listdir('../tests/') if file.endswith('.json')]
    for file in files:
        name = os.path.splitext(file)[0]
        with open('../tests/' + file) as site_tests:
            site_tests = json.load(site_tests)
            tests[site_tests['url']] = []
            sequence = site_tests['sequence']
            for i in sorted(sequence):
                tests[site_tests['url']].append(get_test(name, sequence[i], site_tests['url']))
    return tests


def get_test(site_name, test_name, test_url):
    file = None
    # check if the file exists in the site scope
    if os.path.isfile('../tests/' + site_name + '/' + test_name + '.json'):
        file = '../tests/' + site_name + '/' + test_name + '.json'
    elif os.path.isfile('../tests/base/' + test_name + '.json'):  # fallback
        file = '../tests/base/' + test_name + '.json'
    with open(file) as file:
        test = json.load(file)
        return Test(test_name, test['events'], test['expected_result'], test_url)
