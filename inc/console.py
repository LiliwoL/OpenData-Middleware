import pyfiglet
import platform
import os



# ======================================================================================================================
# Fonctions utiles
# ======================================================================================================================




# Ascii text
def generate_figlet_text(text, font="standard"):
    # Create a Figlet object with the specified font
    figlet = pyfiglet.Figlet(font=font)

    # Render the text
    ascii_art = figlet.renderText(text)
    return ascii_art


# Nettoie la console
def clear_console():
    # Detect the operating system
    current_os = platform.system()

    if current_os == "Windows":
        os.system("cls")
    else:
        os.system("clear")