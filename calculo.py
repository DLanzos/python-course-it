def shortest_string(x,y):
	if len(x) <= len(y):
		return x
	else:
		return y
		
print(shortest_string("Hello", "Holandaa"))
