names = ["bob", "marry"]
for name in names:
    if name.startswith("b"):
        print("Found")
        break
else:
    print("Not found")
