"""Login page smoke and validation tests."""

import pytest
from playwright.sync_api import Page, expect

from framework.config import Settings
from framework.pages.login_page import LoginPage
from framework.pages.requester_page import RequesterPage


@pytest.fixture
def requester_page(page: Page, settings: Settings) -> RequesterPage:
    return RequesterPage(page, settings).open()


@pytest.fixture
def login_page(requester_page: RequesterPage) -> LoginPage:
    return requester_page.open_login()


@pytest.mark.smoke
def test_requester_page_loads(page: Page, settings: Settings):
    requester_page = RequesterPage(page, settings).open()

    expect(page).to_have_title('All2Build')
    expect(requester_page.page_heading).to_be_visible()


@pytest.mark.smoke
def test_login_modal_opens(login_page: LoginPage):
    expect(login_page.heading).to_be_visible()
    expect(login_page.mobile_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.submit_button).to_be_visible()


def test_empty_login_shows_required_field_errors(login_page: LoginPage):
    login_page.submit()

    expect(login_page.mobile_required_message).to_be_visible()
    expect(login_page.password_required_message).to_be_visible()


def test_password_visibility_can_be_toggled(login_page: LoginPage):
    assert login_page.password_input_type() == 'password'

    login_page.toggle_password_visibility()
    expect(login_page.password_input).to_have_attribute('type', 'text')

    login_page.toggle_password_visibility()
    expect(login_page.password_input).to_have_attribute('type', 'password')


def test_forgot_password_and_signup_controls_are_visible(
    login_page: LoginPage,
):
    expect(login_page.forgot_password_button).to_be_visible()
    expect(login_page.signup_button).to_be_visible()

123
 