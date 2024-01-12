import phonenumbers
from phonenumbers import timezone,geocoder,carrier
def number():
    phone_number = input("Enter the phone number you want to check with +: ")
    phone=phonenumbers.parse(phone_number)
    time=timezone.time_zones_for_number(phone)
    cr=carrier.name_for_number(phone,"en")
    geo=geocoder.description_for_number(phone,'en')
    print(phone,time,cr,geo)
# print(time)
# print(cr)
# print(geo)
number()
while input("Do you want to check another number? (y/n): ").lower() == 'y':
    number()
