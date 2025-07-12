class Products:
  def __init__ (self,name,price):
    self.name  = name
    self.price = price
  
  def show_products(self):
    return f"{self.name}の値段は{self.price}です。"
  
def calc_total_and_average_price(product_list):
  total = 0
  for product in product_list:
    total = total + product.price
    average = total / len(product_list)
  return total,average

products = [
    {"name": "りんご", "price": 120},
    {"name": "バナナ", "price": 80},
    {"name": "みかん", "price": 100}
]

product_list = []

for i in products:
  product = Products(i["name"],i["price"])
  product_list.append(product)

total,average = calc_total_and_average_price(product_list)
print(f"合計金額：{total}円")
print(f"平均単価：{average}円")


for product in product_list:
  print(product.show_products())




