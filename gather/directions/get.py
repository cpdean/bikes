import requests
import csv


def get_points():
    with open("../../projections/most_rides.csv") as c:
        return [i for i in csv.DictReader(c)]


def lookup(start, dest, mode):
    s_lat, s_long = start
    d_lat, d_long = dest
    p = {
        "origin": s_lat + "," + s_long,
        "destination": d_lat + "," + d_long,
        "mode": mode
    }

    u = "https://maps.googleapis.com/maps/api/directions/json"
    r = requests.get(u, params=p)
    return r


def main():
    points = get_points()
    print lookup(
            (points[2]['Latitude'], points[2]["Longitude"]),
            (points[2]['Latitude_end'], points[2]["Longitude_end"]),
            "bicycling"
    ).json()


if __name__ == '__main__':
    main()
