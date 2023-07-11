from ..base import BasePlaywrightTestCase


class TestAddSalary(BasePlaywrightTestCase):
    def test_add_salary(self):
        print("running test boy")
        self.page.goto(f"{self.live_server_url}/")
        self.page.goto(f"{self.live_server_url}/test/")
        self.page.goto(f"{self.live_server_url}/")
