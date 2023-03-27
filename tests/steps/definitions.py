from behave import given, when, then
from playwright.sync_api import expect


@given("this step exists")
def step_impl(context):
    # assert Playwright navigates to context url
    context.page.goto(context.base_url)
    context.test.assertIn(context.base_url, context.page.url)


@when("I run {string}")
def step_when(context, string):
    pass


@then("I should see the behave tests run")
def step_then(context):
    pass
