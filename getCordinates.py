from opencage.geocoder import OpenCageGeocode

def getCordinates(filename):
    key = '1230acf4d64345f9a07342cc88c86174'
    geocoder = OpenCageGeocode(key)
    fr = open(filename, "r")
    fw = open("cordinates.txt", "a+")
    lines = fr.readlines()
    i = 0
    for r in lines:
        result = geocoder.geocode(r.split("|")[1])
        z = "\n"
        if result and len(result):
            i = i + 1
            longitude = result[0]['geometry']['lng']
            latitude  = result[0]["geometry"]["lat"]
            z = "%f;%f;%s" % (latitude, longitude, r.split("|")[1])+ "\n"
        fw.write(z)

    print i
#query = "82 Clerkenwell Road, London";

def main():
    getCordinates("user_data.txt")

if __name__ == '__main__':
    main()
