"""
Append 8 more high-intent long-tail niche articles to data_articles.py.
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_ARTICLES_PATH = os.path.join(SCRIPT_DIR, "data_articles.py")

NEW_ARTICLES = [
    {
        "slug": "lenovo-laptop-broken-hinge-casing-repair-guide",
        "title": "Lenovo Broken Hinge & Top Casing Frame Repair Guide | Brass Socket Fix",
        "h1": "Lenovo Broken Hinge & Top Casing Frame Repair: How We Fix Broken Screw Sockets",
        "meta_desc": "Guide to fixing broken Lenovo hinges & cracked top casing frames. How we reconstruct broken brass screw sockets on Flex 5 & Yoga without costly lid swaps.",
        "category": "Lenovo Hardware",
        "reading_time": "7 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Quick Overview: Fixing Lenovo Hinge & Casing Fractures",
                "text": "When a Lenovo IdeaPad, Flex 5, or Yoga laptop lid pops open at the corner with grinding plastic sounds, the steel hinge has not broken—rather, the <strong>knurled brass threaded sockets have ripped out of the thin plastic top housing frame</strong>. Rather than spending $350+ to order an entire replacement lid assembly from overseas, independent technicians reconstruct the mounting sockets using <strong>aerospace-grade structural polymer bonding</strong> in 2 to 3 hours for <strong>$170 to $240</strong>."
            },
            {
                "type": "h2",
                "title": "The Anatomy of Lenovo's Plastic Screw Socket Failure",
                "text": """
                <p>To keep modern laptops lightweight, manufacturers anchor heavy-duty steel friction hinges into 1.2mm-thick plastic frames using knurled brass threaded inserts. Over 18 to 24 months:</p>
                <ol>
                  <li>Internal factory lithium grease inside the hinge barrel dries out, attracting airborne lint and dust.</li>
                  <li>Opening resistance increases by up to 40%, requiring significantly more torque to tilt the screen.</li>
                  <li>Every time you open the lid from a top corner, torsional twisting concentrates immense mechanical leverage directly on the three brass screw posts.</li>
                  <li>Eventually, the brittle plastic cylinder snaps, ejecting the brass insert and allowing the steel hinge arm to push outward through the casing or display glass.</li>
                </ol>
                """
            },
            {
                "type": "h2",
                "title": "The Professional Reconstruction Process (Why Super Glue Fails)",
                "text": """
                <p>Many laptop owners attempt to squeeze Super Glue (cyanoacrylate) into the cracked hinge gap. <strong>Never do this!</strong> Super Glue is extremely brittle under shear stress, snaps on the very first lid movement, and outgasses white cyanoacrylate fumes that permanently fog the LCD glass.</p>
                <p>Our workshop method:</p>
                <ul>
                  <li>We fully disassemble the display lid and remove the LCD screen to isolate the bare frame.</li>
                  <li>We re-align the original brass threaded nuts and anchor them into a high-tensile structural epoxy bed reinforced with micro-fibers.</li>
                  <li>We calibrate the friction locknut on the steel hinge using a torque gauge, reducing opening resistance by 15% so the hinge opens like butter without stressing the casing.</li>
                  <li>The cured compound has four times the tensile strength of factory injection-molded plastic.</li>
                </ul>
                """
            }
        ],
        "faqs": [
            ("Can you fix a Lenovo hinge that has pushed through the palmrest?", "Yes! We service both top display lid casings (A-covers) and bottom palmrest / keyboard frames (C-covers)."),
            ("Will my screen still close properly after the repair?", "Yes. Because we calibrate the hinge friction nuts and use low-profile structural bonding, the lid closes completely flush with factory alignment."),
            ("How long does the repaired hinge last?", "Our structural polymer reconstruction is permanently bonded. We back all hinge repairs with a 12-month parts and labor warranty.")
        ]
    },
    {
        "slug": "printer-offline-troubleshooting-wifi-setup-brisbane",
        "title": "Why Does My Printer Keep Saying Offline? Brisbane Wi-Fi Setup Guide",
        "h1": "Why Does My Printer Keep Saying 'Offline'? Brisbane Wi-Fi Setup Guide",
        "meta_desc": "Fix 'Printer Offline' errors on Windows & Mac in Brisbane. Wireless setup steps for HP, Brother, Canon & Epson printers with static IP & mesh fixes.",
        "category": "Home & Office IT",
        "reading_time": "7 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Why Printers Go Offline on Home & Office Networks",
                "text": "The dreaded 'Printer Offline' status on Windows and macOS is almost never caused by a broken printer. In 90% of cases, it happens because your Wi-Fi router assigned a <strong>new dynamic IP address via DHCP</strong> after a reboot or power outage, while your computer is still sending print data to the old IP. The permanent fix is locking your printer to a <strong>reserved static IP address</strong> and creating a direct standard TCP/IP port."
            },
            {
                "type": "h2",
                "title": "4 Permanent Steps to Stop 'Printer Offline' Errors",
                "text": """
                <ol>
                  <li><strong>Assign a Static IP via Printer Network Menu:</strong> Go into your printer's setup screen > Network / Wi-Fi > TCP/IP settings. Change IP configuration from Automatic (DHCP) to Manual/Static (e.g. 192.168.1.250, outside your router's normal lease pool).</li>
                  <li><strong>Create a Standard TCP/IP Port in Windows:</strong> Open Windows Control Panel > Devices & Printers > Right click your printer > Printer Properties > Ports tab > Add Port > Select 'Standard TCP/IP Port' > Type in the printer's fixed IP. This bypasses unreliable WSD (Web Services for Devices) ports.</li>
                  <li><strong>Disable SNMP Status Checking:</strong> In the TCP/IP port configuration, uncheck 'SNMP Status Enabled'. Misconfigured SNMP packets frequently fool Windows into thinking the printer is powered down.</li>
                  <li><strong>Disable Dual-Band Band Steering:</strong> If your NBN router merges 2.4GHz and 5GHz under one Wi-Fi name, cheap printer Wi-Fi chips drop connection. Bind the printer exclusively to the stable 2.4GHz band.</li>
                </ol>
                """
            }
        ],
        "faqs": [
            ("Why did my printer stop working after getting a new Telstra or Optus modem?", "New NBN modems have different network subnets, Wi-Fi passwords, and security protocols (WPA3). We reconfigure printer network profiles on-site in Brisbane in 30 minutes."),
            ("Can you set up wireless scanning directly to my desktop folder?", "Yes! We set up SMB network folders on your PC so one push of the scanner button sends a high-resolution PDF directly to your desktop."),
            ("Why do print jobs get stuck in the Windows queue?", "Corrupted print spooler service files trap pending jobs. We purge the <code>C:\\Windows\\System32\\spool\\PRINTERS</code> cache and restart the spooler service.")
        ]
    },
    {
        "slug": "telstra-bigpond-optus-email-migration-to-outlook-365-guide",
        "title": "How to Migrate Telstra BigPond & Optus Email to Outlook 365 (2026 Guide)",
        "h1": "How to Migrate Telstra BigPond & Optus Email to Outlook 365 (Step-by-Step)",
        "meta_desc": "Step-by-step guide to migrating Telstra BigPond & Optus email to Outlook 365. Export PST archives, avoid account closure, and fix sync errors safely.",
        "category": "Email & Cloud Setup",
        "reading_time": "8 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Safely Migrating Away from Dying Australian ISP Email",
                "text": "For over two decades, hundreds of thousands of Queenslanders have relied on Telstra BigPond (<code>@bigpond.com</code>, <code>@bigpond.net.au</code>) and OptusNet (<code>@optusnet.com.au</code>) email addresses. However, Australian telcos are progressively outsourcing or decommissioning legacy mail infrastructure. Migrating your decades of archived emails into <strong>Microsoft Outlook 365 or Gmail</strong> protects your tax records, invoices, and family memories permanently with zero data loss."
            },
            {
                "type": "h2",
                "title": "The Step-by-Step Safe Migration Roadmap",
                "text": """
                <ol>
                  <li><strong>Export Historical Offline PST Archive:</strong> In Outlook Classic, navigate to File > Open & Export > Import/Export > Export to a file > Outlook Data File (.pst). Select the root account folder and ensure 'Include subfolders' is checked. Save this backup file to an external USB drive.</li>
                  <li><strong>Provision Modern Cloud Mailbox:</strong> Create a modern, independent Microsoft 365 / Outlook.com or Google Workspace account with two-factor authentication (2FA).</li>
                  <li><strong>Import Archive & Re-Establish Folder Hierarchy:</strong> In the new profile, import the .PST file. All historical folders (Inbox, Sent Items, Archive, Receipts, Family) populate seamlessly into cloud storage.</li>
                  <li><strong>Configure Automated Server-Side Forwarding:</strong> Log into Telstra Webmail or Optus Webmail and set up automatic forwarding to your new address. Set up an auto-responder notifying contacts of your new email.</li>
                  <li><strong>Update Critical Service Logins:</strong> Systematically update your email on banking (CommBank, NAB, ANZ), myGov, utility providers, and medical clinics.</li>
                </ol>
                """
            }
        ],
        "faqs": [
            ("Will my BigPond emails disappear if I change internet providers?", "If you disconnect your Telstra home internet service, Telstra generally charges an ongoing annual mailbox fee or closes the account after a grace period. Migrating to an independent provider ensures you never lose access."),
            ("Can you migrate my BigPond emails on my computer at my Brisbane home?", "Yes! We attend your home, back up your complete email database, configure Outlook, and verify send/receive functionality on your PC, iPad, and phone."),
            ("What if I don't know my BigPond webmail password?", "We assist you through the Telstra identity verification workflow to reset your master password before performing the export.")
        ]
    },
    {
        "slug": "how-to-transfer-everything-from-old-pc-to-new-pc-safely",
        "title": "How to Transfer Everything From Old PC to New PC (Zero Data Loss)",
        "h1": "How to Transfer All Files, Photos & Settings From Old PC to New PC",
        "meta_desc": "Complete guide to transferring files, bookmarks, passwords, and programs from an old computer to a new Windows 11 PC safely with zero data lost.",
        "category": "Data & Migration",
        "reading_time": "7 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Moving to a New PC Without Losing a Single File",
                "text": "Bought an exciting new Windows 11 computer in Brisbane but stressed about how to transfer thousands of family photos, Chrome bookmarks, tax documents, and email accounts? Using generic cloud sync or USB copying often misses hidden browser profiles, Outlook archive files, and software product keys. A <strong>professional bit-level migration</strong> replicates your entire digital life with zero data loss."
            },
            {
                "type": "h2",
                "title": "Checklist: The 7 Hidden Items Most People Forget to Transfer",
                "text": """
                <ul>
                  <li><strong>Browser Autofill & Saved Passwords:</strong> Chrome, Edge, and Firefox credentials, auto-complete forms, and bookmark bars.</li>
                  <li><strong>Local Outlook .PST Files:</strong> Stored in <code>%localappdata%\\Microsoft\\Outlook</code>, containing decades of emails and contacts not stored on the mail server.</li>
                  <li><strong>Desktop Accounting & Tax Databases:</strong> Local MYOB (.myo), Quicken/Reckon (.qbw), or e-tax PDF archives.</li>
                  <li><strong>Custom Font & Photo Editing Libraries:</strong> Lightroom catalogs, RAW photo caches, and custom presets.</li>
                  <li><strong>Network Printer & Scanner Drivers:</strong> Pre-configured network port bindings for seamless printing.</li>
                  <li><strong>Windows Sticky Notes & Downloads Folder:</strong> Quick notes and important downloads stored on the local drive.</li>
                  <li><strong>Software License Keys:</strong> Extracting digital product keys (Office, Adobe, CAD) prior to decommissioning the old machine.</li>
                </ul>
                """
            }
        ],
        "faqs": [
            ("Can you move everything if my old PC has a black screen and won't turn on?", "Yes! As long as the internal storage drive is not physically smashed, we can extract the SSD or hard drive and copy all files directly onto your new computer."),
            ("How long does an in-home PC-to-PC data transfer take?", "Typically 1 to 2 hours depending on how many gigabytes of photos and documents you have."),
            ("Will my new computer be clean of bloatware after setup?", "Yes. We remove trial antivirus bloatware and unnecessary pre-installed sponsor apps from your new PC so it runs at peak factory speed.")
        ]
    },
    {
        "slug": "myob-reckon-migration-to-windows-11-guide",
        "title": "Migrating MYOB v19 & Reckon Accounts to Windows 11: Business Guide",
        "h1": "Migrating MYOB v19 & Reckon Accounts to Windows 11 Without Losing Data",
        "meta_desc": "How to move legacy MYOB v19, AccountRight & Reckon Accounts to Windows 11 without losing historical company ledger files. Step-by-step business guide.",
        "category": "Business Software",
        "reading_time": "8 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Running Classic Accounting Software on Modern Windows 11",
                "text": "Many Brisbane small businesses, trade contractors, and bookkeepers still rely on classic desktop accounting programs like <strong>MYOB AccountRight v19 or Reckon Accounts</strong> because of their speed and lack of costly monthly subscription fees. When upgrading office hardware to Windows 11, these 32-bit legacy apps often refuse to install or fail to generate PDF invoices. Our business IT service configures <strong>clean Windows 11 legacy environments</strong> with 100% database integrity."
            },
            {
                "type": "h2",
                "title": "Solving the Most Common Windows 11 MYOB v19 Errors",
                "text": """
                <ol>
                  <li><strong>The 'Unable to Create PDF Invoice' Error:</strong> MYOB v19 relies on an ancient Amyuni Document Converter virtual PDF driver that Windows 11 blocks due to driver signature enforcement. We install a certified virtual postscript print bridge that restores one-click email invoicing.</li>
                  <li><strong>The 'File Locked by Another User' Multi-User Bug:</strong> Modern Windows 11 SMB2/SMB3 network protocols handle file locking differently than Windows 7. We configure registry opportunistic locking (OpLocks) parameters on your host server so staff can collaborate without database lockups.</li>
                  <li><strong>Database Verification Read Errors:</strong> Prior to migration, we execute deep database optimization passes to repair index fragmentation and purge obsolete audit trail logs.</li>
                </ol>
                """
            }
        ],
        "faqs": [
            ("Will we lose historical accounting records from 10 years ago?", "Never. We perform a complete, verified backup of your company files (.myo, .box) and test the data verification routine to guarantee 100% mathematical ledger accuracy."),
            ("Can you set up automated daily accounting backups?", "Yes. We configure automated scripts that create encrypted daily backups to both an on-site USB drive and an offsite cloud vault every evening at 5:00 PM."),
            ("Do you assist Brisbane businesses on-site?", "Yes. Our commercial technicians service offices across Brisbane CBD, Milton, Fortitude Valley, Woolloongabba, Chermside, and all suburbs.")
        ]
    },
    {
        "slug": "senior-computer-lessons-online-banking-safety-brisbane",
        "title": "Senior Computer Lessons & Safe Online Banking Guide Brisbane",
        "h1": "Senior Computer Guide: Safe Online Banking, Passwords & Scam Protection",
        "meta_desc": "Essential computer guide for seniors: how to do online banking safely, avoid SMS & phone scams, spot fake bank websites, and set up simple passwords.",
        "category": "Senior Tech Lessons",
        "reading_time": "7 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Patient In-Home Computer Coaching for Brisbane Seniors",
                "text": "Technology should make life easier, not more stressful. For seniors and retirees in Brisbane, keeping up with constant computer updates, mobile apps, and confusing banking security requirements can feel overwhelming. Computer Repairs Fast provides <strong>patient, friendly, 1-on-1 in-home computer lessons</strong> across Brisbane. We explain everything in plain English, never rush, and write down clear instructions in your own notebook."
            },
            {
                "type": "h2",
                "title": "Top 5 Essential Skills Covered in In-Home Lessons",
                "text": """
                <ul>
                  <li><strong>Safe Online Banking:</strong> How to log in safely, verify you are on the genuine bank website (CommBank, NAB, ANZ, Westpac), and transfer funds to family with confidence.</li>
                  <li><strong>Spotting Fake Scam Calls & SMS Texts:</strong> Learning the golden rule: genuine banks, Telstra, and the Australian Taxation Office (ATO) will NEVER text you a clickable link or demand urgent payment via gift cards.</li>
                  <li><strong>Simple Password Management:</strong> Moving away from unsafe scraps of paper to a secure, easy-to-use password system that you won't forget.</li>
                  <li><strong>Sharing & Organizing Family Photos:</strong> How to transfer pictures from your smartphone or digital camera onto your computer and email them to grandchildren.</li>
                  <li><strong>Video Calling Family on FaceTime, Zoom & WhatsApp:</strong> One-touch video calling with crisp audio and video to stay connected with loved ones anywhere in the world.</li>
                </ul>
                """
            }
        ],
        "faqs": [
            ("How long is a typical lesson?", "Most seniors prefer a relaxed 1 to 1.5-hour session. This allows plenty of time to practice each step without feeling tired or overloaded."),
            ("Can family members attend the lesson too?", "Yes, absolutely! Family members are always welcome to sit in and take notes."),
            ("Do you charge travel fees to come to retirement villages in Brisbane?", "No. We charge a flat, transparent lesson rate with $0 travel fees right across Greater Brisbane.")
        ]
    },
    {
        "slug": "recovering-accidentally-deleted-files-and-folders-brisbane",
        "title": "How to Recover Accidentally Deleted Files & Emptied Recycle Bin (Brisbane)",
        "h1": "Accidentally Deleted Critical Files or Emptied Recycle Bin? Emergency Steps",
        "meta_desc": "Accidentally deleted critical files or emptied the Recycle Bin? Learn immediate emergency steps to prevent overwriting and recover lost photos & docs.",
        "category": "Data Recovery",
        "reading_time": "7 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Emergency First Aid for Accidentally Deleted Files",
                "text": "If you just deleted a critical folder of business spreadsheets, tax invoices, or irreplaceable family photos and emptied the Windows Recycle Bin or Mac Trash, <strong>DO NOT PANIC and STOP USING THE COMPUTER IMMEDIATELY</strong>. When Windows deletes a file, it does not destroy the data—it only removes the file's index entry in the Master File Table (MFT). Every second you continue browsing, streaming, or downloading risks permanently overwriting that space."
            },
            {
                "type": "h2",
                "title": "3 Critical Rules to Maximize File Recovery Chances",
                "text": """
                <ol>
                  <li><strong>Do Not Install Data Recovery Software on the Same Drive:</strong> Downloading and installing free recovery tools onto your C: drive writes thousands of new files directly over the deleted data you are trying to rescue.</li>
                  <li><strong>Power Down or Put Computer to Sleep:</strong> If the deleted files were on your main operating system SSD, shut down the computer immediately. Modern SSDs execute TRIM commands in the background, which permanently zeros out deleted blocks if left powered on.</li>
                  <li><strong>Seek Professional Sector-Level Extraction:</strong> Our Brisbane laboratory mounts your drive as a read-only write-blocked volume and uses deep raw file carving to reconstruct deleted files safely onto separate external media.</li>
                </ol>
                """
            }
        ],
        "faqs": [
            ("Can files still be recovered after the Recycle Bin is emptied?", "Yes! In the vast majority of cases, as long as new data hasn't overwritten the sectors, raw file signatures can be located and restored intact."),
            ("What types of files can you recover?", "We recover Word documents (.docx), Excel spreadsheets (.xlsx), PDF invoices, JPEG/RAW family photos, video files, Outlook data files (.pst), and accounting databases."),
            ("How quickly can you recover my files?", "Most accidental deletion recovery jobs in Brisbane are completed within 1 to 3 hours.")
        ]
    },
    {
        "slug": "pc-maintenance-cleaning-dust-removal-speed-guide",
        "title": "Computer Maintenance: Deep Dust Cleaning, Repasting & System Tune-Up",
        "h1": "Computer Maintenance: Deep Dust Extraction, Repasting & Speed Tune-Up",
        "meta_desc": "Why laptops & PCs slow down over time: clogged heatsink dust, dried thermal paste, and startup bloatware. Complete physical cleaning & maintenance guide.",
        "category": "Maintenance & Tune-Up",
        "reading_time": "7 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Why Modern Computers Need Regular Physical Maintenance",
                "text": "Is your laptop feeling burning hot on your lap, fans roaring like a jet engine, and software taking ages to load? Computers aren't like appliances—they actively inhale thousands of liters of ambient room air every day to stay cool. In Brisbane's humid climate, dust, pet hair, and airborne moisture form a thick blanket over copper cooling fins, forcing CPUs into severe <strong>thermal throttling</strong>. A professional physical de-dusting and thermal repaste restores factory cooling and whisper-quiet performance."
            },
            {
                "type": "h2",
                "title": "What Happens During a Complete Workshop Physical Clean",
                "text": """
                <ul>
                  <li><strong>Disassembly & Anti-Static Dust Extraction:</strong> We open the chassis and use ESD-safe high-pressure air and micro-brushes to extract impacted dust from cooling fan blades, exhaust fins, and intake vents.</li>
                  <li><strong>Thermal Paste Replacement:</strong> Factory thermal paste dries into hard, brittle chalk after 2 to 3 years. We remove old paste using 99% electronic-grade isopropyl alcohol and apply premium non-conductive compound (Arctic MX-6 or PTM7950 phase-change material).</li>
                  <li><strong>Fan Bearing Lubrication & Inspection:</strong> We inspect cooling fan bearings for wobble, friction, or hair entanglement, lubricating or replacing noisy fan motors.</li>
                  <li><strong>Software Bloatware Purge:</strong> We disable useless background startup programs, remove browser hijackers, and clean registry cruft so your PC boots in under 15 seconds.</li>
                </ul>
                """
            }
        ],
        "faqs": [
            ("How much cooler will my laptop run after cleaning?", "Most laptops experience temperature drops of 15°C to 25°C under load, eliminating thermal throttling and prolonging battery life."),
            ("Can dust inside a computer cause a fire or short circuit?", "Yes. Dust attracts moisture, which can bridge 19V power rail traces and cause electrical shorts on motherboards."),
            ("How often should I have my computer serviced in Brisbane?", "We recommend an annual physical clean-out, particularly if you have pets or live near high-traffic roads.")
        ]
    }
]

def main():
    with open(DATA_ARTICLES_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    from data_articles import ARTICLES
    existing_slugs = {a["slug"] for a in ARTICLES}

    added = 0
    articles_to_add = []
    for a in NEW_ARTICLES:
        if a["slug"] not in existing_slugs:
            articles_to_add.append(a)
            added += 1
        else:
            print(f"Skipping existing article: {a['slug']}")

    if not articles_to_add:
        print("All articles already present in data_articles.py")
        return

    last_bracket_idx = content.rfind("]")
    if last_bracket_idx == -1:
        print("Error: Could not find closing bracket in data_articles.py")
        return

    additions_code = ""
    for a in articles_to_add:
        additions_code += "    " + repr(a) + ",\n"

    new_content = content[:last_bracket_idx] + ",\n" + additions_code + content[last_bracket_idx:]

    with open(DATA_ARTICLES_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Successfully added {added} new articles to data_articles.py!")

if __name__ == "__main__":
    main()
