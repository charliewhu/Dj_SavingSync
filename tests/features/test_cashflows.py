from ..base import BasePlaywrightTestCase

from model_bakery import baker
from src.cashflows.models import Cashflow


class TestCashflows(BasePlaywrightTestCase):
    def setUp(self):
        self.page.goto(f"{self.live_server_url}/")
        self.income_list_item_id = "income-list-item"

    def test_create(self):
        """
        Given I am on the home page
        When I add an income of "100"
        Then I should see "100" in the monthly budget remaining section
        When I add an expense of "50"
        Then I should see "50" in the monthly budget remaining section
        """

        self.page.locator('select[name="type"]').select_option(label="Income")
        self.page.locator('select[name="source"]').select_option(label="Salary")
        self.page.locator('input[name="name"]').fill("Salary")
        self.page.locator('input[name="amount"]').fill("100")
        self.page.get_by_role("button", name="add").click()

        cashflow_item_count = self.page.get_by_test_id(self.income_list_item_id).count

        assert self.page.locator('input[name="name"]').inner_text() == ""
        assert "100" in self.page.get_by_test_id("monthly-balance").inner_text()
        assert cashflow_item_count() == 1

        self.page.locator('select[name="type"]').select_option(label="Expense")
        self.page.locator('select[name="source"]').select_option(label="Regular Bill")
        self.page.locator('input[name="name"]').fill("Phone")
        self.page.locator('input[name="amount"]').fill("50")
        self.page.get_by_role("button", name="add").click()

        assert self.page.locator('input[name="name"]').inner_text() == ""
        assert "50" in self.page.get_by_test_id("monthly-balance").inner_text()
        assert self.page.get_by_test_id("expense-list-item").count() == 1

    def test_delete(self):
        """
        Given I am on the home page
        And I have 1 existing cashflow
        When I delete the cashflow
        Then I should not see any cashflows
        """

        self.cashflow = baker.make(Cashflow)

        cashflow_item_count = self.page.locator(self.income_list_item_id).count

        assert cashflow_item_count() == 1

        self.page.locator('button[name="Delete"]').click()

        assert cashflow_item_count() == 0
