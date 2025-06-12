# =================================================================
# FINAL COMPLETE SCRIPT
# =================================================================
import folium
import json
from geopy.geocoders import ArcGIS

# --- 1. SETUP ---
# Create the geocoder instance we will use
geolocator = ArcGIS()

# Define the starting center of our map
map_center_coordinates = [30.4369, -87.2756]
service_map = folium.Map(location=map_center_coordinates, zoom_start=10)


# --- 2. DATA LOADING AND PROCESSING ---
try:
    # Open and load the address data from the JSON file
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Combine technicians and customers into one list to loop through
    locations_to_plot = []
    for tech in data.get("technicians", []):
        tech['type'] = 'Technician'
        locations_to_plot.append(tech)

    for customer in data.get("customers", []):
        customer['type'] = 'Customer'
        locations_to_plot.append(customer)

    print(f"Found {len(locations_to_plot)} total locations to plot.")

    # --- 3. GEOCODING AND PLOTTING LOOP ---
    # This is the main loop where the magic happens
    for location in locations_to_plot:
        address = location.get("address")
        name = location.get("name")
        loc_type = location.get("type")

        if not address:
            print(f"--> Skipping '{name}' due to missing address.")
            continue

        try:
            print(f"Geocoding: {address}...")
            # THIS IS THE KEY STEP: Call the geocoder to get location data
            found_location = geolocator.geocode(address, timeout=10)

            if found_location:
                print("...Success! Location found.")
                # Extract the coordinates from the result
                coords = [found_location.latitude, found_location.longitude]

                # Your original code for styling the markers
                if loc_type == "Technician":
                    marker_color = "blue"
                    icon_symbol = "wrench"
                else:
                    marker_color = "green"
                    icon_symbol = "home"

                # Create the marker using the 'coords' we just found
                folium.Marker(
                    location=coords,
                    popup=f"<strong>{name}</strong>",
                    tooltip="Click for details",
                    icon=folium.Icon(color=marker_color, icon=icon_symbol, prefix='fa')
                ).add_to(service_map)
            else:
                print(f"...Failed. Could not find coordinates for: {address}")

        except Exception as e:
            print(f"An error occurred for address '{address}': {e}")


# --- 4. SAVING THE FINAL MAP ---
except FileNotFoundError:
    print("ERROR: File 'data.json' not found. Exiting.")
except json.JSONDecodeError:
    print("ERROR: Syntax error in decoding JSON data. Please check formatting.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Save the map to an HTML file
output_filename = "interactive_map.html"
service_map.save(output_filename)

print("\n----------------------------------------------------")
print(f"Map generation complete. File saved to: {output_filename}")
print("You can now open this file in a browser to view your map.")
print("----------------------------------------------------")