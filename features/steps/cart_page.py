from behave import given, when, then
from time import sleep


@then("Verify the added {expected_result} is in cart")
def item_is_in_cart(context, expected_result):
    context.app.cart_page.item_is_in_cart(expected_result)