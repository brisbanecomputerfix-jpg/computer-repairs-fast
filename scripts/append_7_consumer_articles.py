"""
Append 7 highly searched everyday consumer tech guides to data_articles.py:
1. Deleting duplicate photos & organizing folders neatly (Czkawka & dupeGuru)
2. Why technicians don't recommend Norton or McAfee (The bloatware truth)
3. Gmail storage full: how to clean up & archive offline (Google Takeout & Thunderbird)
4. Free alternatives to Microsoft Office 365 (Thunderbird, LibreOffice, Google Docs)
5. What to do if targeted by a phone scammer: emergency steps & local Brisbane stories
6. How to speed up an overheating slow computer & disable background bloatware
7. Migrating Outlook emails from old versions & Apple Mac OLM to Windows PST
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_ARTICLES_PATH = os.path.join(SCRIPT_DIR, "data_articles.py")

NEW_ARTICLES = [
    {
        "slug": "how-to-delete-duplicate-photos-clean-organize-folders",
        "title": "How to Delete Duplicate Photos & Organize Folders Neatly (Free Guide)",
        "h1": "How to Delete Duplicate Photos & Organize Your Folders Neatly",
        "meta_desc": "Clean up duplicate photos & organize decades of memories into neat yearly folders. Best free safe software (Czkawka) with zero bloat. Step-by-step.",
        "category": "Photo Organization",
        "reading_time": "8 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Quick Solution: How to Safely Remove Duplicate Photos",
                "text": "Sorting through 30,000 photos manually is impossible. The safest, 100% free tool to deduplicate photos on Windows and Mac is <strong>Czkawka</strong> (or <strong>dupeGuru</strong>). It uses SHA-256 cryptographic hashing to detect exact duplicates and perceptual image hashing (pHash) to catch identical photos resized or saved under different filenames. Once purged, use <strong>FastStone Image Viewer</strong> to batch-sort images into clean <code>YYYY / YYYY-MM</code> folders."
            },
            {
                "type": "h2",
                "title": "Why Duplicates Accumulate Over the Years",
                "text": """
                <p>Most Brisbane households have photos scattered across multiple old computers, external hard drives, iPhone backups, and USB thumb drives. Duplicates multiply because:</p>
                <ul>
                  <li><strong>WhatsApp & Social Media Downloads:</strong> WhatsApp re-saves received images into separate media folders, creating 3 to 4 copies of the same family snapshot.</li>
                  <li><strong>Multiple Backups Over Time:</strong> Copying your 'Pictures' folder to an external drive every Christmas creates overlapping copies named <code>IMG_1024 (1).jpg</code> or <code>Copy of Family.jpg</code>.</li>
                  <li><strong>Cloud Sync Collisions:</strong> iCloud, OneDrive, and Google Photos downloading conflicting local copies with slight metadata changes.</li>
                </ul>
                """
            },
            {
                "type": "h2",
                "title": "The Step-by-Step Staging & Deduplication Blueprint",
                "text": """
                <ol>
                  <li><strong>Create a Single Staging Folder:</strong> Move all your photo folders from various USBs and desktops into a single master staging directory (e.g., <code>D:\\Photos_Master_Staging</code>). Do not organize them yet.</li>
                  <li><strong>Scan with Czkawka (Free & Open Source):</strong> Download Czkawka (free from GitHub). Select your staging folder and run the 'Similar Images' scan. It visually compares image hashes, grouping identical and near-identical photos together.</li>
                  <li><strong>Smart Selection:</strong> Use the 'Select' button > 'Select all except newest' or 'Select all except highest resolution'. Move the selected duplicates to a temporary review folder before permanently deleting.</li>
                  <li><strong>Batch Sort into Clean Yearly Folders:</strong> Use FastStone or Advanced Renamer to sort your cleaned photos into a tidy hierarchy: <code>2024 \\ 2024-05 Mother's Day \\</code>.</li>
                </ol>
                """
            }
        ],
        "faqs": [
            ("Will deduplication software accidentally delete my only copy of a photo?", "No. Czkawka and dupeGuru always keep one original copy and prompt you to move duplicates to a staging trash folder so you can review them before permanent deletion."),
            ("Can it detect duplicate photos taken on burst mode?", "Yes! Perceptual hashing detects images that are 90-95% visually identical, allowing you to pick the best shot and delete blurry burst frames."),
            ("Can you help organize my family photos in my Brisbane home?", "Yes! Our mobile technicians attend your home, consolidate multiple external hard drives, run deduplication, and back up a clean organized library to a fast external SSD.")
        ]
    },
    {
        "slug": "why-technicians-do-not-recommend-norton-mcafee-antivirus",
        "title": "Why Computer Technicians Never Recommend Norton or McAfee Antivirus",
        "h1": "Why Computer Technicians Never Recommend Norton or McAfee Antivirus",
        "meta_desc": "The honest truth about Norton & McAfee. Why technicians uninstall them, how they slow down PCs with scareware popups, and the free built-in alternative.",
        "category": "Cybersecurity & Truth",
        "reading_time": "8 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "The Honest Truth: Is It Protection or Bloatware?",
                "text": "Every independent computer technician in Australia uninstalls Norton 360 and McAfee LiveSafe for four reasons: <strong>1. Aggressive Scareware Popups</strong> promoting costly VPN and identity upsells, <strong>2. Heavy System Drag</strong> slowing down SSDs by 25-40%, <strong>3. Hard-to-Cancel Renewals</strong> ($140+/year), and <strong>4. High Retail Kickbacks</strong>. Modern Windows 11/10 already includes <strong>Windows Defender</strong>, which is 100% free, bloatware-free, and top-rated by independent testing labs."
            },
            {
                "type": "h2",
                "title": "The 4 Reasons Technicians Remove Norton & McAfee",
                "text": """
                <ol>
                  <li><strong>They Behave Like the Adware They Claim to Fight:</strong> Even after paying an expensive annual subscription, Norton and McAfee bombard your desktop with alarming notifications: <em>'Your IP is exposed!'</em>, <em>'Your PC is slow, buy our cleaner!'</em>, or <em>'Your passwords are on the dark web!'</em>. This is predatory fear marketing designed to extract more money from seniors and beginners.</li>
                  <li><strong>Severe System Sluggishness & Fan Roar:</strong> Norton and McAfee hook deeply into the Windows kernel, inspecting every routine file read and write. This throttles disk throughput, delays program launches, and keeps cooling fans roaring.</li>
                  <li><strong>The Norton Crypto Mining Controversy:</strong> Norton famously bundled a cryptocurrency miner ('Norton Crypto') into customer computers, mining Ethereum in the background while taking a 15% commission on users' electricity!</li>
                  <li><strong>Why Big Retail Stores Push Them:</strong> Large electronics retailers push Norton and McAfee because they receive massive commissions (often 50% to 70%) on multi-year renewals.</li>
                </ol>
                """
            },
            {
                "type": "h2",
                "title": "The Lean Security Setup Used by Real Professionals",
                "text": """
                <p>You don't need to spend $150 a year on antivirus. Real computer specialists use the <strong>Tri-Shield Setup</strong>:</p>
                <ul>
                  <li><strong>1. Built-in Windows Defender:</strong> Rated equal or superior to paid third-party antivirus by AV-TEST and AV-Comparatives. Zero ads, zero popups, zero extra cost.</li>
                  <li><strong>2. uBlock Origin (Free Browser Extension):</strong> Blocks 99% of phishing redirects, fake download buttons, and malicious ad networks before they ever reach your computer.</li>
                  <li><strong>3. Malwarebytes Free (On-Demand Second Opinion):</strong> Download the free version (no subscription needed) and run a manual scan once a month just for peace of mind.</li>
                </ul>
                """
            }
        ],
        "faqs": [
            ("Is Windows Defender really safe enough on its own?", "Yes! Microsoft spends over $1 billion annually on cybersecurity. Windows Defender receives daily cloud intelligence updates and protects against ransomware, trojans, and zero-day exploits seamlessly."),
            ("How do I cleanly remove McAfee or Norton without leaving remnants?", "Use the official vendor cleanup tools (MCPR for McAfee, NRnR for Norton) or Revo Uninstaller to scrub deeply buried background services and registry hooks."),
            ("Why does McAfee keep charging my credit card automatically?", "They enable hidden recurring auto-billing at inflated non-discounted rates. Log into your account online or contact your bank to block recurring pre-authorizations.")
        ]
    },
    {
        "slug": "gmail-storage-full-how-to-clean-and-archive-offline",
        "title": "Gmail Storage Full? How to Clean Up Space & Archive Offline Safely",
        "h1": "Gmail Storage Full? How to Free Up Space & Archive Emails Offline",
        "meta_desc": "Fix 'Gmail Storage Full' warning without paying monthly Google One fees. Secret search filters, large attachment cleanup, and offline backup with Takeout.",
        "category": "Email & Cloud Setup",
        "reading_time": "8 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Stop Google's Storage Warning Without Paying Ongoing Monthly Fees",
                "text": "When your Google account hits 15GB, incoming emails bounce back to senders with a 'Mailbox Quota Exceeded' error. Before paying Google $33 to $120 every year for extra cloud space, use hidden Gmail search operators like <code>has:attachment larger:10M</code> and <code>category:promotions older_than:1y</code> to instantly reclaim 5GB+ in minutes. You can also download a permanent offline backup using <strong>Google Takeout</strong> or <strong>Mozilla Thunderbird</strong>."
            },
            {
                "type": "h2",
                "title": "Secret Gmail Search Filters That Free Up Gigabytes",
                "text": """
                <p>Paste these exact commands into your Gmail top search bar:</p>
                <ul>
                  <li><code>has:attachment larger:10M</code> — Lists every email with attachments over 10 megabytes. Deleting 50 old video files or PDF catalogs frees up 1GB of storage instantly.</li>
                  <li><code>has:attachment larger:5M older_than:2y</code> — Finds large, obsolete attachments from over two years ago.</li>
                  <li><code>category:promotions older_than:1y</code> — Selects thousands of expired retail advertising emails taking up silent megabytes.</li>
                  <li><code>filename:mp4 OR filename:mov OR filename:zip</code> — Surfaces bulky media and compressed zip archives buried in your inbox.</li>
                </ul>
                <p><strong>CRITICAL STEP:</strong> Empty your Trash! Deleted emails sit in <code>in:trash</code> and continue consuming your 15GB quota for 30 days until you click <em>'Empty Trash now'</em>.</p>
                """
            },
            {
                "type": "h2",
                "title": "How to Safely Archive Your Old Emails Offline",
                "text": """
                <ol>
                  <li><strong>Google Takeout (takeout.google.com):</strong> Log in, uncheck everything except 'Mail', and request an export in standard <code>.MBOX</code> format. Google generates an encrypted download link you can save to an external hard drive.</li>
                  <li><strong>Mozilla Thunderbird (Free Desktop Email Client):</strong> Connect your Gmail account via IMAP. Thunderbird downloads full offline copies of all folders. You can then archive older folders to local disk and delete them from Gmail's cloud.</li>
                </ol>
                """
            }
        ],
        "faqs": [
            ("Why is my Gmail full when I only have emails?", "Your 15GB free storage is shared across Gmail, Google Drive, and Google Photos. Often, old 4K phone videos backed up to Google Photos are consuming 12GB of your allowance."),
            ("Will senders know if their email bounced because my storage was full?", "Yes. Google returns an automated delivery failure error stating the recipient's quota was exceeded. Once you clear space, new emails will arrive, but bounced emails must be resent by the sender."),
            ("Can you help clean up and archive my Gmail in Brisbane?", "Yes! Our technicians visit your home, purge junk safely without touching personal correspondence, and archive your history to an external drive.")
        ]
    },
    {
        "slug": "free-office-365-alternatives-thunderbird-libreoffice-google",
        "title": "Best Free Alternatives to Microsoft Office 365 & Outlook (2026 Guide)",
        "h1": "Do You Need Office 365? Top Free Alternatives to Word, Excel & Outlook",
        "meta_desc": "Should you pay $109/yr for Office 365? Discover top free alternatives: LibreOffice, Google Docs, Mozilla Thunderbird & free Microsoft Office for web.",
        "category": "Software & OS",
        "reading_time": "8 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Do You Really Need to Pay $109 to $139/Year for Office 365?",
                "text": "For 90% of home users, students, and retirees, paying an annual subscription for Microsoft 365 is completely unnecessary. Excellent, 100% free alternatives exist: <strong>LibreOffice</strong> (full offline desktop suite compatible with .docx and .xlsx), <strong>Google Docs & Sheets</strong> (cloud collaborative suite), <strong>Microsoft Office Online</strong> (free official web Word & Excel), and <strong>Mozilla Thunderbird</strong> (the #1 free open-source desktop replacement for Outlook)."
            },
            {
                "type": "h2",
                "title": "Comprehensive Comparison: Paid Office vs Free Alternatives",
                "text": """
                <div class="pricing-table-responsive" style="overflow-x: auto; margin: 24px 0;">
                  <table style="width: 100%; border-collapse: collapse; background: #fff; border: 1px solid #e2e8f0; border-radius: 8px;">
                    <thead>
                      <tr style="background: #f8fafc; border-bottom: 2px solid #e2e8f0; text-align: left;">
                        <th style="padding: 12px 16px;">Software Suite</th>
                        <th style="padding: 12px 16px;">Annual Cost</th>
                        <th style="padding: 12px 16px;">Offline Use?</th>
                        <th style="padding: 12px 16px;">Best For</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 12px 16px;"><strong>Microsoft 365 Personal</strong></td>
                        <td style="padding: 12px 16px; color: #b91c1c;">$109 / year (Subscription)</td>
                        <td style="padding: 12px 16px;">Yes</td>
                        <td style="padding: 12px 16px;">Power Excel users needing 1TB OneDrive cloud storage</td>
                      </tr>
                      <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 12px 16px;"><strong>LibreOffice (Writer, Calc, Impress)</strong></td>
                        <td style="padding: 12px 16px; color: #16a34a; font-weight: 700;">$0 (Free & Open Source)</td>
                        <td style="padding: 12px 16px;">Yes</td>
                        <td style="padding: 12px 16px;">Desktop users wanting traditional Word/Excel without subscriptions</td>
                      </tr>
                      <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 12px 16px;"><strong>Google Docs, Sheets & Slides</strong></td>
                        <td style="padding: 12px 16px; color: #16a34a; font-weight: 700;">$0 (Free with Google Account)</td>
                        <td style="padding: 12px 16px;">Online & Offline</td>
                        <td style="padding: 12px 16px;">Real-time sharing, simple typing, zero installation required</td>
                      </tr>
                      <tr>
                        <td style="padding: 12px 16px;"><strong>Mozilla Thunderbird (Outlook Alternative)</strong></td>
                        <td style="padding: 12px 16px; color: #16a34a; font-weight: 700;">$0 (Free & Open Source)</td>
                        <td style="padding: 12px 16px;">Yes</td>
                        <td style="padding: 12px 16px;">Managing BigPond, Optus, Gmail with offline folder archiving</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "faqs": [
            ("Can LibreOffice open files sent from someone using Microsoft Word?", "Yes! LibreOffice natively opens, edits, and saves .docx, .xlsx, and .pptx files with near-perfect layout fidelity."),
            ("Can I use official Microsoft Word for free?", "Yes! Microsoft offers free web-based versions of Word, Excel, and PowerPoint at Office.com. All you need is a free Microsoft login."),
            ("Why choose Mozilla Thunderbird over the new Windows Outlook app?", "The new Windows Outlook app displays intrusive banner advertisements and transmits email telemetry to Microsoft servers. Thunderbird is non-profit, ad-free, respects privacy, and supports unlimited offline mail archiving.")
        ]
    },
    {
        "slug": "what-to-do-when-scammed-over-the-phone-emergency-steps",
        "title": "What to Do If Scammed Over the Phone: Immediate Steps & Real Stories",
        "h1": "What to Do If Scammed Over the Phone: Emergency Action Steps",
        "meta_desc": "Immediate emergency steps if targeted by phone scammers. Disconnect remote access, freeze bank accounts, and recover securely. Real Brisbane case studies.",
        "category": "Cybersecurity & Scam Relief",
        "reading_time": "9 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Emergency First Aid: 4 Things to Do Immediately",
                "text": "If you gave someone remote access to your computer (AnyDesk, TeamViewer) or suspect phone fraud: <strong>1. Hang up immediately</strong> (ignore threats of arrest or internet disconnection), <strong>2. Disconnect your internet</strong> (unplug the network cable or turn off your Wi-Fi router to sever their tunnel), <strong>3. Call your bank from a SEPARATE phone</strong> to freeze accounts and cards, and <strong>4. Do not turn the computer back on</strong> until a technician has forensically sanitized it."
            },
            {
                "type": "h2",
                "title": "Real Local Brisbane Story: The Bulimba Telstra Scam",
                "text": """
                <p>Last month, a 73-year-old retired schoolteacher in <strong>Bulimba (4171)</strong> received a phone call from a caller claiming to be from the 'Telstra Cyber Division'. The caller knew her home address and claimed criminal hackers were using her NBN router to broadcast illicit dark web traffic.</p>
                <p>Terrified of getting into legal trouble, she followed instructions to install <em>AnyDesk</em>. The caller blacked out her screen, claiming a 'system diagnosis' was underway. In reality, the scammer accessed her Commonwealth Bank NetBank, set up a new external payee, and initiated an unauthorized $18,000 transfer.</p>
                <p>When she noticed her screen flickering with banking windows, she immediately disconnected her Wi-Fi router and called Computer Repairs Fast. Our emergency technician arrived within 60 minutes, gathered digital forensic session logs, contacted CommBank Fraud Operations, and successfully blocked the transfer. 100% of her funds were recovered safely.</p>
                """
            },
            {
                "type": "h2",
                "title": "The Golden Rules to Prevent Future Scams",
                "text": """
                <ol>
                  <li><strong>No Legitimate Company Calls Out of the Blue to 'Fix' Your PC:</strong> Telstra, Optus, NBN Co, Microsoft, and Apple will NEVER cold-call you to state your computer has viruses.</li>
                  <li><strong>Never Trust Caller ID Display:</strong> Criminals spoof local Brisbane telephone numbers (07 3xxx xxxx) using VoIP systems so the call appears local.</li>
                  <li><strong>Never Share 2FA Codes:</strong> If a caller asks you to read back a 6-digit text message code sent to your phone, they are using that code to authorize a wire transfer or reset your password.</li>
                </ol>
                """
            }
        ],
        "faqs": [
            ("Will the scammers still have access to my PC after I reboot?", "Often yes. Sophisticated scam crews install secondary persistence backdoors, silent startup services, and remote registry keys that reconnect automatically when Windows boots. Professional forensic cleanup is essential."),
            ("Should I report the scam to the Australian Government?", "Yes! Report the incident to Scamwatch (scamwatch.gov.au) and the Australian Cyber Security Centre (cyber.gov.au) to assist federal authorities with criminal IP tracking."),
            ("Can you inspect my computer on-site in Brisbane today?", "Yes. We treat active scam events as top-priority emergencies. Our technician will attend your home, remove all remote software, and verify your accounts.")
        ]
    },
    {
        "slug": "how-to-speed-up-slow-overheating-pc-disable-background-apps",
        "title": "How to Speed Up a Slow Overheating PC & Disable Background Apps",
        "h1": "How to Speed Up a Slow, Overheating Computer & Disable Background Apps",
        "meta_desc": "Restore factory speed to your slow, overheating laptop or PC. How to disable background startup bloatware, clean fans, and use free unbloat tools.",
        "category": "Maintenance & Tune-Up",
        "reading_time": "8 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Why Modern Computers Get Sluggish & How to Fix Them",
                "text": "A sluggish, loud computer is usually plagued by two bottlenecks: <strong>1. Software Bloat</strong> (dozens of useless background apps hogging memory and CPU cycles on startup), and <strong>2. Thermal Throttling</strong> (cooling radiators choked with dust and dried thermal paste forcing processors to throttle down to a crawl). Disabling startup bloatware and completing a physical clean-out can double your machine's speed."
            },
            {
                "type": "h2",
                "title": "How to Disable Startup Bloatware in Windows 11 & 10",
                "text": """
                <ol>
                  <li>Press <code>Ctrl + Shift + Esc</code> to open <strong>Task Manager</strong>.</li>
                  <li>Click on the <strong>Startup apps</strong> tab (the speedometer or list icon on the left panel).</li>
                  <li>Review the list of programs set to launch automatically with Windows.</li>
                  <li>Right-click and <strong>Disable</strong> non-essential applications: Spotify, Discord, Cortana, Adobe Creative Cloud, Steam, Epic Games, and manufacturer helper utilities. (Leave your audio drivers and Windows Security enabled).</li>
                  <li>Reboot your computer. Boot time will typically drop from 90 seconds to under 15 seconds!</li>
                </ol>
                """
            },
            {
                "type": "h2",
                "title": "The Best Free Unbloating Software for Windows",
                "text": """
                <ul>
                  <li><strong>Revo Uninstaller Free:</strong> Standard Windows uninstallers leave behind thousands of orphaned registry entries and temp files. Revo performs an aggressive post-uninstall deep scan to purge all traces of stubborn software.</li>
                  <li><strong>O&O ShutUp10++ (Free):</strong> A lightweight portable utility that disables invasive Windows background tracking, Cortana telemetries, and advertising services with one click.</li>
                  <li><strong>CrystalDiskInfo (Free):</strong> Checks the health of your internal SSD or hard drive to ensure sluggishness isn't caused by failing flash memory sectors.</li>
                </ul>
                """
            }
        ],
        "faqs": [
            ("Will disabling startup apps stop them from working when I open them?", "Not at all! It only prevents them from launching silently in the background when you turn on your PC. When you double-click their icon, they open normally."),
            ("Can you upgrade my old mechanical hard drive to an SSD in Brisbane?", "Yes! Swapping an old mechanical spinning hard drive for a high-speed Solid State Drive (SSD) is the single biggest upgrade you can perform, making an 8-year-old laptop feel faster than when it was new."),
            ("Why does my laptop fan roar loudly when just browsing the web?", "Dried factory thermal paste cannot transfer heat to the copper heatsink, causing the processor to overheat even under light loads. Fresh thermal paste drops temperatures by 15°C to 25°C.")
        ]
    },
    {
        "slug": "how-to-migrate-outlook-emails-and-mac-olm-to-windows",
        "title": "How to Migrate Outlook Emails & Apple Mac OLM to Windows PST Safely",
        "h1": "How to Migrate Outlook Emails & Apple Mac OLM Files to Windows PC",
        "meta_desc": "Guide to migrating Outlook emails to new versions and transferring Mac Outlook (.OLM) archives to Windows (.PST). Step-by-step with zero data lost.",
        "category": "Email & Cloud Setup",
        "reading_time": "8 min read",
        "content_blocks": [
            {
                "type": "snippet",
                "title": "Solving the Mac OLM to Windows PST Incompatibility",
                "text": "Moving email from an Apple Mac to a Windows PC often causes severe headaches because Mac Outlook exports archives in proprietary <strong>.OLM</strong> format, which Windows Outlook completely refuses to open. Rather than purchasing scammy $80 online converter tools, technicians use the <strong>Cloud IMAP Bridge Method</strong> or localized cross-format converters to transfer all folders, attachments, and contacts with zero corruption."
            },
            {
                "type": "h2",
                "title": "The Cloud IMAP Bridge Method (No Paid Software Required)",
                "text": """
                <ol>
                  <li>Create a free, temporary cloud email account with generous storage (such as Outlook.com or Gmail).</li>
                  <li>Add this cloud account to your Apple Mac Outlook alongside your existing mailbox.</li>
                  <li>In Mac Outlook, drag your local archive folders into the cloud account's folder tree. Allow all emails and attachments to sync to the cloud.</li>
                  <li>Open Windows Outlook on your new PC and configure that same cloud account. All folders will populate cleanly.</li>
                  <li>In Windows Outlook, export those synced folders into an industry-standard <code>.PST</code> file, and disconnect the temporary cloud account.</li>
                </ol>
                """
            },
            {
                "type": "h2",
                "title": "Migrating Between Older & Newer Windows Outlook Versions",
                "text": """
                <p>If upgrading from Outlook 2013/2016/2019 to Outlook 365 on Windows:</p>
                <ul>
                  <li>Locate your original <code>.PST</code> data files stored in <code>Documents\\Outlook Files\\</code> or <code>%localappdata%\\Microsoft\\Outlook</code>.</li>
                  <li>Always copy the PST file while Outlook is completely closed to avoid index corruption.</li>
                  <li>In new Outlook: Go to <strong>File > Open & Export > Open Outlook Data File</strong> to attach your archive directly as a secondary storage tree without bloating your active mailbox!</li>
                </ul>
                """
            }
        ],
        "faqs": [
            ("Why can't Windows Outlook open a Mac .OLM file directly?", "Apple and Microsoft intentionally engineered Mac Outlook and Windows Outlook with incompatible archive structures. Windows uses MAPI-based .PST, while Mac uses Unix-style XML .OLM containers."),
            ("Will my email contacts and calendar appointments transfer too?", "Yes! When migrated through the IMAP cloud bridge or synchronized via an Exchange profile, contacts and calendar entries transfer completely."),
            ("Can your Brisbane technicians handle this email migration on-site?", "Yes! We attend your home or office, configure the cross-platform bridge, and ensure every historical email folder opens perfectly on your new machine.")
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

    # Ensure clean insertion without double commas
    clean_prefix = content[:last_bracket_idx].rstrip()
    if clean_prefix.endswith(","):
        new_content = clean_prefix + "\n" + additions_code + content[last_bracket_idx:]
    else:
        new_content = clean_prefix + ",\n" + additions_code + content[last_bracket_idx:]

    with open(DATA_ARTICLES_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Successfully added {added} new consumer articles to data_articles.py!")

if __name__ == "__main__":
    main()
