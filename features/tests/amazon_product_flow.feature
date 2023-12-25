Feature: user is able to successful buy item from store

  Scenario: verify user is able to search an item
    Given user navigates to Amazon website
    When user searches for airpods
    And clicks on search button
    Then verify that user sees "airpods"

  Scenario: verify user is able to click an item
    Given user navigates to Amazon website
    When user searches for airpods
    And clicks on search button
    And clicks on first item
    And saves search item name
    Then verify the title contains AirPods

  Scenario: verify user is able to add item to cart
    Given user navigates to Amazon website
    When user searches for airpods
    And clicks on search button
    And clicks on first item
    And clicks on add to cart button
    Then Verify the added to cart message

  Scenario: verify that item is in cart after user add item to cart
    Given user navigates to Amazon website
    When user searches for airpods
    And clicks on search button
    And clicks on first item
    And clicks on add to cart button
    And clicks on go to cart button
    Then Verify the added AirPods is in cart

  Scenario: verify when user add items to cart the number in cart updates
    Given user navigates to Amazon website
    When user searches for airpods
    And clicks on search button
    And clicks on first item
    And clicks on add to cart button
    Then Verify the on the number cart updates

