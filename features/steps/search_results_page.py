from behave import given, when, then
from time import sleep


@when('clicks on first item')
def clicks_on_first_item(context):
    context.app.search_results_page.clicks_on_first_item()


@when('saves search item name')
def save_item_name(context):
    context.app.search_results_page.save_item_name()


@then('verify the title contains {search_item}')
def item_open_to_product_page(context, search_item):
    context.app.search_results_page.item_open_to_product_page(search_item)


@then('Verify the added to cart message')
def verify_add_to_crt_message(context):
    context.app.item_added_to_cart_message_page.verify_add_to_crt_message()