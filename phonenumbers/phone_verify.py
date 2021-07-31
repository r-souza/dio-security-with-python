import phonenumbers
from phonenumbers import geocoder, carrier

phone = input('Enter phone number using this format (+5511912345678): ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))

print(phonenumbers.is_valid_number(phone_number))

print(carrier.name_for_number(phone_number, 'pt'))
