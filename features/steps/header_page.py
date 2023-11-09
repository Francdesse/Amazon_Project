from behave import given, when, then


@when('user searches for {search_item}')
def user_searches_for_airpods(context, search_item):
    context.app.header_page.user_searches_for_airpods(search_item)


@when('clicks on search button')
def user_clicks_search_btn(context):
    context.app.header_page.user_clicks_search_btn()


@then('verify that user sees {expected_result}')
def user_sees_airpods_in_search_results(context, expected_result):
    context.app.header_page.user_sees_airpods_in_search_results(expected_result)