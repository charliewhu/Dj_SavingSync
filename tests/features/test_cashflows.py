from ..base import BasePlaywrightTestCase

from playwright.sync_api import expect

from model_bakery import baker
from src.cashflows.models import Cashflow

expect.set_options(timeout=500)


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

        income_item = {
            "name": "Salary",
            "amount": "100",
        }

        expense_item = {
            "name": "Phone",
            "amount": "50",
        }

        self.page.locator('select[name="type"]').select_option(label="Income")
        self.page.locator('select[name="source"]').select_option(label="Salary")
        self.page.locator('input[name="name"]').fill(income_item["name"])
        self.page.locator('input[name="amount"]').fill(income_item["amount"])
        self.page.get_by_role("button", name="add").click()

        expect(self.page.locator('input[name="name"]')).to_have_value("")
        expect(self.page.get_by_test_id(self.income_list_item_id)).to_have_count(1)
        expect(self.page.get_by_test_id("income-list-item")).to_contain_text(
            income_item["name"]
        )
        expect(self.page.get_by_test_id("income-list-item")).to_contain_text(
            income_item["amount"]
        )

        self.page.locator('select[name="type"]').select_option(label="Expense")
        self.page.locator('select[name="source"]').select_option(label="Regular Bill")
        self.page.locator('input[name="name"]').fill(expense_item["name"])
        self.page.locator('input[name="amount"]').fill(expense_item["amount"])
        self.page.get_by_role("button", name="add").click()

        expect(self.page.locator('input[name="name"]')).to_have_value("")
        expect(self.page.get_by_test_id("expense-list-item")).to_have_count(1)
        expect(self.page.get_by_test_id("expense-list-item")).to_contain_text(
            expense_item["name"]
        )
        expect(self.page.get_by_test_id("expense-list-item")).to_contain_text(
            expense_item["amount"]
        )

    def test_delete(self):
        """
        Given I have 1 existing cashflow
        And I am on the home page
        When I delete the cashflow
        Then I should not see any cashflows
        """

        baker.make(_model=Cashflow, type="income")
        self.page.goto(f"{self.live_server_url}/")

        cashflow_item = self.page.get_by_test_id(self.income_list_item_id)
        expect(cashflow_item).to_have_count(1)

        self.page.get_by_role("button", name="delete").click()

        expect(self.page).to_have_url(f"{self.live_server_url}/")
        expect(cashflow_item).to_have_count(0)

    def test_milestones(self):
        """
        Given I have an existing Income Cashflow of 200
        And I have and existing Expense Cashflow of 100
        And I am on the home page
        Then I should see a monthly balance of 100
        And I should see a biannual balance of 600
        And I should see an annual balance of 1200
        """

        baker.make(Cashflow, type="income", amount=200)
        baker.make(Cashflow, type="expense", amount=100)
        self.page.goto(f"{self.live_server_url}/")

        expect(self.page.get_by_test_id("monthly-balance")).to_contain_text("100")
        expect(self.page.get_by_test_id("biannual-balance")).to_contain_text("600")
        expect(self.page.get_by_test_id("annual-balance")).to_contain_text("1200")


# TODO: Model: Add categories Needs / Wants / Savings to Cashflow
# TODO: UI/UX: Salary/Income could be radio buttons
# TODO: Model: add Irregular Expense as Cashflow source
