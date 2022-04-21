length = input("What is the length of the prism? ")
width = input("What is the width of the prism? ")
height = input("What is the height of the prism? ")

def volume(length, width, height):
    """Returns the volume of a prism."""
    return float(length) * float(width) * float(height)


print("The volume of the prism is " + str(volume(length, width, height)) + ".")
