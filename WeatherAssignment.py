import requests
import datetime

base_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
params = {"q": "London,us", "appid": "b6907d289e10d714a6e88b30761fae22"}

def get_temperatures_for_date(date):
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data["cod"] == "200":
            temperatures_by_hour = {}
            for item in data["list"]:
                item_unix_timestamp = datetime.datetime.strptime(
                    item["dt_txt"], "%Y-%m-%d %H:%M:%S"
                )
                if abs(
                    item_unix_timestamp.date()
                    - datetime.datetime.strptime(date, "%Y-%m-%d").date()
                ) == datetime.timedelta(days=0):
                    temp = item["main"]["temp"]
                    hour = item_unix_timestamp.hour
                    temperatures_by_hour[hour] = temp

            if not temperatures_by_hour:
                print("No data")
                return None
            else:
                return temperatures_by_hour
        else:
            print("Error: Unable to fetch the data")
            return None

    except requests.exceptions.RequestException as e:
        print("Error: Unable to fetch the data", e)
        return None

def get_windspeeds_for_date(date):
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data["cod"] == "200":
            windspeed_by_hour = {}
            for item in data["list"]:
                item_unix_timestamp = datetime.datetime.strptime(
                    item["dt_txt"], "%Y-%m-%d %H:%M:%S"
                )
                if abs(
                    item_unix_timestamp.date()
                    - datetime.datetime.strptime(date, "%Y-%m-%d").date()
                ) == datetime.timedelta(days=0):
                    wind_speed = item["wind"]["speed"]
                    hour = item_unix_timestamp.hour
                    windspeed_by_hour[hour] = wind_speed
            if not windspeed_by_hour:
                print("No data")
                return None
            else:
                return windspeed_by_hour
        else:
            print("Error: Unable to fetch the data")
            return None

    except requests.exceptions.RequestException as e:
        print("Error: Unable to fetch the data", e)
        return None

def get_pressures_for_date(date):
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data["cod"] == "200":
            pressures_by_hour = {}
            for item in data["list"]:
                item_unix_timestamp = datetime.datetime.strptime(
                    item["dt_txt"], "%Y-%m-%d %H:%M:%S"
                )
                if abs(
                    item_unix_timestamp.date()
                    - datetime.datetime.strptime(date, "%Y-%m-%d").date()
                ) == datetime.timedelta(days=0):
                    pressure = item["main"]["pressure"]
                    hour = item_unix_timestamp.hour
                    pressures_by_hour[hour] = pressure

            if not pressures_by_hour:
                print("No data")
                return None
            else:
                return pressures_by_hour
        else:
            print("Error: Unable to fetch the data")
            return None

    except requests.exceptions.RequestException as e:
        print("Error: Unable to fetch the data", e)
        return None


if __name__ == "__main__":
    while True:
        print("\n")
        print("Choose an option:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter the choice (0, 1, 2, 3): ")

        if choice == "0":
            print("Exiting the program...")
            break
        elif choice == "1":
            date = input("Enter the date (YYYY-MM-DD) i.e. 2019-03-27: ")
            temperatures = get_temperatures_for_date(date)
            print("\n")
            if temperatures is not None:
                print(f"The temperatures on {date} are: ")
                for hour, temperature in temperatures.items():
                    print(f"{hour}:00 - {temperature:.2f}°")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD) i.e. 2019-03-27: ")
            windspeeds = get_windspeeds_for_date(date)
            print("\n")
            if windspeeds is not None:
                print(f"The windspeeds on {date} are: ")
                for hour, speed in windspeeds.items():
                    print(f"{hour}:00 - {speed}")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD) i.e. 2019-03-27: ")
            pressures = get_pressures_for_date(date)
            print("\n")
            if pressures is not None:
                print(f"The pressures on {date} are: ")
                for hour, pressure in pressures.items():
                    print(f"{hour}:00 - {pressure}")
        else:
            print("Invalid choice. Please choose again.")