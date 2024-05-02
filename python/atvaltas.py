merfold = int(input("Adjon meg egy számot mérföldben: "))
meter = 1609.344
print(f"{merfold} mérföld =")
print(f"\t{merfold*meter*100:.1f} centiméter")
print(f"\t{merfold*meter:.2f} méter")
print(f"\t{merfold*meter/1000:.2f} kilométer")