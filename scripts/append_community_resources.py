import sys
import os
import pprint

community_article = {
    'slug': 'free-brisbane-computer-courses-cyber-security-government-resources',
    'title': 'Free Computer Courses & Cyber Security Resources in Brisbane: Government & Community Guide',
    'h1': 'Free Brisbane Computer Courses, Cyber Security Training & Community Tech Help',
    'meta_desc': 'Discover free computer classes & cyber security resources in Brisbane. Brisbane City Council libraries, Be Connected, IDCARE, ACSC, SLQ & U3A seniors programs.',
    'category': 'Community & Digital Safety',
    'reading_time': '9 min read',
    'content_blocks': [
        {
            'type': 'snippet',
            'title': 'Free Digital Skills & Cyber Safety for Brisbane Households',
            'text': 'Looking to learn essential computer skills, build online confidence, or protect your family from aggressive phone and internet scams without paying expensive course fees? Brisbane households, seniors, job seekers, and small business owners have access to outstanding <strong>free local government and non-profit digital literacy programs</strong>. This directory provides verified links, phone numbers, and booking instructions for <strong>Brisbane City Council Libraries</strong>, the Australian Government’s <strong>Be Connected</strong> initiative, <strong>IDCARE</strong>, <strong>cyber.gov.au (ACSC)</strong>, <strong>State Library of Queensland</strong>, and <strong>U3A Brisbane</strong>.'
        },
        {
            'type': 'h2',
            'title': '1. Brisbane City Council Libraries: Free 1-on-1 Tech Help & Classes',
            'text': """
            <p>Brisbane City Council (BCC) operates <strong>33 public library branches</strong> across the city, providing completely free computer access, Wi-Fi, and digital literacy workshops for all Brisbane residents:</p>
            <ul>
              <li><strong>Free 1-on-1 Tech Help:</strong> Many local branches (including Indooroopilly, Carindale, Toowong, Chermside, Wynnum, Banyo, and Sunnybank Hills) offer personalised, booking-required sessions. You can bring in your laptop, tablet, or smartphone to sit down with a friendly library staff member and troubleshoot specific questions.</li>
              <li><strong>Beginner Digital Literacy Workshops:</strong> Group classes designed for absolute beginners. Topics cover using Windows, Apple macOS, touchscreen gestures, managing files, setting up email, and basic internet browsing.</li>
              <li><strong>Free Public Computers &amp; High-Speed Wi-Fi:</strong> Available at all 33 branches using your free Brisbane library card. The flagship <strong>Brisbane Square Library</strong> (266 George St in the CBD) features a dedicated <em>Learning Lounge</em> with extensive computer banks.</li>
              <li><strong>Online Tech Classes &amp; eBooks:</strong> Through Council's digital library portal, members get free access to LinkedIn Learning courses, digital magazines, and interactive learning tools.</li>
            </ul>
            <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px 18px; margin: 16px 0;">
              <strong>📍 How to Book &amp; Explore Events:</strong><br/>
              • Official Council Tech Portal: <a href="https://www.brisbane.qld.gov.au/things-to-see-and-do/council-venues-and-precincts/libraries/library-facilities-and-services/internet-computers-and-technology" target="_blank" rel="noopener noreferrer" style="color: var(--red-600); font-weight: 700; text-decoration: underline;">Brisbane Council Libraries Technology Services</a><br/>
              • What's On Events Calendar: <a href="https://www.brisbane.qld.gov.au/whats-on-and-events?venues=libraries" target="_blank" rel="noopener noreferrer" style="color: var(--red-600); font-weight: 700; text-decoration: underline;">BCC Library Events &amp; Workshops</a><br/>
              • Council 24/7 Telephone Contact: <strong>(07) 3403 8888</strong>
            </div>
            """
        },
        {
            'type': 'h2',
            'title': '2. Be Connected: Australian Government Free Digital Training for 50+',
            'text': """
            <p><strong>Be Connected</strong> is a flagship Australian Government initiative led by the <strong>eSafety Commissioner</strong> and the Department of Social Services, in partnership with the Good Things Foundation. It is specifically tailored to help Australians aged 50 and over thrive online with confidence and safety:</p>
            <ul>
              <li><strong>Self-Paced Interactive Online Modules:</strong> The official portal offers hundreds of short, jargon-free video tutorials and printable cheat sheets on:
                <ul>
                  <li>The absolute basics: using a mouse, keyboard, touchscreens, and connecting to Wi-Fi.</li>
                  <li>Setting up and safely navigating government services like <strong>myGov</strong>, Medicare, and Centrelink.</li>
                  <li>Safe online banking practices and verifying genuine bank apps.</li>
                  <li>Video calling grandchildren and family using Zoom, FaceTime, and WhatsApp.</li>
                  <li>Spotting dangerous SMS delivery scams, lottery frauds, and fake investment pop-ups.</li>
                </ul>
              </li>
              <li><strong>In-Person Community Network:</strong> Be Connected funds thousands of community organizations across Brisbane—including local neighborhood centres, Men's Sheds, and community halls—providing free digital mentors and small group classes.</li>
            </ul>
            <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px 18px; margin: 16px 0;">
              <strong>🌐 Official Be Connected Portal:</strong><br/>
              • Online Learning Website: <a href="https://beconnected.esafety.gov.au" target="_blank" rel="noopener noreferrer" style="color: var(--red-600); font-weight: 700; text-decoration: underline;">beconnected.esafety.gov.au</a><br/>
              • Free Support &amp; Enquiries Helpline: <strong>1300 795 897</strong>
            </div>
            """
        },
        {
            'type': 'h2',
            'title': '3. Australian Cyber Security Centre (cyber.gov.au) & Emergency Reporting',
            'text': """
            <p>The <strong>Australian Cyber Security Centre (ACSC)</strong>, a division of the Australian Signals Directorate (ASD), provides free authoritative cyber protection resources for households and everyday Australians:</p>
            <ul>
              <li><strong>Personal Cyber Security Handbook:</strong> A free, plain-English downloadable guide covering Multi-Factor Authentication (MFA), passkeys, strong passphrases, automated system updates, and safe Wi-Fi browsing.</li>
              <li><strong>Family &amp; Kids Online Safety:</strong> Age-specific guidance for parents of young children (5–10) and teenagers (10–15+) regarding gaming risks, social media privacy, and device boundaries.</li>
              <li><strong>ReportCyber Incident Reporting:</strong> If your identity, email, or internet banking has been compromised or you have suffered a financial cyber loss, you can report it directly to Australian federal and state law enforcement through ReportCyber.</li>
            </ul>
            <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px 18px; margin: 16px 0;">
              <strong>🛡️ ACSC Resources &amp; Hotline:</strong><br/>
              • Official Website: <a href="https://www.cyber.gov.au" target="_blank" rel="noopener noreferrer" style="color: var(--red-600); font-weight: 700; text-decoration: underline;">cyber.gov.au</a><br/>
              • Personal Cyber Security Guide: <a href="https://www.cyber.gov.au/protect-yourself-and-your-family" target="_blank" rel="noopener noreferrer" style="color: var(--red-600); font-weight: 700; text-decoration: underline;">Protect Yourself &amp; Family Online</a><br/>
              • 24/7 Australian Cyber Security Hotline: <strong>1300 CYBER1 (1300 292 371)</strong>
            </div>
            """
        },
        {
            'type': 'h2',
            'title': '4. IDCARE: Australia’s National Identity & Cyber Support Service (Non-Profit)',
            'text': """
            <p><strong>IDCARE</strong> is Australia and New Zealand's official independent charity and non-profit organization dedicated to helping individuals and small businesses navigate the aftermath of scams, data breaches, and identity theft:</p>
            <ul>
              <li><strong>Free Case Management:</strong> If a phone scammer tricked you into remote access software (AnyDesk, TeamViewer), or your driver’s licence, Medicare card, or passport details were leaked in a corporate breach, IDCARE assigns a dedicated Identity Security Counsellor to build an individual recovery plan.</li>
              <li><strong>Credit Ban Assistance:</strong> Expert guidance on placing free temporary credit bans across all three Australian credit reporting bureaus (Equifax, Experian, and illion) to block criminals from taking out fraudulent loans in your name.</li>
              <li><strong>Cyber First Aid Kit:</strong> Immediate triage steps to contain account takeovers and regain control of your digital identity.</li>
            </ul>
            <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px 18px; margin: 16px 0;">
              <strong>🤝 Free IDCARE Support Helpline:</strong><br/>
              • Official Website: <a href="https://www.idcare.org" target="_blank" rel="noopener noreferrer" style="color: var(--red-600); font-weight: 700; text-decoration: underline;">idcare.org</a><br/>
              • Free Support Line (Australia): <strong>1800 595 160</strong> (Monday – Friday, 7:00am – 7:00pm AEST)
            </div>
            """
        },
        {
            'type': 'h2',
            'title': '5. State Library of Queensland & The Edge (South Brisbane)',
            'text': """
            <p>Located in the heart of South Brisbane's Cultural Precinct (Stanley Place, South Brisbane QLD 4101), the <strong>State Library of Queensland (SLQ)</strong> and its innovative makerspace, <strong>The Edge</strong>, host regular community workshops:</p>
            <ul>
              <li><strong>Digital Literacy &amp; Inclusion Programs:</strong> Initiatives such as <em>Digital and You</em> helping Queenslanders develop digital confidence and career skills.</li>
              <li><strong>Creative Technology &amp; Hardware Labs:</strong> Hands-on open labs exploring coding, 3D printing, electronics, podcasting, and digital media production with support from experienced mentors.</li>
            </ul>
            <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px 18px; margin: 16px 0;">
              <strong>🏛️ State Library Details:</strong><br/>
              • Official Website: <a href="https://www.slq.qld.gov.au" target="_blank" rel="noopener noreferrer" style="color: var(--red-600); font-weight: 700; text-decoration: underline;">slq.qld.gov.au</a><br/>
              • The Edge Creative Hub: <a href="https://www.slq.qld.gov.au/visit/spaces/edge" target="_blank" rel="noopener noreferrer" style="color: var(--red-600); font-weight: 700; text-decoration: underline;">The Edge at SLQ</a><br/>
              • Telephone: <strong>(07) 3840 7666</strong>
            </div>
            """
        },
        {
            'type': 'h2',
            'title': '6. U3A Brisbane (University of the Third Age)',
            'text': """
            <p><strong>U3A Brisbane</strong> is a vibrant, non-profit community organisation run by volunteers for retirees and seniors. For an annual membership fee (under $50/year), members gain access to dozens of low-cost and free technology classes:</p>
            <ul>
              <li><strong>Device Classes:</strong> Practical, beginner-friendly courses for Apple iPad, iPhone, Android tablets, and Windows laptops.</li>
              <li><strong>Navigating Modern Tech:</strong> Understanding everyday online services, artificial intelligence concepts, digital photo management, and safe cloud backup.</li>
              <li><strong>Central &amp; Suburban Campuses:</strong> Classes are held at their City Campus (288 Edward St, Brisbane CBD) as well as suburban volunteer-run venues in Logan, Northside, and Westside.</li>
            </ul>
            <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px 18px; margin: 16px 0;">
              <strong>🎓 U3A Brisbane Details:</strong><br/>
              • Official Website: <a href="https://www.u3abrisbane.org.au" target="_blank" rel="noopener noreferrer" style="color: var(--red-600); font-weight: 700; text-decoration: underline;">u3abrisbane.org.au</a><br/>
              • Address: 288 Edward St, Brisbane QLD 4000<br/>
              • Telephone: <strong>(07) 3236 3055</strong>
            </div>
            """
        },
        {
            'type': 'h2',
            'title': '7. Scamwatch: National Anti-Scam Centre (ACCC)',
            'text': """
            <p>Run by the Australian Competition and Consumer Commission (ACCC), <strong>Scamwatch</strong> is the national clearinghouse for scam statistics, consumer warnings, and reporting:</p>
            <ul>
              <li><strong>Real-Time Threat Warnings:</strong> Read immediate alerts about trending phone impersonation scams targeting Telstra, Optus, Linkt toll road users, Australia Post delivery texts, and Australian bank customers.</li>
              <li><strong>Report a Scam:</strong> Submit details of scam calls, text messages, or deceptive websites to help authorities shut down fraudulent phone numbers and phishing servers.</li>
            </ul>
            <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px 18px; margin: 16px 0;">
              <strong>🚨 Official Scamwatch Portal:</strong><br/>
              • Official Website: <a href="https://www.scamwatch.gov.au" target="_blank" rel="noopener noreferrer" style="color: var(--red-600); font-weight: 700; text-decoration: underline;">scamwatch.gov.au</a>
            </div>
            """
        }
    ],
    'faqs': [
        (
            'Are Brisbane City Council library computer classes really completely free?',
            'Yes! All 1-on-1 tech help sessions and group digital literacy workshops hosted at Brisbane City Council libraries are 100% free of charge. You just need a free Brisbane library card or you can register when you attend.'
        ),
        (
            'What is the best free computer resource for seniors learning at home?',
            'The Australian Government\'s Be Connected platform (beconnected.esafety.gov.au) is by far the best free resource. It features step-by-step interactive lessons with large text and videos covering basic device use, myGov, and scam prevention.'
        ),
        (
            'Who should I call in Brisbane if I have been scammed or lost money online?',
            'First, immediately call your bank to freeze transactions. Second, call IDCARE on 1800 595 160 for free identity recovery support. Third, report the cyber incident to Australian police and authorities via cyber.gov.au or the ACSC hotline on 1300 292 371.'
        ),
        (
            'Can Computer Repairs Fast help with 1-on-1 in-home lessons if I need personal help?',
            'Yes! While public libraries and community hubs are fantastic for group learning, we provide private, patient 1-on-1 in-home computer coaching across Brisbane. We sit with you at your own desk, work on your exact machine, and write down step-by-step instructions in your notebook.'
        )
    ]
}

