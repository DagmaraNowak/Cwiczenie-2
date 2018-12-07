print("Hello World")
name = 'Dagmara'
print("Hello World",name)
message = 'Hello {0:s} and {1:s}!'
message.format('Dagmara','Kuba')
print(message)
message1 = "Kuba ma {0:d} pieskow"
print(message1.format(6))
message2 = "Goodbye %s and %s"
print(message2 % ('Dagmara','Kuba'))
print((message2 % ('Dagmara','Kuba')).upper())
