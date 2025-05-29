
from PlayWrightProject.Pages.Dashboard_Page import DashboardPage


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def login(self, username, password):
        username_input = self.page.locator('input[name="username"]')
        password_input = self.page.locator('input[name="password"]')
        login_button = self.page.locator('button[type="submit"]')

        username_input.fill(username)
        password_input.fill(password)
        login_button.click()
        return DashboardPage(self.page)
