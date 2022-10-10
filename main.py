import requests, json


def error_correct(unformated_data):
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if unformated_data["cod"] != "404":

        # store the value of "main"
        # key in variable y
        y = unformated_data["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = unformated_data["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # print following values
        print(" Temperature (in Degrees) = " + str(current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) + "\n humidity (in percentage) = " +
              str(current_humidity) + "\n description = " +
              str(weather_description))
    #else statement if zipcode not found
    else:
        print(" Zipcode Not Found ")


def main():
    #Base url of openweathermap
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    # API key from open wether map
    api_key = "4aa30f675c0089c92d019e633a38aa67"
    # user input of zipcode
    zip_code = input("Please enter a zipcode or q to quit\n")
    #While loop to quit if q is pressed
    while zip_code != 'q':
        #fstring to build URL for approprate unit and zipcode for JSON
        url = f"{base_url}?q={zip_code}&units=imperial&APPID={api_key}"

        #Tryblock to enable error messaging
        try:
            response = requests.get(url)
            unformated_data = response.json()
            print("Successful connection")
            error_correct(unformated_data)
        except:
            print('Malformed URL')

        zip_code = input("whats your zipcode or q to quit\n")


#start of the program, calling main and running main function.
if __name__ == "__main__":
    main()
