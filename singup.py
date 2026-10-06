from playwright.sync_api import Page


class SignupPage:

    def __init__(self, page: Page):
        self.page = page

        self.name_input = page.get_by_label("Name")
        self.email_input = page.get_by_label("Email")
        self.password_input = page.get_by_label("Password")
        self.confirm_password_input = page.get_by_label("Confirm Password")
        self.signup_button = page.get_by_role("button", name="Sign Up")

    def open(self, url):
        self.page.goto(url)

    def signup(self, name, email, password, confirm_password):

        self.name_input.fill(name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.confirm_password_input.fill(confirm_password)

        self.signup_button.click()