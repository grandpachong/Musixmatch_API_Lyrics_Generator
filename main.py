import requests
import json
from lyrics_api import *

# Example call: base_url + lyrics_matcher + format_url + artist_search_parameter + artist_variable + track_search_parameter + track_variable + api_key
# Example json print: print(json.dumps(api_call, sort_keys=True, indent=2))

while True:
    print()
    print("Lyrics Generator")
    print()
    print("Please choose your search method")
    print("1: Use an API method with parameters & view JSON")
    print("2: Find lyrics via artist & song name")
    print("3: Quit")
    print()
    choice = input("> ")
    print()

    if choice == "3":
        break

    # Use an API method with parameters & view JSON
    if choice == "1":
        print("API Methods")
        for index, api_method in enumerate(api_methods, start = 0):
            print(str(index) + ": " + api_method)
        print()
        print("Your choice (0 - 15)")
        method_choice = input("> ")
        print()
        user_choice = api_methods[int(method_choice)]
        parameter_list = get_parameters(user_choice)

        print("Parameters")
        for index, parameter in enumerate(parameter_list, start = 0):
            print(str(index) + ": " + parameter)
        print()

        # Start building the API call
        api_call = base_url + user_choice + format_url

        while True:
            print("API call so far: " + api_call)
            print()
            print("Which parameter would you like to add a value for? (0-15) (Type x when finished)")
            parameter_choice = input("> ")
            print()

            # Add the API key and make the call
            if parameter_choice == "x":
                api_call = api_call + api_key
                request = requests.get(api_call)
                data = request.json()
                print("Final API Call: " + api_call)
                print()
                print("JSON DATA")
                print(json.dumps(data, sort_keys=True, indent=2))
                break

            # Add parameter
            else:
                parameter_choice_string = parameter_list[int(parameter_choice)]
                value = input(parameter_choice_string)
                api_call = api_call + parameter_choice_string + value
                print()

    # Find lyrics via artist & song name
    if choice == "2":
        print("Enter artist name:")
        artist_name = input()
        print("Enter song name:")
        track_name = input()
        print()
        api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
        request = requests.get(api_call)
        data = request.json()
        data = data['message']['body']
        print("API Call: " + api_call)
        print()
        print(data['lyrics']['lyrics_body'])

    # Check if user wants to go again & try to be funny by mentioning DJ Khaled
    print()
    print("Another one? *DJ Khaled voice* (y/n)")
    again = input("> ")
    if again == "n":
        break