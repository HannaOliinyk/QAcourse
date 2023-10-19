import pytest
import requests
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 50
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_classroom_can_be_found(assigment_id):
    github_api = GitHub()
    r = github_api.classroom_assigment(assigment_id)()
    print(r)
    assert 'assigment_id' not in r

@pytest.mark.api
def test_get_emojis_status_code(emojis_fixture):
    assert emojis_fixture.status_code == 200

@pytest.mark.api
def test_get_emojis_response_data(emojis_fixture):
    emojis_data = emojis_fixture.json()
    assert "+1" in emojis_data