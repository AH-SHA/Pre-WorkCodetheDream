






#IMPORT COMMANDS
from csv import Error
from typing import Type

import json
import requests


#FUNCTIONS DEFINED

def app_Instructions():
    instruct = "Type two letters for a country's abbreviation, such as 'CA' for 'Canada.' You have 3 attempts."
    print(instruct)



def api_Attempt(alpha2Code):    
    url = f"https://countries.dev/alpha/{userInput}"
    response = requests.get(url, timeout=8)
    return response
    




#TRY-EXCEPT BLOCK

#TRY

def main():
     
    

    i = 3  
for i in range (3):
    counter = 2-i 

    app_Instructions()
    print()

    try:
        
        userInput = input("Enter the 2-letter abbreviation for a country for which you want to find its Capital City and Population: ")

    except TypeError:
        print("Wrong format, try again.");
        continue

    except ValueError:
        print("Wrong format, try again.");
        continue

    except TimeoutError:
        print("Connection timed out, try again."); 
        continue

    else:    
       if userInput.isalpha():
            numChar = len(userInput)
            if numChar != 2:
                print("Wrong format, try again.")

            else: numChar == 2;

# INVOKE API JSON and Parsing HERE:
    # Nested try-except block
            
            try:
               

               response = api_Attempt(userInput)

            except requests.exceptions.Timeout:
                print("Timed out.");
                continue

            except requests.exceptions.ConnectTimeout:
                print("Connection timed out.");
                continue

            except requests.exceptions.ReadTimeout:
                print("Server took too long to respond.");
                continue

            except requests.exceptions.ConnectionError:
                print("Connection failed.");
                continue

            else:
                if response.status_code == 200:
                   
                    answer = response.json()
              
                    name = answer["name"]
                    capital = answer["capital"]
                    population = answer["population"]

                    country_info = f"Country's Info:  {name}  |  {capital}  |  {population:,} population"
                    print(country_info)
                    print(str(counter) + " chances remaining to select a country.")
                        
    finally: 
        print("Thanks for using this tool!") 
        print()
        print()

   

if __name__ == "__main__":
    main()







