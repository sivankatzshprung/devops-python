## Basic scraping 
# from https://github.com/pricing/
# use inspect in browser to find HTML path
# Install lxml and request:
# pip install lxml request


from lxml import html
import requests

page = requests.get('https://github.com/pricing/')
tree = html.fromstring(page.content)
print("Page Object:", tree)
plans = tree.xpath('//h3[@class="h2-mktg text-bold mt-1"]/text()')
pricing = tree.xpath('//h3[@class="h1-mktg lh-condensed-ultra my-3 py-1"]/text()')
print("Plans:", plans, "\nPricing:", pricing)