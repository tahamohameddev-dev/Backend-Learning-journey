from test_Python import phone, ifone

type1 = phone("infinix", "read", True)
type2 = phone("iphone", "black", "False")
type3 = ifone("ifone", "white", False)
print(type1.is_android)
print(type2.is_android)

print(type1.is_infinix())
type3.string()