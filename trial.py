hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price
average_price = total_price/len(prices)
print("Average haircut price: " + str(average_price))
print (price)
change_price=price

percent_discount = 0.85
Discount = [0, 0, 0, 0, 0, 0, 0, 0]

for a in range(len(prices)):
  Discount [a] = prices[a]*percent_discount
  
print(Discount)

new_prices = [price -change_price for price in prices]
print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
  
print("Total Revenue: " + str(total_revenue))
avg_daily_revenue = total_revenue/7
print("Average Daily Revenue: " + str(avg_daily_revenue))

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)

  

