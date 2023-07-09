from behave import given, when, then

@given("this step exists")
def step_impl(context):
    pass


@when("I run {string}")
def step_when(context, string):
    pass


@then("I should see the behave tests run")
def step_then(context):
    pass
