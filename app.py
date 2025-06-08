from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def geocode(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json"}
    headers = {"User-Agent": "flask-map-app/1.0"}
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    if not data:
        return None
    return float(data[0]["lat"]), float(data[0]["lon"])

def get_osrm_route(start, end):
    base_url = "https://router.project-osrm.org/route/v1/walking/"
    coords = f"{start[1]},{start[0]};{end[1]},{end[0]}"
    params = "?overview=full&geometries=geojson"
    url = base_url + coords + params

    res = requests.get(url)
    data = res.json()

    if "routes" not in data or not data["routes"]:
        return []

    return [[lat, lon] for lon, lat in data["routes"][0]["geometry"]["coordinates"]]

@app.route("/", methods=["GET", "POST"])
def index():
    start = end = ""
    start_coords = end_coords = None

    path = [
        [47.624285, -122.324056],
        [47.624300, -122.325343],
        [47.621978, -122.325319],
        [47.622005, -122.323081],
        [47.624292, -122.323081],
        [47.623148, -122.323106],
        [47.623174, -122.322073],
        [47.624266, -122.321996],
        [47.622043, -122.322099],
        [47.622025, -122.320942],
        [47.624311, -122.320927],
        [47.624269, -122.319911],
        [47.623150, -122.319960],
        [47.623150, -122.320940],
        [47.623141, -122.319973],
        [47.622018, -122.319938],
        [47.621993, -122.318917],
        [47.623121, -122.318875],
        [47.623141, -122.317839],
        [47.623141, -122.318848],
        [47.624277, -122.318837],
        [47.624284, -122.317775],
        [47.624269, -122.318837],
        [47.621984, -122.318880],
        [47.621991, -122.316820],
        [47.624269, -122.316745],
        [47.621993, -122.316801],
        [47.621972, -122.315771],
        [47.623136, -122.315729],
        [47.621986, -122.315771],
        [47.621993, -122.314677],
        [47.624264, -122.314666],
        [47.621965, -122.314688],
        [47.621972, -122.313679],
        [47.624293, -122.313647],
        [47.624260, -122.312637],
        [47.622102, -122.312697],
        [47.621991, -122.313701],
        [47.622110, -122.311408],
        [47.624457, -122.311324],
        [47.624437, -122.310672],
        [47.622110, -122.310717],
        [47.622079, -122.310057],
        [47.624411, -122.310004],
        [47.624433, -122.308682]
        ]

    if request.method == "POST":
        start = request.form.get("start")
        end = request.form.get("end")
        start_coords = geocode(start)
        end_coords = geocode(end)

        if start_coords and end_coords:
                start_path = get_osrm_route(start_coords, path[0])
                end_path = get_osrm_route(path[-1], end_coords)
                path = start_path + path + end_path

    return render_template("index.html",
                           start=start,
                           end=end,
                           start_coords=start_coords,
                           end_coords=end_coords,
                           custom_path=path)

if __name__ == "__main__":
    app.run(debug=True)
