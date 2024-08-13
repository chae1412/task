import requests
from bs4 import BeautifulSoup
import pandas as pd

# 쇼핑몰 URL (예: 특정 페이지의 URL)
url = 'https://spao.com/product/list.html?cate_no=64'

# 웹 페이지 요청
response = requests.get(url)
html = response.text

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

# 상품 정보를 담을 리스트
products = []

# 상품 리스트를 찾는 방법 (쇼핑몰에 따라 다를 수 있음)
product_list = soup.find_all('div', class_='product-item')

for product in product_list:
    name = product.find('div', class_='product-title').text.strip()  # 상품명
    price = product.find('div', class_='product-price').text.strip()  # 가격
    
    # 정보를 딕셔너리에 저장
    products.append({
        'name': name,
        'price': price
    })

# 데이터를 Pandas DataFrame으로 변환
df = pd.DataFrame(products)

# CSV 파일로 저장 (선택 사항)
df.to_csv('products.csv', index=False)

print(df)