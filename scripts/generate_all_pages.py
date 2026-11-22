import os
import json
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCATIONS_DIR = os.path.join(ROOT_DIR, "locations")
SERVICES_DIR = os.path.join(ROOT_DIR, "services")
ARTICLES_DIR = os.path.join(ROOT_DIR, "articles")

os.makedirs(LOCATIONS_DIR, exist_ok=True)
os.makedirs(SERVICES_DIR, exist_ok=True)
os.makedirs(ARTICLES_DIR, exist_ok=True)

print(f"Project Root: {ROOT_DIR}")
