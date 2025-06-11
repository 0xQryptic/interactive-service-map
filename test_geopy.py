from geopy.geocoders import ArcGIS

# 1. Initialize the ArcGIS geocoder (it's simpler, no user_agent needed)
geolocator = ArcGIS()

# 2. Define the address you want to look up
address = "222 W Main St, Pensacola, FL 32502"

print(f"Looking up the coordinates for: {address}")

# 3. Call the geocode method to get the location data
# We'll still use a timeout, just in case.
try:
    location = geolocator.geocode(address, timeout=10)

    # 4. Print the results
    if location:
        print("\n--- Results ---")
        print(f"Full Address: {location.address}")
        print(f"Coordinates: ({location.latitude}, {location.longitude})")
    else:
        print("Address could not be found.")

except Exception as e:
    print(f"An error occurred: {e}")