from plugins.helper.api_helper import get_order_data_from_api


def extract(date):
    order_date = get_order_data_from_api(date)
    return f"Extract: {order_date}, order_detail"

def transform():
    return f"Transform order_detail"

def load():
    return f"Load order_detail"


