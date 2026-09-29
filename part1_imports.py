# Laborator: funcții, metode și importuri pe web
# Student: Caragia Denis SI-262

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

# Exercițiul 1
import requests
print(requests.__version__)

import urllib.request
# requests a avut nevoie de pip install pentru că este o bibliotecă externă,
# iar urllib face parte din biblioteca standard.