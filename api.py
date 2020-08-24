import requests

def get_data():
    url = 'https://3b2636638658e577e50c02e4c7268850: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@tungrs94.myshopify.com/admin/api/2020-07/customers.json'
    # url = 'https://3b2636638658e577e50c02e4c7268850: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@tungrs94.myshopify.com/admin/api/2020-07/orders.json'
    r = requests.get(url)
    return r.json()

print(get_data())