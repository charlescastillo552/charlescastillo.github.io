import pyfiglet # type: ignore

# Generate ASCII art
ascii_art = pyfiglet.figlet_format("Yourname", font="slant") # Replace "YourName" with your name

# Print ASCII art to console
print(ascii_art)

ascii_art = """
 ________  ___  ___  ________  ________  ___       _______   ________      
|\   ____\|\  \|\  \|\   __  \|\   __  \|\  \     |\  ___ \ |\   ____\     
\ \  \___|\ \  \\\  \ \  \|\  \ \  \|\  \ \  \    \ \   __/|\ \  \___|_    
 \ \  \    \ \   __  \ \   __  \ \   _  _\ \  \    \ \  \_|/_\ \_____  \   
  \ \  \____\ \  \ \  \ \  \ \  \ \  \\  \\ \  \____\ \  \_|\ \|____|\  \  
   \ \_______\ \__\ \__\ \__\ \__\ \__\\ _\\ \_______\ \_______\____\_\  \ 
    \|_______|\|__|\|__|\|__|\|__|\|__|\|__|\|_______|\|_______|\_________\
                                                               \|_________|
                                                               
"""
print(ascii_art)

