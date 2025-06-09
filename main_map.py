import folium
import json

map_center_coordinates = [30.4369, -87.2756]
service_map = folium.Map(location=map_center_coordinates, zoom_start=10)

try:
    with open('data.json', 'r') as f:
        data=json.load(f)

    locations_to_plot = []
    for tech in data.get("technicians", []):
        tech['type'] = 'Technician'
        locations_to_plot.append(tech)

    for customer in data.get("customers", []):
        customer['type'] = 'Customer'
        locations_to_plot.append(customer)

    for location in locations_to_plot:
        coords = location["coords"]
        name =  location["name"]
        loc_type = location["type"]

        if loc_type == "Technician":
            marker_color = "blue"
            icon_symbol = "wrench"
        else:
            marker_color = "green"
            icon_symbol = "home"

        folium.Marker(
            location=coords, 
            popup=f"<strong>{name}</strong>",
            tooltip="Click for details",
            icon=folium.Icon(color=marker_color, icon=icon_symbol, prefix='fa')
        ).add_to(service_map)
    
except FileNotFoundError:
    print("File 'data.json' not found. Exiting.")
except json.JSONDecodeError:
    print("Syntax error in decoding JSON data. Please check formatting.")
except Exception as e:
    print(f"An error occurred: {e}")


output_filename = "interactive_map.html"
service_map.save(output_filename)

print(f"Interactive map saved to {output_filename}")
print("You can now open this file to view your interactive map.")
