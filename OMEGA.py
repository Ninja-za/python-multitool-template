import requests
import os
import json
from pystyle import Colors, Colorate
import time

logo = """
                              ██████╗ ███╗   ███╗███████╗ ██████╗  █████╗ 
                              ██╔═══██╗████╗ ████║██╔════╝██╔════╝ ██╔══██╗
                              ██║   ██║██╔████╔██║█████╗  ██║  ███╗███████║
                              ██║   ██║██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║
                              ╚██████╔╝██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║
                               ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
 """

colored_logo = Colorate.Horizontal(Colors.red_to_yellow, logo)
loop = "Y"




while True:
    os.system("title OMEGA -by ninja")
    os.system("cls")
    print(colored_logo)
    print("")
    print("   ╔════════════════════════════╗   ╔════════════════════════════╗   ╔════════════════════════════╗ ")
    print("   ║                            ║   ║                            ║   ║                            ║ ")
    print("   ║  ╚═══[1] ip lookup         ║   ║  ╚═══[5]                   ║   ║  ╚═══[9]                   ║ ")
    print("   ║  ╚═══[2] webhook sender    ║   ║  ╚═══[6]                   ║   ║  ╚═══[10]                  ║ ")
    print("   ║  ╚═══[3] show HWID         ║   ║  ╚═══[7]                   ║   ║  ╚═══[11]                  ║ ")
    print("   ║  ╚═══[4] webbhook spammer  ║   ║  ╚═══[8]                   ║   ║  ╚═══[12]                  ║ ")
    print("   ║                            ║   ║                            ║   ║                            ║ ")
    print("   ╚════════════════════════════╝   ╚════════════════════════════╝   ╚════════════════════════════╝ ")
    print("") 
    x = input("option: ")

    if x == "1":
        os.system("cls")
        print("IP LOOKUP\n")
        ip = input("Enter IP: ")
        os.system("cls")
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        print("RESULTS\n")
        print(f"Country: {data["country"]}")
        print(f"City: {data["city"]}")
        print(f"Region: {data["regionName"]}")
        print(f"Timezone: {data["timezone"]}")
        print("")
        pause = input("Press enter to return....")


    if x == "2":
         os.system("cls")
         print("WEBHOOK SENDER\n")
         url = input("Webhook URL: ")
         message = input("Message: ")
         name = input("Webhook Name: ")

         data = {
              "content": message,
             "username": name

         }



         try:
             r = requests.post(url, json=data)
             print("Webhook sent")
         except:
             print("ERROR SENDING WEBHOOK")

         print()
         pause = input("Press enter to return....")

    if x == "3":

          os.system("cls")
          print("Hardware ID\n")
          print("CPU SERIAL")
          print(os.system("wmic cpu get ProcessorID"))
          print()

          os.system("cls")
          print("Disk Serial\n")
          print("DISK SERIAL")
          print(os.system("wmic baseboard get SerialNumber"))
          print()

          os.system("cls")
          print("Motherboard Serial\n")
          print("MOTHERBOARD SERIAL")
          print(os.system("wmic baseboard get SerialNumber"))
          print()
          pause = input("Press enter to return....")


    if x == "4":
          os.system("cls")
    print("WEBHOOK SPAMMER\n")
    webhook = input("Webhook URL: ")
    text = input("Enter text to spam: ")
    name = input("Webhook Name: ")

    # Payload for sending message
    payload = {
        "content": text,
        "username": name
    }

    loop = "Y"  # Initialize the loop variable
    
    while loop == "Y":
        try:
            response = requests.post(webhook, json=payload)
            
            if response.status_code == 204:
                print("Message sent successfully.")
            else:
                print(f"Failed to send message. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error sending webhook: {e}")

        # Asking the user if they want to continue
        loop = input("Do you want to continue spamming? (Y/N): ").capitalize()
         


        
      
       
          


            
         



        
            
             

         
    


    