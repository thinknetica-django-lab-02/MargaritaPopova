from main.models import Building, Apartment

b = Building(
    lat=54.343545,
    lng=36.4534543,
    year=2007
).save()

a = Apartment(
    building=b,
    story=3,
    rooms=3,
    price=3000000,
    area=54.6
).save()

for i in range(5):
    b = Building.objects.create(
        lat=55+i,
        lng=35+i,
        year=2000+i
    )
    for j in range(5):
        Apartment.objects.create(
            building=b,
            story=j+1,
            rooms=2,
            price=2000000+j*10,
            area=30+j
        )

buildings = Building.objects.all()
apartments = Apartment.objects.all()

print(*buildings)
print(*apartments)
print(Building.objects.filter(year=2004))
print(Apartment.objects.filter(rooms=2))