data_path = os.path.join(r"C:\Users\PC\.gemini\antigravity-ide\scratch\computer-repairs-fast\scripts", "data_articles.py")

with open(data_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add community article if not present
if 'free-brisbane-computer-courses-cyber-security-government-resources' not in content:
    last_bracket_idx = content.rfind(']')
    if last_bracket_idx != -1:
        prefix = content[:last_bracket_idx].rstrip()
        if not prefix.endswith(','):
            prefix += ',\n'
        else:
            prefix += '\n'
        
        article_str = "    " + pprint.pformat(community_article, indent=4, width=120) + "\n"
        content = prefix + article_str + content[last_bracket_idx:]
        print("Appended community article to data_articles.py!")

# 2. Enrich senior-computer-lessons-online-banking-safety-brisbane
additional_senior_text = """
<div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 12px; padding: 18px 20px; margin: 24px 0;">
  <h3 style="color: #166534; margin: 0 0 8px; font-size: 1.15rem;">Looking for Free Community Tech Classes in Brisbane?</h3>
  <p style="color: #1e293b; line-height: 1.55; margin: 0 0 10px;">
    In addition to our private 1-on-1 in-home lessons, Brisbane seniors have access to fantastic free resources:
  </p>
  <ul style="color: #1e293b; margin: 0 0 10px; padding-left: 20px;">
    <li><strong>Brisbane City Council Libraries:</strong> Free 1-on-1 tech appointments across 33 branches (Brisbane Square, Carindale, Toowong, Chermside, Indooroopilly).</li>
    <li><strong>Be Connected (beconnected.esafety.gov.au):</strong> Free online lessons for Australians aged 50+ on myGov, banking, and spotting scams. Helpline: 1300 795 897.</li>
    <li><strong>U3A Brisbane (u3abrisbane.org.au):</strong> Volunteer-run technology classes for seniors in the Brisbane CBD and suburbs.</li>
    <li><strong>IDCARE (idcare.org):</strong> Free identity and cyber support helpline on 1800 595 160 if you ever feel scammed.</li>
  </ul>
  <p style="margin: 0; font-size: 0.92rem;">
    Read our complete guide: <a href="/articles/free-brisbane-computer-courses-cyber-security-government-resources.html" style="color: #15803d; font-weight: 800; text-decoration: underline;">Free Brisbane Computer Courses &amp; Cyber Security Resources Guide ➔</a>
  </p>
</div>
"""

# Check if already added
if "Looking for Free Community Tech Classes in Brisbane?" not in content:
    target_str = "'slug': 'senior-computer-lessons-online-banking-safety-brisbane'"
    pos = content.find(target_str)
    if pos != -1:
        # Find the end of content_blocks list for this article
        block_end_marker = "'faqs': [('How long is a typical lesson?'"
        faq_pos = content.find(block_end_marker, pos)
        if faq_pos != -1:
            # Insert a new content block right before faqs
            new_block_str = f", {{'type': 'h2', 'title': 'Free Brisbane Community & Government Computer Classes', 'text': {repr(additional_senior_text)}}}"
            content = content[:faq_pos-3] + new_block_str + content[faq_pos-3:]
            print("Enriched senior-computer-lessons-online-banking-safety-brisbane with community resources!")

with open(data_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished updating data_articles.py!")
