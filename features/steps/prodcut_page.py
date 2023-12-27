from behave import given, when, then
from time import sleep


@when('clicks on add to cart button')
def user_clicks_on_add_to_cart(context):
    context.app.product_page.user_clicks_on_add_to_cart()


@when('user clicks no thanks on order pop up page')
def user_click_no_thanks(context):
    context.app.product_page.user_click_no_thanks()