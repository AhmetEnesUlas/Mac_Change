import os
import time

# Function to display a welcome message with figlet
def figlet():
    os.system("apt-get install figlet")  # Ensure figlet is installed
    os.system("clear")  # Clear the terminal screen
    os.system("figlet Mac Changer Tool")  # Display the figlet text

def mac_changer():
    print("""
         0 - to automatically change your mac address
         1 - to manually change your Mac address
         2 - to reset your Mac address
         3 - to exit
    """)

# Function to change MAC address
def mac():
    while True:
        try:
            mac_changer()
            choice = int(input("Enter Num: "))  # User choice for MAC change action
            if 0 <= choice <= 3:
                if choice == 0:
                    # Automatically change MAC address
                    os.system("ifconfig eth0 down")
                    os.system("sudo macchanger -r eth0")
                    os.system("ifconfig eth0 up")
                    print("Transaction completed successfully")
                elif choice == 1:
                    # Manually change MAC address
                    mac = input("Enter your MAC address: ")
                    os.system(f"ifconfig eth0 down")
                    os.system(f"sudo macchanger --mac {mac} eth0")
                    os.system("ifconfig eth0 up")
                    print("Transaction completed successfully")
                elif choice == 2:
                    # Reset to default MAC address
                    os.system("ifconfig eth0 down")
                    os.system("sudo macchanger -p eth0")
                    os.system("ifconfig eth0 up")
                    print("Transaction completed successfully")
                elif choice == 3:
                    # Exit the program
                    os.system("clear")
                    os.system("figlet Exiting...")  # Fixed indentation here
                    time.sleep(2)
                    os.system("figlet Created By Sub0 Elliot")
                    break  # Exit the loop
            else:
                print("Error: Invalid choice, please enter a number between 0 and 3.")
        except ValueError:
            print("Error: Invalid input, please enter a valid number.")

# Calling the functions
figlet() 
mac()  # Call the mac() function
