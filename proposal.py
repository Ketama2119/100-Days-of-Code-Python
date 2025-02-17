import time
import os
import sys
import math
from random import randint

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_heart():
    colors = ['\033[91m', '\033[95m']  # Red and Pink
    heart_frames = [
        r'''
         @@@@@@       @@@@@@     
       @@@@@@@@@@   @@@@@@@@@@   
      @@@@@@@@@@@@ @@@@@@@@@@@@  
     @@@@@@@@@@@@@@@@@@@@@@@@@@@ 
     @@@@@@@@@@@@@@@@@@@@@@@@@@@ 
      @@@@@@@@@@@@@@@@@@@@@@@@@  
       @@@@@@@@@@@@@@@@@@@@@@@   
        @@@@@@@@@@@@@@@@@@@@@    
          @@@@@@@@@@@@@@@@@      
            @@@@@@@@@@@@@        
              @@@@@@@@@          
                @@@@@            
                 @@              
        ''',
        # Slightly modified frame for animation
        r'''
         @@@@@@       @@@@@@     
       @@@@@@@@@@   @@@@@@@@@@   
      @@@@@@@@@@@@ @@@@@@@@@@@@  
     @@@@@@@@@@@@@@@@@@@@@@@@@@@ 
     @@@@@@@@@@@@@@@@@@@@@@@@@@@ 
      @@@@@@@@@@@@@@@@@@@@@@@@@  
       @@@@@@@@@@@@@@@@@@@@@@@   
        @@@@@@@@@@@@@@@@@@@@@    
          @@@@@@@@@@@@@@@@@      
            @@@@@@@@@@@@         
              @@@@@@@@@          
                @@@@             
                 @@              
        '''
    ]
    
    start_time = time.time()
    
    try:
        while True:
            clear()
            # Select a heart frame for the pulsing effect
            frame = heart_frames[int((time.time() * 2) % 2)]
            
            # Add twinkling stars at random positions
            for _ in range(3):
                print(f"\033[{randint(1, 20)};{randint(1, 80)}H\033[93m*\033[0m", end='')
            
            # Pulse the heart color and replace '@' with heart symbols
            color = colors[int((time.time() * 2) % 2)]
            colored_heart = color + frame.replace('@', '♥') + '\033[0m'
            print(colored_heart)
            
            # (Optional) Floating ring emoji below the heart
            print(f"\033[1;97m{' ' * int((time.time() * 10) % 20)}💍\033[0m")
            
            # -------------------------------
            # Animate rotating proposal text
            # -------------------------------
            # Set rotation parameters:
            rotation_speed = 2      # radians per second
            angle = time.time() * rotation_speed
            radius = 10             # radius of the circular path (in character cells)
            
            # Calculate offset from the heart center using sine and cosine
            x_offset = int(radius * math.cos(angle))
            y_offset = int(radius * math.sin(angle))
            
            # Define an approximate center for the heart
            # (Adjust these values if your heart art changes)
            heart_center_row = 8    # row number (approximate center of heart art)
            heart_center_col = 35   # column number (approximate center of heart art)
            
            # Calculate absolute position for the rotating text
            text_row = heart_center_row + y_offset
            text_col = heart_center_col + x_offset
            
            # Proposal text with some blinking/bright effect
            proposal_text = "\033[5;97mWould you marry me?\033[0m"
            
            # Move the cursor to the calculated position and print the proposal text
            print(f"\033[{text_row};{text_col}H{proposal_text}")
            
            # -------------------------------
            # (Optional) Display additional messages after 4 seconds
            if time.time() - start_time > 4:
                print("\n\033[1;95mTo the love of my life:\033[0m 💖")
                print("\033[93m" + "~" * 40 + "\033[0m")
                print("You make every moment magical...")
                print("\033[93m" + "~" * 40 + "\033[0m")
            # -------------------------------
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\033[0m")  # Reset colors on exit

def main():
    animate_heart()
    
    # Final interaction after animation (e.g., when the animation loop is stopped)
    input("\n\033[92m[Press Enter to see her answer]\033[0m ")
    print("\n\033[1;92mShe said: YES! 💍 💞 🌸\033[0m")
    print(r'''
          \_\     _/
            \___/
            |   |
            |   |
            /---\
           /     \
          ''' + '\033[0m')

if __name__ == "__main__":
    main()