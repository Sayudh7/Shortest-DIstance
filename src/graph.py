# Nepal cities graph
# (x, y) = approximate screen position for visualization
# x goes left to right (west to east)
# y goes top to bottom (north to south)

cities = {
    # Central
    "Kathmandu":   (370, 170),
    "Hetauda":     (390, 245),
    "Bharatpur":   (305, 255),

    # Western
    "Pokhara":     (200, 195),
    "Butwal":      (245, 275),
    "Nepalgunj":   (145, 260),
    "Dhangadhi":   (80,  240),
    "Bhairahawa":  (230, 290),
    "Baglung":     (175, 200),
    "Beni":        (160, 215),
    "Damauli":     (255, 210),
    "Tulsipur":    (140, 245),
    "Dang": (175, 255),

    # Eastern
    "Biratnagar":  (590, 210),
    "Janakpur":    (480, 255),
    "Dharan":      (560, 190),
    "Itahari":     (575, 200),
    "Ilam":        (625, 170),
    "Birtamod":    (610, 195),
    "Damak":       (600, 200),

    # Southern (Terai)
    "Birgunj":     (355, 290),
    "Simara":      (365, 275),
    "Narayanghat": (300, 265),
    "Gaur":        (430, 285),

    # Far West
    "Mahendranagar": (55, 250),
    "Tikapur":       (100, 255),
}

roads = [
    # --- Kathmandu connections ---
    ("Kathmandu",   "Pokhara",      200),
    ("Kathmandu",   "Birgunj",      145),
    ("Kathmandu",   "Hetauda",       75),
    ("Kathmandu",   "Janakpur",     220),
    ("Kathmandu",   "Bharatpur",    145),
    ("Kathmandu",   "Narayanghat",  150),
    ("Kathmandu",   "Simara",       130),
    ("Kathmandu",   "Biratnagar",   465),
    ("Kathmandu",   "Dharan",       400),

    # --- Central ---
    ("Hetauda",     "Birgunj",       55),
    ("Hetauda",     "Janakpur",     150),
    ("Hetauda",     "Narayanghat",  100),
    ("Bharatpur",   "Narayanghat",   10),
    ("Bharatpur",   "Birgunj",       75),
    ("Simara",      "Birgunj",       25),
    ("Simara",      "Gaur",          80),
    ("Narayanghat", "Butwal",        95),
    ("Narayanghat", "Bharatpur",     10),

    # --- Western ---
    ("Pokhara",     "Butwal",        95),
    ("Pokhara",     "Baglung",       72),
    ("Pokhara",     "Damauli",       60),
    ("Pokhara",     "Beni",          90),
    ("Baglung",     "Beni",          35),
    ("Damauli",     "Bharatpur",     55),
    ("Butwal",      "Bhairahawa",    10),
    ("Butwal",      "Nepalgunj",    175),
    ("Bhairahawa",  "Nepalgunj",    170),
    ("Nepalgunj",   "Tulsipur",      35),
    ("Nepalgunj",   "Dhangadhi",    170),
    ("Tulsipur",    "Dhangadhi",    145),
    ("Dhangadhi",   "Tikapur",       45),
    ("Tikapur",     "Mahendranagar", 80),
    ("Dhangadhi",   "Mahendranagar", 90),
    ("Dang",        "Nepalgunj",    110),
    ("Dang",        "Butwal",       120),
    ("Dang",        "Tulsipur",      75),
    ("Dang",        "Bhairahawa",   130),
    ("Dang",        "Pokhara",      210),   

    # --- Eastern ---
    ("Janakpur",    "Gaur",         110),
    ("Janakpur",    "Biratnagar",   260),
    ("Janakpur",    "Itahari",      240),
    ("Biratnagar",  "Itahari",       15),
    ("Biratnagar",  "Dharan",        50),
    ("Biratnagar",  "Birtamod",      30),
    ("Itahari",     "Dharan",        13),
    ("Itahari",     "Damak",         25),
    ("Dharan",      "Ilam",          80),
    ("Birtamod",    "Ilam",          40),
    ("Birtamod",    "Damak",         15),
    ("Damak",       "Ilam",          45),
]