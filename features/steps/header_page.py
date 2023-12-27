from behave import given, when, then


@when('user searches for {search_item}')
def user_searches_for_airpods(context, search_item):
    context.app.header_page.user_searches_for_airpods(search_item)


@when('clicks on search button')
def user_clicks_search_btn(context):
    context.app.header_page.user_clicks_search_btn()


@when('clicks on go to cart button')
def user_clicks_on_cart(context):
    context.app.header_page.user_clicks_on_cart()


@then('verify that user sees {expected_result}')
def user_sees_airpods_in_search_results(context, expected_result):
    context.app.cart_page.user_sees_airpods_in_search_results(expected_result)


@then('Verify the on the number cart updates to {1}')
def num_on_cart_item(context, cart_numb):
    context.app.header_page.num_on_cart_item(cart_numb)