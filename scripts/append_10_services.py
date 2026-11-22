"""
Append 10 high-intent, long-tail commercial services to data_services.py:
1. Lenovo broken hinge & top casing frame repair
2. Wireless printer setup & Wi-Fi installation
3. BigPond, Optus & Outlook email migration
4. Old PC to new PC data migration & cloning
5. MYOB & Reckon accounting software migration
6. In-home computer lessons & senior tech consultations
7. Safe online banking & scam protection consultation
8. Computer physical dust cleaning & maintenance tune-up
9. Deleted file & lost folder recovery
10. Specialist software installation & app setup
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_SERVICES_PATH = os.path.join(SCRIPT_DIR, "data_services.py")

NEW_SERVICES = [
    {
        "slug": "lenovo-laptop-broken-hinge-casing-repair-brisbane",
        "title": "Lenovo Broken Hinge & Top Casing Frame Repair Brisbane | Flex & Yoga",
        "h1_main": "Lenovo Laptop Broken Hinge & Casing Repair Brisbane",
        "h1_sub": "Top Housing Frame, Broken Screw Sockets & Hinge Re-Anchoring",
        "meta_desc": "Brisbane Lenovo broken hinge & casing repairs. Reconstruct dislocated brass screw sockets, top housing frames & hinges on Flex 5 & Yoga. Call 0401 148 654.",
        "icon": "🔧",
        "category": "Hardware Reconstruction",
        "price_from": "From $170",
        "models": "Lenovo IdeaPad Flex 5, Yoga 7i/9i, ThinkPad Yoga, IdeaPad 3/5, Legion 5/7",
        "common_issues": [
            "Left or right hinge popped through the front display bezel or palmrest",
            "Brass knurled threaded screw inserts ripped out of thin plastic mounting posts",
            "Top lid housing (A-cover) flexing or cracking diagonally near the bottom corner",
            "Lid will not close flat without severe crunching sounds and display distortion",
            "Excessive hinge friction pulling the antenna cables and LCD ribbon tight"
        ],
        "pricing_table": [
            ("Lenovo Single Hinge Bracket Re-Anchoring (Resin Bonding)", "$170 – $220", "2 to 3 Hours"),
            ("Dual Hinge Reconstruction & Friction Nut Calibration", "$220 – $280", "Same Day"),
            ("Top Lid Housing (A-Cover) Replacement & Re-Assembly", "$280 – $360", "1 to 2 Days"),
            ("Palmrest & Keyboard Frame (C-Cover) Replacement", "$290 – $380", "1 to 2 Days"),
            ("Combination Hinge Repair + New Touchscreen Panel", "$380 – $480", "Same Day")
        ],
        "faqs": [
            ("Why do Lenovo IdeaPad and Yoga hinges break so easily?", "Lenovo anchors stiff steel hinges into a paper-thin plastic casing using tiny knurled brass nuts. Over 18-24 months, factory grease breaks down, hinge resistance increases, and the torque required to open the screen rips the brass sockets right out of the plastic."),
            ("Can you fix dislocated screw sockets without replacing the entire lid casing?", "Yes! In over 90% of cases, we reconstruct the damaged screw sockets using aerospace-grade steel-reinforced structural polymer compound. This creates a mounting base four times stronger than the original factory plastic."),
            ("Will my touchscreen still work after the hinge repair?", "Yes. We calibrate the opening tension of both hinges to ensure smooth, zero-resistance travel that prevents future stress fractures on the display glass.")
        ]
    },
    {
        "slug": "printer-setup-wifi-installation-brisbane",
        "title": "Wireless Printer Setup & Wi-Fi Installation Brisbane | Home & Office",
        "h1_main": "Wireless Printer Setup & Wi-Fi Installation Brisbane",
        "h1_sub": "HP, Brother, Canon & Epson Wireless Network & Scanning Setup",
        "meta_desc": "Fast wireless printer setup & Wi-Fi troubleshooting in Brisbane. Fix printer offline errors, network scanning & mobile printing for HP, Brother, Canon, Epson.",
        "category": "Home & Office IT",
        "price_from": "From $120",
        "models": "HP Envy/OfficeJet/SmartTank, Brother MFC/HL, Canon PIXMA/MAXIFY, Epson EcoTank",
        "common_issues": [
            "Printer constantly showing 'Offline' or 'Driver Unavailable' on Windows and Mac",
            "New NBN modem or mesh Wi-Fi installed and the printer stopped connecting",
            "Scanner not working or scanning to computer folder fails with network error",
            "iPhone, iPad, or Android phone unable to find AirPrint / Mopria printer",
            "Print jobs stuck in Windows print spooler queue and refusing to delete"
        ],
        "pricing_table": [
            ("Standard Wireless Printer In-Home Setup (1-2 Computers)", "$120 – $160", "45 to 60 Mins"),
            ("Multi-Device Office Network Printer Configuration (5+ PCs)", "$160 – $240", "1 to 2 Hours"),
            ("Network Scanner & Scan-to-Email / SMB Folder Setup", "$130 – $180", "45 Mins"),
            ("Printer Offline / Print Spooler Corrupted Driver Repair", "$120 – $150", "30 to 45 Mins"),
            ("USB to Wireless Print Server / Mesh Network Setup", "$150 – $210", "1 Hour")
        ],
        "faqs": [
            ("Why does my printer say 'Printer Offline' every time I try to print?", "Most home Wi-Fi routers change device IP addresses dynamically via DHCP. When your router reboots, your printer gets a new IP, but your computer still searches for the old one. We assign a permanent static IP and configure direct TCP/IP ports so it never goes offline again."),
            ("Can you set up my printer to print from our iPhones and iPads?", "Yes! We configure Apple AirPrint, Mopria, and universal network discovery so every phone, tablet, and laptop in your home can print wirelessly."),
            ("Do you install printer software without all the annoying bloatware?", "Yes. We install clean, lightweight OEM print and scan drivers without the intrusive subscription prompts, marketing popups, and trial software.")
        ]
    },
    {
        "slug": "bigpond-optus-email-outlook-migration-brisbane",
        "title": "BigPond & Optus Email to Outlook Migration Brisbane | Specialist Setup",
        "h1_main": "BigPond, Optus & Outlook Email Migration Brisbane",
        "h1_sub": "Transfer Old ISP Emails, PST Archives & Outlook 365 Setup",
        "meta_desc": "Migrate Telstra BigPond, Optus & TPG emails to Outlook 365 in Brisbane. Transfer old PST archives, fix send/receive errors & recover passwords with zero loss.",
        "category": "Email & Cloud Setup",
        "price_from": "From $140",
        "models": "Microsoft Outlook (Classic & 365), Apple Mail, Mozilla Thunderbird, Windows Mail",
        "common_issues": [
            "Telstra BigPond (@bigpond.com, @bigpond.net.au) rejecting passwords or failing sync",
            "OptusNet (@optusnet.com.au) shutting down or migrating mail platforms",
            "Corrupted .PST or .OST Outlook data file causing Outlook to crash on startup",
            "Decades of vital business and personal emails stuck on an old, dying computer",
            "Email accounts not syncing contacts, calendar events, and sent items across devices"
        ],
        "pricing_table": [
            ("Single Account ISP Email to Outlook / Gmail Migration", "$140 – $180", "1 Hour"),
            ("Full Multi-Account + PST Archive Historical Transfer (10GB+)", "$180 – $260", "1 to 2 Hours"),
            ("Outlook Corrupted Data File Repair (.PST / ScanPST)", "$130 – $170", "45 Mins"),
            ("Microsoft 365 Exchange Business Email Setup & Domain DNS", "$190 – $290", "1 to 2 Hours"),
            ("Cross-Device Sync Setup (PC, Mac, iPhone, iPad, Android)", "$140 – $190", "1 Hour")
        ],
        "faqs": [
            ("What happens if Telstra or Optus closes down my email account?", "If your ISP closes or changes your email service, you can lose years of tax records, receipts, and personal letters. We back up your entire mailbox into an offline archive file, set up a permanent modern address (such as Outlook or Gmail), and configure automated forwarding so you never miss an email."),
            ("Will I lose my old folders and sent emails during migration?", "Not a single email will be lost. We extract every folder, sent item, draft, contact list, and sub-folder and import them cleanly into your new email setup."),
            ("Can you help if I forgot my BigPond or Optus webmail password?", "Yes. We assist you through official ISP identity verification and password recovery channels right in your home to regain access to your account.")
        ]
    },
    {
        "slug": "old-pc-to-new-pc-data-migration-brisbane",
        "title": "Old PC to New PC Data Migration Brisbane | Full System Cloning",
        "h1_main": "Old PC to New PC Data Migration & Cloning Brisbane",
        "h1_sub": "Transfer All Files, Software, Bookmarks & Windows Profiles Fast",
        "meta_desc": "Move everything from your old computer to a new PC in Brisbane. Full data migration, drive cloning, photos, emails & software transfer with 0 data loss.",
        "category": "Data & Migration",
        "price_from": "From $160",
        "models": "Windows 7 / 8 / 10 to Windows 11, Intel / AMD PC, Apple Mac to PC, Mac to Mac",
        "common_issues": [
            "Bought a brand-new computer and don't know how to move files without losing data",
            "Old computer runs Windows 7/10 and has thousands of family photos scattered everywhere",
            "Browser bookmarks, saved passwords, and auto-fills missing on the new machine",
            "Desktop icons, documents, downloads, and Outlook archives need exact transfer",
            "Old PC is dying or failing to boot, making traditional copy-paste impossible"
        ],
        "pricing_table": [
            ("Standard User Data Transfer (Documents, Photos, Music, Desktop)", "$160 – $220", "1 to 2 Hours"),
            ("Complete System Drive Cloning (Bit-for-Bit Exact Replica)", "$180 – $250", "1 to 2 Hours"),
            ("Large Archive Transfer (500GB to 2TB+ Multi-Drive Migration)", "$220 – $310", "2 to 3 Hours"),
            ("Software Reinstallation & License Key Activation Setup", "$140 – $190", "1 Hour"),
            ("Secure Forensic Erase / Sanitization of Old Decommissioned PC", "$90 – $130", "45 Mins")
        ],
        "faqs": [
            ("Can you make my new computer feel exactly like my old one?", "Yes! We replicate your desktop layout, transfer your photos, music, downloads, documents, Chrome/Edge bookmarks, saved passwords, and printer connections so turning on your new machine feels completely familiar."),
            ("What if my old computer is extremely slow or won't boot into Windows?", "We remove the storage drive from your old computer and connect it directly to our high-speed forensic data transfer dock, bypassing the dead machine completely."),
            ("What do you do with my old computer once the transfer is complete?", "We can perform a certified DOD 5220.22-M secure data sanitization wipe on the old drive so you can safely sell, donate, or recycle the computer with complete privacy.")
        ]
    },
    {
        "slug": "myob-reckon-accounting-software-migration-brisbane",
        "title": "MYOB & Reckon Accounting Software Migration Brisbane | Database Setup",
        "h1_main": "MYOB & Reckon Software Migration Brisbane",
        "h1_sub": "Move Company Data Files, Multi-User Networks & Windows 11 Installs",
        "meta_desc": "Migrate MYOB v19, AccountRight & Reckon Accounts to new Windows 11 PCs in Brisbane. Company file setup, licensing transfer & historical data preserved.",
        "category": "Business Software",
        "price_from": "From $180",
        "models": "MYOB AccountRight (Classic v19, Live, Premier), Reckon Accounts Desktop, QuickBooks",
        "common_issues": [
            "Upgrading office workstations to Windows 11 and older MYOB v19 refuses to install",
            "Company file (.myo, .box, .qbw) locked or displaying 'file in use by another user' error",
            "Multi-user office network access failing between the host computer and staff PCs",
            "End of financial year (EOFY) backup failing or database verify reporting errors",
            "Migrating on-premise accounting software to cloud hybrid without losing past years"
        ],
        "pricing_table": [
            ("Single Workstation MYOB / Reckon Database Migration", "$180 – $240", "1 to 2 Hours"),
            ("Multi-User Office Network Accounting Host Configuration (2-5 PCs)", "$240 – $340", "2 to 3 Hours"),
            ("Corrupted Company File (.myo / .qbw) Database Verification Repair", "$190 – $280", "1 to 2 Hours"),
            ("Windows 11 Compatibility Patching for Legacy Desktop Accounting", "$170 – $220", "1 Hour"),
            ("Automated Triple-Redundant Accounting Backup Configuration", "$150 – $210", "1 Hour")
        ],
        "faqs": [
            ("Can older desktop MYOB v19 run reliably on a new Windows 11 computer?", "Yes! While official retail channels tell businesses they must pay ongoing cloud subscriptions, we configure specialized Windows 11 compatibility environments and PDF driver patches so legacy desktop versions run smoothly."),
            ("Will our business experience downtime during the accounting migration?", "We schedule accounting migrations during your low-volume periods or after-hours to ensure your staff experience zero interruption to customer billing and payroll."),
            ("Can multiple computers share the same accounting company file simultaneously?", "Yes. We configure dedicated peer-to-peer network permissions, Windows Defender firewall exceptions, and shared mapped network drives for seamless multi-user access.")
        ]
    },
    {
        "slug": "computer-lessons-senior-tech-consultations-brisbane",
        "title": "In-Home Computer Lessons & Senior Tech Support Brisbane | 1-on-1",
        "h1_main": "In-Home Computer Lessons & Senior Tech Consultations Brisbane",
        "h1_sub": "Patient 1-on-1 Training: Email, Internet, Photos & iPad Syncing",
        "meta_desc": "Patient, jargon-free computer lessons for Brisbane seniors & beginners. Learn email, safe browsing, iPad/iPhone syncing & photo management in your home.",
        "category": "Senior Tech Lessons",
        "price_from": "From $110",
        "models": "Windows Desktop/Laptop, Apple Mac, iPad, iPhone, Android Tablet & Smart TV",
        "common_issues": [
            "Feeling overwhelmed or anxious about modern computer updates and changing screens",
            "Need patient guidance on how to send photos, open attachments, and print documents",
            "Trouble navigating government portals (myGov, Medicare, Centrelink, Digital ID)",
            "Syncing photos between an iPhone/iPad and a computer without filling iCloud",
            "Learning how to safely use FaceTime, Zoom, or WhatsApp to video call family"
        ],
        "pricing_table": [
            ("1-Hour In-Home Personalized Computer Consultation", "$110 – $130", "1 Hour"),
            ("2-Hour Comprehensive In-Home Training Session", "$190 – $220", "2 Hours"),
            ("Handwritten Plain-English Step-by-Step Instruction Notes", "Included", "At Visit"),
            ("iPad / iPhone & Computer Photo Organization Session", "$120 – $160", "1 to 1.5 Hours"),
            ("myGov & Online Essential Services Secure Setup Tutorial", "$110 – $140", "1 Hour")
        ],
        "faqs": [
            ("Are your technicians patient with seniors who have little computer experience?", "Absolutely! Our technicians specialize in respectful, patient, plain-English coaching. We never use confusing technical jargon, we never rush you, and we write down customized step-by-step notes in your own notebook so you can review them anytime."),
            ("Can you help me organize thousands of messy family photos into folders?", "Yes! We can create tidy albums by year, holiday, or family member, show you how to find them easily, and back them up safely to a portable USB stick."),
            ("Do you come to retirement villages and aged care living in Brisbane?", "Yes. We regularly visit independent living villages, retirement communities, and private homes right across Greater Brisbane with zero travel fees.")
        ]
    },
    {
        "slug": "safe-online-banking-scam-protection-brisbane",
        "title": "Safe Online Banking & Scam Defense Consultation Brisbane | Security",
        "h1_main": "Safe Online Banking & Scam Protection Consultation Brisbane",
        "h1_sub": "Secure Browsers, Two-Factor Authentication & Phishing Defense",
        "meta_desc": "Protect your money with Brisbane safe online banking setup. Secure 2FA, password managers, anti-phishing & myGov protection. In-home consultation.",
        "category": "Cybersecurity & Banking",
        "price_from": "From $130",
        "models": "Commonwealth Bank, ANZ, NAB, Westpac, Bank of Queensland, Suncorp, myGov",
        "common_issues": [
            "Fear of bank fraud, unauthorized account withdrawals, or suspicious SMS links",
            "Using weak or repeated passwords across banking, email, and shopping websites",
            "Annoying, fake 'Your Computer Has Been Locked' full-screen browser popups",
            "Confusion around authenticating SMS codes and banking phone app tokens",
            "Securing myGov, Medicare, ATO, and superannuation portals from identity theft"
        ],
        "pricing_table": [
            ("In-Home Banking Security Audit & Hardened Browser Setup", "$130 – $170", "1 Hour"),
            ("Password Manager Setup & Master Password Training (Bitwarden)", "$140 – $190", "1 to 1.5 Hours"),
            ("Multi-Factor Authentication (2FA) & Authenticator App Setup", "$120 – $160", "1 Hour"),
            ("Browser Ad-Blocker, Anti-Phishing & Malicious Popup Shielding", "$110 – $140", "45 Mins"),
            ("Full Identity Theft Audit & Suspicious Remote Access Purge", "$170 – $240", "1.5 to 2 Hours")
        ],
        "faqs": [
            ("Will you ever ask for my banking PIN, password, or account balance?", "Never! We strictly adhere to privacy codes. When setting up secure login windows or passwords, our technician turns away or steps back while you enter your private credentials."),
            ("How do I know if an SMS from my bank is genuine or a scam?", "Banks in Australia will NEVER send you a text message containing an active clickable link asking you to log in or update details. We teach you how to verify genuine communications and install tools that block fake phishing links."),
            ("What should I do if a loud alarm sounds on my screen saying my PC is infected?", "Do NOT call the 1800 number on the screen. It is a fake browser popup designed to trick you into granting criminals remote access. Simply hold down your power button to turn off the computer and call us.")
        ]
    },
    {
        "slug": "computer-cleaning-maintenance-tuneup-brisbane",
        "title": "Computer Physical Cleaning & System Maintenance Tune-Up Brisbane",
        "h1_main": "Computer Physical Dust Cleaning & Maintenance Tune-Up Brisbane",
        "h1_sub": "Thermal Dust Extraction, Repasting, Bloatware Purge & Speed-Up",
        "meta_desc": "Deep physical dust cleaning & Windows tune-up in Brisbane. Eliminate overheating, noisy fans, thermal throttling & junk bloatware to restore factory speed.",
        "category": "Maintenance & Tune-Up",
        "price_from": "From $130",
        "models": "All Laptops (HP, Dell, Lenovo, Apple, ASUS, Acer), Desktop Towers, All-In-Ones",
        "common_issues": [
            "Laptop casing feels hot to touch and cooling fan runs constantly at maximum speed",
            "Desktop tower filled with dust bunnies, pet hair, and lint choking air filters",
            "Computer takes 5 to 10 minutes to boot up and open basic programs",
            "Dozens of startup apps, toolbars, and background bloatware consuming memory",
            "Thermal paste dried out into cracked chalk, causing severe CPU thermal throttling"
        ],
        "pricing_table": [
            ("Complete Laptop Internal Dust Extraction & Thermal Repaste", "$140 – $190", "1 Hour"),
            ("Desktop PC Deep Airflow De-Dusting, Cable Tidy & Repaste", "$130 – $180", "1 Hour"),
            ("Windows Software Optimization, Bloatware Purge & Startup Clean", "$120 – $160", "45 to 60 Mins"),
            ("Combination Ultimate Tune-Up (Full Physical Clean + Software Clean)", "$190 – $260", "1.5 to 2 Hours"),
            ("High-Performance Thermal Compound Upgrade (Arctic MX-6 / PTM7950)", "$40", "Add-on")
        ],
        "faqs": [
            ("How often should a laptop or desktop computer be physically cleaned?", "In Brisbane's humid climate, dust and pet hair combine with moisture to form dense mats inside cooling fans every 12 to 18 months. Regular cleaning prevents permanent silicon damage from heat fatigue."),
            ("Will cleaning out dust make my computer run faster?", "Yes! When cooling fans are clogged, your CPU throttles its clock speed down to protect itself from burning out. Removing dust and applying fresh thermal paste allows your processor to run at full turbo speed."),
            ("What is thermal paste and why does it need replacing?", "Thermal paste is a heat-conducting compound that sits between your processor and the metal heatsink. Over 2 to 3 years, it dries out into crusty powder, destroying heat transfer. We replace it with fresh high-conductivity compound.")
        ]
    },
    {
        "slug": "deleted-file-recovery-accidental-deletion-brisbane",
        "title": "Deleted File & Lost Folder Recovery Brisbane | Accidental Deletion",
        "h1_main": "Deleted File & Lost Folder Recovery Brisbane",
        "h1_sub": "Recover Emptied Recycle Bin, Missing Documents, Photos & USB Sticks",
        "meta_desc": "Recover accidentally deleted files, emptied Recycle Bin, and lost folders in Brisbane. Fast emergency retrieval for photos, Word docs, USBs & external drives.",
        "category": "Data Recovery",
        "price_from": "From $150",
        "models": "Internal SSD / HDD, External USB Hard Drives, USB Thumb Drives, SD / MicroSD Cards",
        "common_issues": [
            "Accidentally hit 'Delete' and emptied the Windows Recycle Bin or Mac Trash",
            "An entire folder of critical Word documents, tax invoices, or photos disappeared",
            "USB thumb drive showing 'You need to format the disk before you can use it'",
            "Cut-and-paste file transfer interrupted by a computer crash or disconnected cable",
            "Accidental quick format of an external backup drive or camera memory card"
        ],
        "pricing_table": [
            ("Accidentally Deleted File Retrieval (Recycle Bin / Quick Format)", "$150 – $220", "1 to 2 Hours"),
            ("Corrupted USB Flash Drive / SD Camera Memory Card Recovery", "$160 – $240", "Same Day"),
            ("Deep Sector Data Carving (Formatted / Missing Partition File Tables)", "$220 – $320", "1 to 2 Days"),
            ("Shadow Copy / Previous Versions Snapshot Volume Extraction", "$130 – $170", "45 Mins"),
            ("Transfer of Recovered Files to Secure New External Media", "$40 – $70", "At Service")
        ],
        "faqs": [
            ("What is the most important thing to do if I just deleted vital files?", "STOP USING THE COMPUTER IMMEDIATELY. When you delete a file, Windows does not erase the data—it merely marks that space as available. Every webpage you load, document you open, or update that downloads can overwrite those invisible sectors and destroy the files forever."),
            ("Can you recover files if the Recycle Bin has already been emptied?", "Yes! As long as new data has not overwritten the disk sectors, our deep raw forensic carving tools can locate and reconstruct the missing files."),
            ("How long does data recovery take?", "Standard accidental deletion cases are diagnosed and recovered within 1 to 3 hours in our Brisbane laboratory.")
        ]
    },
    {
        "slug": "software-installation-setup-services-brisbane",
        "title": "Software Installation & App Setup Services Brisbane | Office & Design",
        "h1_main": "Software Installation & Application Setup Brisbane",
        "h1_sub": "Microsoft 365, Adobe Suite, Antivirus & Driver Configuration",
        "meta_desc": "Professional software installation & app setup in Brisbane. Fast setup for Microsoft 365, Adobe Creative Cloud, AutoCAD, antivirus & printer drivers.",
        "category": "Software & OS",
        "price_from": "From $110",
        "models": "Windows 11 / 10, macOS (Apple Silicon & Intel), Microsoft Office 365, Adobe, AutoCAD",
        "common_issues": [
            "Microsoft 365 / Office installation fails with cryptic error code or won't activate",
            "Adobe Creative Cloud (Photoshop, Illustrator, Premiere) crashing on launch",
            "Antivirus software conflict blocking internet access or printer communication",
            "Audio, Wi-Fi, or graphics drivers corrupted after a failed Windows update",
            "Specialized engineering, medical, or accounting software setup requirements"
        ],
        "pricing_table": [
            ("Standard Single Application Installation & Licensing Activation", "$110 – $140", "30 to 45 Mins"),
            ("Complete Software Suite Setup (Microsoft 365, Adobe, Utilities)", "$140 – $190", "1 Hour"),
            ("Corrupted Driver Clean Removal & Fresh Factory Driver Reinstallation", "$120 – $160", "45 Mins"),
            ("Windows 11 Clean Installation & Driver Packaging", "$170 – $220", "1.5 Hours"),
            ("Virtual Machine / Dual-Boot / Specialized Sandbox Configuration", "$190 – $280", "1.5 to 2 Hours")
        ],
        "faqs": [
            ("Can you help me install Microsoft Office if I'm having trouble with my product key?", "Yes. We assist you with registering your genuine license key to your Microsoft account and install the full desktop applications (Word, Excel, Outlook, PowerPoint)."),
            ("Can you fix software that crashes immediately when opened?", "Yes. Most software crashes are caused by missing Visual C++ redistributables, corrupted .NET Framework installations, or conflicting graphic drivers, which we repair on-site."),
            ("Do you install pirated or cracked software?", "No. We strictly install legal, genuine software using your own licenses or assist you in purchasing official software at the best legitimate prices.")
        ]
    }
]

def main():
    with open(DATA_SERVICES_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    from data_services import SERVICES
    existing_slugs = {s["slug"] for s in SERVICES}

    added = 0
    services_to_add = []
    for s in NEW_SERVICES:
        if s["slug"] not in existing_slugs:
            services_to_add.append(s)
            added += 1
        else:
            print(f"Skipping existing service: {s['slug']}")

    if not services_to_add:
        print("All services already present in data_services.py")
        return

    last_bracket_idx = content.rfind("]")
    if last_bracket_idx == -1:
        print("Error: Could not find closing bracket in data_services.py")
        return

    additions_code = ""
    for s in services_to_add:
        additions_code += "    " + repr(s) + ",\n"

    new_content = content[:last_bracket_idx] + ",\n" + additions_code + content[last_bracket_idx:]

    with open(DATA_SERVICES_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Successfully added {added} new commercial services to data_services.py!")

if __name__ == "__main__":
    main()
