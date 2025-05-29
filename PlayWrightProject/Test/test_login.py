import pytest
from PlayWrightProject.Pages.Login_Page import LoginPage

def test_login(playwright, launch_browser, credentials):
    page = launch_browser
    login_page = LoginPage(page)
    login_page.navigate(credentials["url"])
    dashboadpage=login_page.login(credentials["username"], credentials["password"])

    # Optional: Validate successful login
    assert page.url != credentials["url"]
