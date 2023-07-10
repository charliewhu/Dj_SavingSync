from behave import given, when, then
from playwright.sync_api import expect


@given("this step exists")
def step_impl(context):
    pass


@when("I run {string}")
def step_when(context, string):
    pass


@then("I should see the behave tests run")
def step_then(context):
    pass


@given("I am on the home page")
def step_impl(context):
    raise NotImplementedError("STEP: Given I am on the home page")


@when('I add an income of "{amount}"')
def step_impl(context, amount):
    raise NotImplementedError('STEP: When I add an income of "100"')


@then('I should see "{amount}" in the monthly budget remaining section')
def step_impl(context, amount):
    raise NotImplementedError(
        'STEP: Then I should see "100" in the monthly budget remaining section'
    )


@when('I add an expense of "{amount}"')
def step_impl(context, amount):
    raise NotImplementedError('STEP: When I add an expense of "50"')
