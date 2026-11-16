






#Import Commands
from csv import Error
from typing import Type

import json
import requests


#FUNCTIONS DEFINED

def app_Instructions():
    instruct = "Type two letters for a country's abbreviation, such as 'CA' for 'Canada.' You have 3 attempts."
    return
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

                    country_info = f"Country's Info:  {name}  |  {capital}  |  {population:,}"
                    print(country_info)
    finally: 
        print("Thanks for using this tool!")                   

                    
                

                

               
#-----------------------------------------------------------------------------------------------
            #Notes to SELF - Instructions from Assignment:
            #API shuld return: capital city, name of country, and currency
            #name
            #capital
            #population
            #currencies  --> break the dictionary to get "name"
            # practice code for API before final placement
            # url = f"https://countries.dev/alpha/{userInput}"
                    #response = requests.get(url, timeout=8)
                #else: print("problematic API request status, {response.status_code}"):
            
       


   

if __name__ == "__main__":
    main()







