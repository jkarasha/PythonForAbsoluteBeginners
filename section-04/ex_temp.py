celcius = input("What is the temperature in Celcius? ")

def get_farhenheit(celcius):
    """Converts Celcius to Farhenheit."""
    return float(celcius) * 1.8 + 32


def get_farhenheit_rounded(celcius):
    """Converts Celcius to Farhenheit."""
    return round(float(celcius) * 1.8 + 32, 1)

print("farhenheit: " + str(get_farhenheit(celcius)))
print("farhenheit rounded: " + str(get_farhenheit_rounded(celcius)))
