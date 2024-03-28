def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_price = price - (price * (discount_percent / 100)) 
        return discount_price
    else:
        return price
    
   # To find discount price is: 
   
def main():  

    # Prompting the user for inputs:      
    original_price= float(input("Enter the original price:")) 
    op= input("Enter operator:")
    discount_percent= float(input("Enter the discount percent:"))

    # Calculating the final price using calculate_discount function
    final_price= calculate_discount(original_price, discount_percent)

    # Printing the final price:
    print("Final price after discount is:",final_price)

    #Finding the discount price:
    discount_price= float(input("Enter the original price:"))
    op= input("Enter operator:")
    discount_price= float(input("Enter the final price:"))
    discount_price=(original_price - final_price)
    print("Discount price is:",discount_price)

    if final_price == original_price:
       print("No discount applied...final price:", final_price)
    else:
       print("Discount applied after final price3:" ,final_price)

if __name__ == "__main__":
    main()

    
    



