from plugins.helper.api_helper import get_order_data_from_api


def extract(date):
    order_date = get_order_data_from_api(date)
    returns = f"Extract: {order_date}, table: order"
    return returns

def transform():

    return f"Transform order"

def load():
    return f"Load order"


