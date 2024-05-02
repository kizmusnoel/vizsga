bill_szam = int(input("Pontozott eszközök darabszáma: "))
bill_list = []
for i in range(bill_szam):
    print()
    current_list = [int(input("\tFestés minősége: ")), int(input("\tBillentyű lenyomásának könnyedsége: ")), int(input("\tAnyag minősége: ")), int(input("\tLED-ek fényereje: ")), ]
    osszeg = 0
    for a in current_list:
        osszeg += a
    print(f"\tPontszámok összege: {osszeg}")
    current_list.append(osszeg)
    bill_list.append(current_list)

def atlag():
    atlag = 0
    for b in bill_list:
        atlag += b[-1]
    return f"{atlag/len(bill_list):.2f}"

print(f"Pontozott eszközök minőségi átlaga: {atlag()}")