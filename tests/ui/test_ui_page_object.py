from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.sign_in_page import NovaPost
import pytest

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.try_login("page_object@gmail.com", "wrong password")
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    sign_in_page.close()

@pytest.mark.ui
def test_check_incorrect_parcel_of_nova_poshta():
    sign_in_page = NovaPost()
    sign_in_page.go_to()
    sign_in_page.try_search_invoice("45600000034189")
    assert sign_in_page.check_title("Трекінг посилки | Nova Global")
    sign_in_page.close()