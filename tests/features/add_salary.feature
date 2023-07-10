Feature: Add income and expense

  Scenario: Adding basic income and expense info
    Given I am on the home page
    When I add an income of "100"
    Then I should see "100" in the monthly budget remaining section
    When I add an expense of "50"
    Then I should see "50" in the monthly budget remaining section