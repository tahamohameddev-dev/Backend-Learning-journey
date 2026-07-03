from test_Python import phone

type1 = phone("infinix", "read", True)
type2 = phone("iphone", "black", "False")
print(type1.is_android)
print(type2.is_android)

print(type1.is_infinix())