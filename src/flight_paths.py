"""Find path between airports."""
import urllib.request, json

def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3 # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934 # convert km to miles


def check_data():
    url = 'https://codefellows.github.io/sea-python-401d6/_downloads/cities_with_airports.json'
    jsonurl = urllib.request.urlopen(url)
    data = json.loads(jsonurl.read().decode())
    count = 0
    for city in data:
        count += 1
        if city['city'] == 'Nairobi':
            print(city)
            return count


def find_path_between_cities(city1, city2):
    """Return path and distance between two cities."""
    url = 'https://codefellows.github.io/sea-python-401d6/_downloads/cities_with_airports.json'
    jsonurl = urllib.request.urlopen(url)
    data = json.loads(jsonurl.read().decode())

    stack = [city1]
    connections = {}
    distances = {}
    while len(stack) > 0:
        route = stack.pop(0)
        for airport in data:
            if airport['city'] == route:
                for city in airport['destination_cities']:
                    stack.append(city)
                    for location in data:
                        if location['city'] == city:
                            lat_lon1 = location['lat_lon']
                            break
                    lat_lon2 = airport['lat_lon']
                    distance = calculate_distance(lat_lon1, lat_lon2)
                    if city not in distances or distances[city] > distance:
                        distances[city] = distance
                        connections[city] = route
                    if city == city2:
                        current = city
                        path = [city1]
                        while current != city1:
                            path.insert(1, current)
                            current = connections[current]
                        return path, distances[city2]
    return 'There is no path between these cities'


# Goma
# Kinshasa
# Kisangani
# Lubumbashi
# Brazzaville
# Pointe-Noire
# Malabo
# Franceville
# Libreville
# Port-Gentil
# São Tomé
# Bujumbura
# Eldoret
# Mombasa
# Kisumu
# Nairobi
# Plaine Magnien
# Kigali
# Victoria
# Juba
# Dar es Salaam
# Hai District
# Zanzibar
# Entebbe
# Djibouti City
# Asmara
# Addis Ababa
# Dire Dawa
# Bosaso
# Galkayo
# Garowe
# Hargeisa
# Kismayo
# Mogadishu
# Adrar
# Algiers
# Annaba
# Batna
# Bejaia
# Oumache
# Chlef
# Constantine
# Hassi Messaoud
# Jijel
# Oran
# Setif
# Tamanrasset
# Tlemcen
# N'Djamena
# Alexandria
# Alexandria
# Asyut
# Aswan
# Cairo
# El Arish
# El Dabaa
# Hurghada
# Luxor
# Marsa Alam
# Mersa Matruh
# Saint Catherine
# Sharm el-Sheikh
# Sohag
# Taba
# Benghazi
# Sabha
# Tripoli
# Tajoura
# Agadir
# Casablanca
# Fes
# Marrakech
# Nador
# Oujda
# Rabat
# Tangier
# Tetouan
# Khartoum
# Port Sudan
# Djerba
# Enfidha
# Monastir
# Sfax
# Tabarka
# Tozeur
# Tunis
# Dakhla
# Laâyoune
# Luanda
# Lubango
# Gaborone
# Maun
# Francistown
# Kasane
# Maseru
# Antananarivo
# Antsiranana
# Mahajanga
# Nosy Be
# Toamasina
# Tolanaro
# Toliara
# Blantyre
# Lilongwe
# Dzaoudzi
# Maputo
# Beira
# Inhambane
# Nampula
# Pemba
# Tete
# Vilanculos
# Windhoek
# Walvis Bay
# Cape Town
# Durban
# Kempton Park
# Nelspruit
# Johannesburg
# Manzini
# Livingstone
# Lusaka
# Ndola
# Harare
# Victoria Falls
# Bulawayo
# Cotonou
# Bobo-Dioulasso
# Ouagadougou
# Douala
# Yaoundé
# Boa Vista Island
# Sal Island
# Santiago Island
# Sao Vicente Island
# Bangui
# Abidjan
# Banjul
# Accra
# Tamale
# Conakry
# Bissau
# Bubaque
# Monrovia
# Bamako
# Nouadhibou
# Niamey
# Abuja
# Kano
# Lagos
# Port Harcourt
# Enugu
# Dakar
# Freetown
# Lomé
# The Valley
# Antigua
# Nassau
# Chub Cay
# Exuma
# Freeport
# South Eleuthera
# Central Abaco
# Seawell
# Road Town
# Cayman Brac
# Georgetown
# Camagüey
# Cayo Coco
# Cayo Largo del Sur
# Cienfuegos
# Havana
# Holguín
# Santa Clara
# Santiago de Cuba
# Varadero
# Roseau
# Barahona
# La Romana
# Punta Cana
# Samana
# San Felipe de Puerto Plata
# Santiago de los Caballeros
# Santo Domingo
# Grenada
# Pointe-à-Pitre
# Cap-Haïtien
# Port-au-Prince
# Kingston
# Montego Bay
# Fort-de-France
# Gerald's
# Kralendijk
# Oranjestad, Aruba
# Philipsburg, Sint Maarten
# Willemstad, Curaçao
# Aguadilla
# San Juan
# St. Jean
# Saint Kitts
# Vieux-Fort
# Kingstown
# Canouan
# Port of Spain
# Tobago
# Providenciales
# Saint Thomas
# Saint Croix
# Belize City
# Liberia
# San José de Costa Rica
# San Salvador
# Flores
# Guatemala City
# La Ceiba
# Roatán
# San Pedro Sula
# Tegucigalpa
# Managua
# Bluefields
# Corn Island
# Puerto Cabezas
# Bocas del Toro
# David, Chiriquí
# Panama City
# Ferry Reach
# Calgary
# Edmonton
# Gander
# Halifax
# Hamilton
# Iqaluit
# Kelowna
# Moncton
# Montreal
# Montreal
# Ottawa
# Quebec City
# Regina
# Saskatoon
# St. John's
# Thunder Bay
# Toronto
# Toronto
# Vancouver
# Victoria
# Whitehorse
# Winnipeg
# Qeqqata
# Sermersooq
# Acapulco
# Aguascalientes
# Cancún
# Chihuahua
# Ciudad del Carmen
# Cozumel
# Culiacán
# Durango
# Guadalajara
# Hermosillo
# Huatulco
# Ixtapa
# León
# Loreto
# Los Cabos
# Manzanillo
# Mazatlán
# Mérida
# Mexico City
# Monterrey
# Morelia
# Oaxaca
# Puebla
# Puerto Vallarta
# Querétaro