from ..base import BasePlaywrightTestCase


class TestAddSalary(BasePlaywrightTestCase):
    def test_add_salary(self):
        """
        Given I am on the home page
        When I add an income of "100"
        Then I should see "100" in the monthly budget remaining section
        When I add an expense of "50"
        Then I should see "50" in the monthly budget remaining section
        """

        self.page.goto(f"{self.live_server_url}/")

        self.page.locator('select[name="cashflow"]').select_option(label="Income")
        self.page.locator('select[name="type"]').select_option(label="Salary")
        self.page.get_by_placeholder("Name").fill("Salary")
        self.page.get_by_placeholder("Amount").fill(100)
        self.page.get_by_role("button", name="add").click()

        assert self.page.get_by_placeholder("Name").inner_text() == ""
        assert self.page.get_by_test_id("monthly-balance").inner_text() == "100"
        assert self.page.get_by_test_id("income-list-item").count() == 1

        self.page.locator('select[name="cashflow"]').select_option(label="Expense")
        self.page.locator('select[name="type"]').select_option(label="Regular Bill")
        self.page.get_by_placeholder("Name").fill("Phone")
        self.page.get_by_placeholder("Amount").fill(50)
        self.page.get_by_role("button", name="add").click()

        assert self.page.get_by_placeholder("Name").inner_text() == ""
        assert self.page.get_by_test_id("monthly-balance").inner_text() == "50"
        assert self.page.get_by_test_id("expense-list-item").count() == 1
