# A dictionary of color names and their corresponding hexadecimal codes
COLORS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blue": "#0000ff",
    "chartreuse": "#7fff00",
    "chocolate": "#d2691e",
    "coral": "#ff7f50"
}

# Function to look up a color code based on the color name
def get_color_code(color_name):
    return COLORS.get(color_name.lower(), "Invalid color name")

# Main program loop
while True:
    color_name = input("Enter a color name (or blank to exit): ")
    if not color_name:
        break
    color_code = get_color_code(color_name)
    print(f"The color code for {color_name} is {color_code}")