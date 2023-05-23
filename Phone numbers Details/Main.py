import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# Function to parse the phone number
def parse_phone_number(number):
    try:
        phone = phonenumbers.parse(number)
        return phone
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Invalid phone number.")
        return None

# Function to validate the phone number
def validate_phone_number(phone):
    is_valid = phonenumbers.is_valid_number(phone)
    return is_valid

# Function to format the phone number
def format_phone_number(phone):
    international_format = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    national_format = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.NATIONAL)
    e164_format = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
    return international_format, national_format, e164_format

# Function to retrieve time zones for the phone number
def get_time_zones(phone):
    time_zones = timezone.time_zones_for_number(phone)
    return time_zones

# Function to retrieve the carrier name for the phone number
def get_carrier(phone):
    carrier_name = carrier.name_for_number(phone, "en")
    return carrier_name

# Function to retrieve the geolocation for the phone number
def get_geolocation(phone):
    description = geocoder.description_for_number(phone, "en")
    return description

# Prompt the user to enter a phone number
number = input("Enter your phone number: ")

# Parse the phone number
parsed_phone = parse_phone_number(number)

# Check if the phone number is valid
if parsed_phone:
    is_valid = validate_phone_number(parsed_phone)
    if is_valid:
        # Format the phone number
        international, national, e164 = format_phone_number(parsed_phone)
        # Get the time zones associated with the phone number
        time_zones = get_time_zones(parsed_phone)
        # Get the carrier name for the phone number
        carrier_name = get_carrier(parsed_phone)
        # Get the geolocation for the phone number
        geolocation = get_geolocation(parsed_phone)

        # Display the parsed phone number and information
        print("Parsed Phone Number:", parsed_phone)
        print("International Format:", international)
        print("National Format:", national)
        print("E.164 Format:", e164)
        print("Time Zones:", time_zones)
        print("Carrier:", carrier_name)
        print("Geolocation:", geolocation)
    else:
        print("Invalid phone number.")
else:
    print("Invalid phone number.")
