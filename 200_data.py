import pandas as pd
import random

print("Generating 200 data......")

data = []
products = ["Lipstick", "Foundation", "Mascara", "Blush", "Eyeliner", "Compact", "Serum", "Primer"]

for i in range(200):
    product_name = random.choice(products) + " " + str(i+1)
    brand_rating = random.randint(1, 5)
    weight = random.choice([10, 15, 20, 30, 40, 50, 100, 150, 200])
    spf = random.choice([0, 15, 20, 30, 50])
    customer_rating = round(random.uniform(3.0, 5.0), 1)
    price = (brand_rating * 180) + (weight * 4) + (spf * 5) + (customer_rating * 120) + random.randint(-50, 50)
    data.append([product_name, brand_rating, weight, spf, customer_rating, int(price)])

df = pd.DataFrame(data, columns=['Product_Name','Brand_Rating','Weight','SPF','Customer_Rating','Price'])
df.to_excel("makeup_data.xlsx", index=False)
print("done! 200 data saved in  makeup_data.xlsx !")