# Project Roadmap: Interactive Technician & Routing Application

## 1. Project Vision & Goal

To create a visually appealing, user-friendly, and intelligent application for service businesses to visualize technician/customer locations, manage personnel and jobs, and optimize daily routes for maximum efficiency in terms of drive time and distance.

### Core Principles
- **User-Friendly UI:** The application must be intuitive, allowing non-technical users to easily add, view, and manage data.
- **Visually Appealing & Professional:** The map and interface should be clean, clear, and professional in appearance.
- **Practical Problem-Solving:** The tool must effectively solve the real-world challenge of efficient field service routing.
- **Accessible & Free:** The core tool will be developed as free and open-source.
- **Innovative & Intelligent:** Aims to incorporate unique, AI-powered features.

---

## 2. Phased Development Plan

We will build this application in stages, with each phase resulting in a functional, enhanced version of the tool.

### Phase 1: Foundational Map & Markers (MVP v0.1) - ✅ COMPLETE
* **Goal:** Create a basic interactive map and learn to plot static points with custom icons. This proves the core visualization concept.
* **Key Tasks:**
    - [x] Install the `folium` Python library.
    - [x] Write a script to create a base map with a professional-looking tile set.
    - [x] Define a small, hard-coded list of coordinates for "technicians" and "customers."
    - [x] Plot these points on the map using custom colors and icons.
    - [x] Add informative HTML pop-ups for each marker.
    - [x] Save the final map as a standalone interactive HTML file.
* **Key Learnings:** `folium` library basics, Python data structures, creating visual output.

### Phase 2: Structured Data & Geocoding (MVP v0.2) - 🚧 IN PROGRESS
* **Goal:** Move data out of the script and into a structured file, and convert real-world addresses into plottable map coordinates.
* **Key Tasks:**
    - [x] Create a `data.json` file to store technician and customer information.
    - [x] Modify the Python script to read its data from this `data.json` file.
    - [ ] Install the `geopy` library.
    - [ ] Write a function to geocode addresses from the JSON file into latitude/longitude coordinates.
    - [ ] Implement error handling for invalid addresses.
* **Key Learnings:** Working with JSON files, API interaction (`geopy`), robust error handling.

### Phase 3: Building a UI for Data Management (v0.3)
* **Goal:** Replace manual editing of the JSON file with a simple web-based User Interface (UI).
* **Key Tasks:**
    - [ ] Learn the basics of the **Flask** web framework.
    - [ ] Create simple web pages with HTML forms to add/edit technicians and customers.
    - [ ] Write Python-Flask "routes" to handle form submissions and update the `data.json` file or a simple SQLite database.
    - [ ] Display the current list of technicians/customers on the web page.
* **Key Learnings:** Web development basics (Flask), handling web forms, data persistence.

### Phase 4: Point-to-Point Routing & Proximity (v0.4)
* **Goal:** Integrate basic routing and distance calculations into the application.
* **Key Tasks:**
    - [ ] Integrate a routing API (e.g., OpenRouteService) to calculate and draw a driving route between two points on the map.
    - [ ] Display travel time and distance in the UI.
    - [ ] Implement a feature to find the closest technician to a customer (by straight-line distance first).
* **Key Learnings:** `requests` library, parsing complex JSON responses, advanced `folium` plotting (`PolyLine`).

---

## 3. Advanced Features & Future Vision (v1.0 and beyond)

*(This section remains the same as before, outlining the more advanced goals like Multi-Stop Optimization, AI Features, and Deployment)*

### Phase 5: Multi-Technician Route Optimization & Visualization (v1.0)
* **Goal:** Calculate and visualize optimized multi-stop routes for **multiple technicians simultaneously** on a single map.
...

### Phase 6: Real-Time Traffic Integration
...

### Phase 7: Unique AI & Differentiator Features
...

### Phase 8: Packaging & Deployment
...

---

## 4. Technology Stack (Evolving)

* **Language:** Python 3
* **Core Libraries:** `folium`, `geopy`, `requests`, `os`, `shutil`
* **Web Framework:** Flask (or similar like Django)
* **Database:** JSON file initially, then potentially SQLite.
* **APIs:** Nominatim (for geocoding), OpenRouteService/Google Maps/Mapbox (for routing & optimization).