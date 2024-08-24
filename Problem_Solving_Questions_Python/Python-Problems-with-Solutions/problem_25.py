'''A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams'''


p1 = "Make alot of Money"
p2 ="Buy now"
p3 = "Subscribe this"
p4 = "click this "

message = input("Enter Your Commment: ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
 print("This Message is SPAM")
else:
 print("This Message is not SPAM")