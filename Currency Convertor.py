egyptian = print ("Central bank of Egypt exchange rate 1 USD = 49.20 EGP (as of 8/11/2024)")
print ("Enter how many dollars you currently own")
random = input()
exchange = int(random) * 49.20
rounded = round(exchange, 2)
print ("What is your name?")
name = input().capitalize()
print (f"{name}, You currently have {rounded} EGP")