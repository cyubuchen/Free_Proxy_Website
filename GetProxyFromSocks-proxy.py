import requests
import re
import os


# You can run python from the website https://repl.it/languages
# requirements:
# requests==2.21.0


url = 'https://www.socks-proxy.net'
# url = 'https://www.sslproxies.org/'
fp_unchecked = '{0}/{1}.txt'.format(os.getcwd(), 'UnchekedProxySocks-proxy')


def get_index(url):
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15'}
    print('Getting the website...')
    try:
        rsp = requests.get(url=url, headers=header)
        if rsp.status_code == 200:
            print('Success.')
            html = rsp.text
            return html
        else:
            exit('Can not get the website.')
    except ConnectionError:
        exit('ConnectionError.')


def save_proxy(html):
    pattern = re.compile('<tr><td>(\d+\.\d+\.\d+\.\d+)<\/td><td>(\d+)<')
    result = re.findall(pattern, html)
    print('Get {} proxies.'.format(len(result)))
    with open(fp_unchecked, 'w+') as f:
        for i in result:
            proxy = i[0] + ':' + i[1]
            print(proxy)
            f.write(proxy + '\n')
    d = 'Save to {}.\nDone.'.format(fp_unchecked)
    print(d)


def main():
    html = get_index(url)
    save_proxy(html)


if __name__ == '__main__':
    main()