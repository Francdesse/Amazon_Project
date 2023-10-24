from behave import given, when, then


@given('user navigates to Amazon website')
def user_nav_to_Amz_website(context):
    context.app.main_page.user_nav_to_Amz_website()