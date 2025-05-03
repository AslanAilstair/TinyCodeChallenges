import time
import sys

# ASCII art for "Hello World"
card = """ 
  _______ 
 /       \
|  Hello  |
|  World  |
  _______/
"""

# Function to print text with delay (animation)
def print_with_delay(text):    
    for char in text:        
        sys.stdout.write(char)        
        sys.stdout.flush()        
        time.sleep(0.05)    
    print()
  
# Display the card with animation
print_with_delay("Welcome to your Greeting Card! 🌟")
print(card)
print_with_delay("Crafted with tiny steps! 💻 #CodeTinySteps")
