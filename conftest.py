import pytest
from modules.api.clients.github import GitHub
class User:
    
    def __init__(self) -> None:
        self.name = None
        self.second_name = None
    
    def create(self):
        self.name = 'Sergii'
        self.second_name = 'Butenko'
    
    def remove(self):
        self.name = ''
        self.second_name = ''
    
@pytest.fixture
def user():
        user = User()
        user.create()

        yield user

        user.remove()

@pytest.fixture
def github_api():
     api = GitHub()
     yield api

@pytest.fixture
def assigment_id():
    return '12'

@pytest.fixture
def emojis_fixture():
    github = GitHub()
    emojis_response = github.get_emojis()
    return emojis_response