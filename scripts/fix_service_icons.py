import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_SERVICES_PATH = os.path.join(SCRIPT_DIR, "data_services.py")

icons_map = {
    'printer-setup-wifi-installation-brisbane': '🖨️',
    'bigpond-optus-email-outlook-migration-brisbane': '✉️',
    'old-pc-to-new-pc-data-migration-brisbane': '🔄',
    'myob-reckon-accounting-software-migration-brisbane': '📊',
    'computer-lessons-senior-tech-consultations-brisbane': '👨‍🏫',
    'safe-online-banking-scam-protection-brisbane': '🛡️',
    'computer-cleaning-maintenance-tuneup-brisbane': '🧹',
    'deleted-file-recovery-accidental-deletion-brisbane': '💾',
    'software-installation-setup-services-brisbane': '⚙️'
}

with open(DATA_SERVICES_PATH, "r", encoding="utf-8") as f:
    text = f.read()

for slug, icon in icons_map.items():
    needle = f"'slug': '{slug}',"
    replacement = f"'slug': '{slug}',\n        'icon': '{icon}',"
    if needle in text and f"'icon': '{icon}'" not in text:
        text = text.replace(needle, replacement)
        print(f"Added icon to {slug}")

with open(DATA_SERVICES_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("Icons successfully applied to data_services.py!")
