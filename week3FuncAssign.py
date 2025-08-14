def calculate_discount(price,discount_percent):
    discount_percent/=100
    if discount_percent>=0.2:
        disc=price*discount_percent
        return price-disc
    else:
        return price
    
price,discount_percent=map(int, input("Enter the original price and the discount percentage in respective order separated by space: ").split())
print("Discounted_price: ",calculate_discount(price,discount_percent))
    
