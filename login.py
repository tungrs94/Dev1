import requests

url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php?redirect_to=http%3A%2F%2F45.79.43.178%2Fsource_carts%2Fwordpress%2Fwp-admin%2F&reauth=1'
data = {'log': 'admin', 'pwd': '123456aA'}
with requests.Session() as season:
    resp = season.post(
        url, data=data)
    resp = season.get(url)
data = resp.request.headers.get("Cookie")
print(data[data.find('=') + 1:data.find('%')])