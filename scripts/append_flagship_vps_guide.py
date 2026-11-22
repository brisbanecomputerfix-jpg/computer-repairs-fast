"""
Append the complete flagship VPS, Coolify, Email Aliases, and Vibe Coding Security Guide
to data_articles.py.
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_ARTICLES_PATH = os.path.join(SCRIPT_DIR, "data_articles.py")

FLAGSHIP_ARTICLE = {
    "slug": "complete-vps-coolify-vibe-coding-security-guide",
    "title": "The Ultimate VPS, Coolify & Vibe Coding Security Guide (2026)",
    "h1": "How to Choose a VPS, Setup Coolify & Avoid Vibe Coding Nightmares",
    "meta_desc": "Complete guide to choosing a VPS, setting up Coolify on Hostinger, free Google email aliases, and avoiding vibe coding security nightmares.",
    "category": "DevOps & Web Security",
    "reading_time": "12 min read",
    "content_blocks": [
        {
            "type": "snippet",
            "title": "Mastering Self-Hosted Cloud Infrastructure & Safe Vibe Coding",
            "text": "Moving from expensive managed platforms (Vercel, Heroku, AWS) to a self-hosted <strong>Hostinger KVM VPS running Coolify</strong> can cut your cloud hosting bills by 80% while giving you unlimited domains, databases, and Docker containers. However, pairing self-hosting with modern <strong>vibe coding</strong> requires strict security hygiene to avoid real-world disasters like $15,000 surprise API bills, database ransomware, and server suspensions."
        },
        {
            "type": "h2",
            "title": "1. How to Choose the Best VPS Server (Domain, Database, Emails)",
            "text": """
            <p>A Virtual Private Server (VPS) gives you a dedicated slice of high-performance cloud hardware with root access. To run domains, databases, and Docker without lag, keep these parameters in mind:</p>
            <div class="pricing-table-responsive" style="overflow-x: auto; margin: 24px 0;">
              <table style="width: 100%; border-collapse: collapse; background: #fff; border: 1px solid #e2e8f0; border-radius: 8px;">
                <thead>
                  <tr style="background: #f8fafc; border-bottom: 2px solid #e2e8f0; text-align: left;">
                    <th style="padding: 12px 16px;">Workload</th>
                    <th style="padding: 12px 16px;">Minimum Specs</th>
                    <th style="padding: 12px 16px;">Recommended Specs</th>
                    <th style="padding: 12px 16px;">Why</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 12px 16px;"><strong>Light (1–2 Static Sites + Caddy)</strong></td>
                    <td style="padding: 12px 16px;">1 vCPU, 2GB RAM, 20GB NVMe</td>
                    <td style="padding: 12px 16px; font-weight: 700; color: #16a34a;">1 vCPU, 2GB RAM</td>
                    <td style="padding: 12px 16px;">Minimal memory footprint</td>
                  </tr>
                  <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 12px 16px;"><strong>Coolify / Docker + PostgreSQL + Next.js</strong></td>
                    <td style="padding: 12px 16px;">2 vCPU, 4GB RAM, 50GB NVMe</td>
                    <td style="padding: 12px 16px; font-weight: 700; color: var(--red-600);">4 vCPU, 8GB RAM, 100GB NVMe</td>
                    <td style="padding: 12px 16px;">Building Docker images spikes RAM; databases require memory caching</td>
                  </tr>
                  <tr>
                    <td style="padding: 12px 16px;"><strong>Heavy (Multi-Tenant, Redis, WordPress, Apps)</strong></td>
                    <td style="padding: 12px 16px;">4 vCPU, 8GB RAM</td>
                    <td style="padding: 12px 16px; font-weight: 700; color: var(--red-600);">4+ vCPU, 16GB RAM</td>
                    <td style="padding: 12px 16px;">Prevents Linux OOM (Out-of-Memory) kernel crashes</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h3 style="color: #0f172a; margin-top: 24px;">The 4 Golden Rules for VPS Selection:</h3>
            <ol>
              <li><strong>Always Choose KVM Virtualization:</strong> Avoid older OpenVZ virtualization. KVM provides true hardware isolation and full kernel Docker support.</li>
              <li><strong>Datacenter Proximity (Latency Matters):</strong> If your audience is in Brisbane or Australia, choose a datacenter in <strong>Sydney (15ms latency)</strong>. Hosting in the US or Europe adds 180ms–250ms latency to every database query.</li>
              <li><strong>NVMe SSD Storage (Not SATA):</strong> Databases (PostgreSQL, MySQL) perform thousands of input/output operations per second (IOPS). NVMe drives run 5x to 10x faster than standard SATA SSDs.</li>
              <li><strong>The 'Hosting Your Own Email' Trap (Port 25):</strong>
                <ul>
                  <li><em>Technician Reality:</em> <strong>Do NOT host your primary business email on a raw VPS.</strong></li>
                  <li>Most VPS providers (including Hostinger, Hetzner, DigitalOcean) block or heavily monitor Port 25 to prevent spam abuse. Furthermore, residential and budget VPS IP ranges are routinely blacklisted by Microsoft Outlook and Gmail spam filters.</li>
                  <li><em>Best Practice:</em> Host your web apps and databases on your VPS, but route your domain's email through dedicated providers like Google Workspace, Zoho Mail, or a transactional relay like Resend, SendGrid, or Amazon SES.</li>
                </ul>
              </li>
            </ol>
            """
        },
        {
            "type": "h2",
            "title": "2. How to Setup Coolify on Your Hostinger VPS",
            "text": """
            <p><a href="https://coolify.io" target="_blank" rel="noopener" style="color: var(--red-600); font-weight: 700;">Coolify</a> is an open-source, self-hosted platform (an open-source alternative to Vercel, Netlify, and Heroku). It allows you to connect GitHub repositories, spin up PostgreSQL/MySQL/Redis databases, manage free Let's Encrypt SSL certificates, and deploy apps using Docker with a single click.</p>
            
            <div style="background: #0f172a; color: #f8fafc; padding: 20px; border-radius: 8px; font-family: monospace; font-size: 0.85rem; line-height: 1.5; overflow-x: auto; margin: 24px 0;">
┌──────────────────────────────────────────────┐<br/>
│                Hostinger VPS                 │<br/>
│              (Ubuntu 24.04 LTS)              │<br/>
├──────────────────────────────────────────────┤<br/>
│           Coolify Management Engine          │<br/>
│                   (Port 8000)                │<br/>
├──────────────────────┬───────────────────────┤<br/>
│                      │                       │<br/>
┌────────────▼────────────┐ ┌───────▼─────────┐ ┌───────────▼───────────┐<br/>
│  Traefik Reverse Proxy  │ │   PostgreSQL    │ │    Next.js / Node     │<br/>
│  (Auto SSL / Port 443)  │ │    Database     │ │    Container App      │<br/>
└─────────────────────────┘ └─────────────────┘ └───────────────────────┘
            </div>

            <h3 style="color: #0f172a;">Option A: Hostinger's 1-Click OS Template (Easiest)</h3>
            <ol>
              <li>Log into your <strong>Hostinger hPanel</strong> &gt; Go to <strong>VPS</strong>.</li>
              <li>Under <strong>Operating System</strong>, search for the <strong>Coolify (Ubuntu 24.04)</strong> pre-made image.</li>
              <li>Click <strong>Install</strong>. Hostinger automatically provisions Docker, Coolify, and firewall rules in under 3 minutes.</li>
            </ol>

            <h3 style="color: #0f172a;">Option B: Manual CLI Installation on Clean Ubuntu 24.04</h3>
            <p>If installing on a standard Ubuntu server, connect via SSH using PowerShell or Terminal:</p>
            <div style="background: #1e293b; color: #e2e8f0; padding: 16px; border-radius: 8px; font-family: monospace; font-size: 0.9rem; margin-bottom: 20px;">
              <span style="color: #94a3b8;"># 1. SSH into your Hostinger VPS</span><br/>
              <span style="color: #38bdf8;">ssh</span> root@YOUR_VPS_IP<br/><br/>
              <span style="color: #94a3b8;"># 2. Update system packages</span><br/>
              <span style="color: #38bdf8;">apt update &amp;&amp; apt upgrade -y</span><br/><br/>
              <span style="color: #94a3b8;"># 3. Run the official automated Coolify installation script</span><br/>
              <span style="color: #38bdf8;">curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash</span>
            </div>

            <h3 style="color: #0f172a;">Post-Installation Setup:</h3>
            <ol>
              <li>Open your browser and navigate to: <code>http://YOUR_VPS_IP:8000</code>.</li>
              <li>Register your administrator account.</li>
              <li><strong>Point Your Domain to Coolify:</strong> In your DNS manager (Hostinger, Cloudflare, etc.), create an <strong>A Record</strong>:
                <ul>
                  <li><code>Host:</code> <code>coolify</code> (or <code>@</code>)</li>
                  <li><code>Points to:</code> <code>YOUR_VPS_IP</code></li>
                </ul>
              </li>
              <li>In Coolify's settings, assign your domain (e.g. <code>https://coolify.yourdomain.com</code>). Coolify automatically provisions a free Let's Encrypt SSL certificate via its built-in Traefik reverse proxy.</li>
              <li>You can now click <strong>+ Create New Resource</strong> to deploy Git repos, WordPress, or databases.</li>
            </ol>
            """
        },
        {
            "type": "h2",
            "title": "3. How to Create Free Email Aliases on Your Google Account",
            "text": """
            <p>An alias lets you receive emails sent to multiple addresses (like <code>info@</code>, <code>sales@</code>, <code>billing@</code>) inside a single inbox <strong>without paying for additional user licenses</strong>.</p>

            <h3 style="color: #0f172a;">Method 1: The Free Personal Gmail Trick (+ and .)</h3>
            <p>If using standard <code>@gmail.com</code>, Google provides built-in aliases:</p>
            <ul>
              <li><strong>The Plus Sign Trick:</strong> If your address is <code>john@gmail.com</code>, you automatically own <code>john+banking@gmail.com</code>, <code>john+newsletters@gmail.com</code>, and <code>john+shopping@gmail.com</code>.
                <p><em>Why this is useful:</em> Use <code>john+banking@gmail.com</code> when registering with your bank. In Gmail Settings &gt; <strong>Filters and Blocked Addresses</strong>, set a rule: <em>'If to john+banking, apply label Banking and mark important'</em>. If spam ever arrives addressed to that alias, you know a specific company leaked or sold your email!</p>
              </li>
              <li><strong>The Dot Trick:</strong> <code>j.ohn@gmail.com</code> and <code>jo.hn@gmail.com</code> all route to <code>john@gmail.com</code>.</li>
            </ul>

            <h3 style="color: #0f172a;">Method 2: Google Workspace (Custom Business Domain — Up to 30 Free Aliases per User)</h3>
            <p>If you pay for one Google Workspace account ($6/mo for <code>admin@yourdomain.com</code>):</p>
            <ol>
              <li>Go to the <strong>Google Admin Console</strong> (<a href="https://admin.google.com" target="_blank" rel="noopener">admin.google.com</a>).</li>
              <li>Navigate to <strong>Directory &gt; Users</strong> &gt; Click your primary user.</li>
              <li>Under <strong>User information</strong>, click <strong>Add Alternate Emails (Email alias)</strong>.</li>
              <li>Add up to 30 aliases for free: <code>info@yourdomain.com</code>, <code>support@yourdomain.com</code>, <code>billing@yourdomain.com</code>, <code>contact@yourdomain.com</code>.</li>
              <li>Click <strong>Save</strong>. All mail sent to those addresses lands in your main inbox.</li>
              <li>To reply as that alias: In Gmail &gt; Settings &gt; <strong>Accounts and Import</strong> &gt; <strong>Send mail as</strong> &gt; Add the alias address.</li>
            </ol>

            <h3 style="color: #0f172a;">Method 3: Cloudflare Email Routing to Free Personal Gmail (100% Free Custom Domain Email)</h3>
            <p>If you have a domain and don't want to pay Google Workspace fees:</p>
            <ol>
              <li>Move your domain DNS to <strong>Cloudflare</strong> (Free).</li>
              <li>Go to <strong>Email Routing</strong> &gt; Enable Email Routing.</li>
              <li>Create custom addresses: e.g. <code>hello@yourdomain.com</code> -&gt; forwards to <code>yourname@gmail.com</code>.</li>
              <li>Cloudflare delivers incoming business emails to your free Gmail inbox with zero monthly cost.</li>
            </ol>
            """
        },
        {
            "type": "h2",
            "title": "4. Is It Safe to Create Websites with 'Vibe Coding'?",
            "text": """
            <p><strong>'Vibe coding'</strong> (coined by AI researchers like Andrej Karpathy) describes building applications by iteratively prompting LLMs to write all the code, accepting the output based on visual and functional vibes without reading or understanding every line of syntax.</p>
            
            <h3 style="color: #0f172a;">The Verdict:</h3>
            <ul>
              <li><strong>Static Websites, Landing Pages &amp; Portfolios:</strong> <span style="color: #16a34a; font-weight: 700;">VERY SAFE &amp; HIGHLY EFFECTIVE.</span> For HTML, CSS, JavaScript animations, landing pages, and marketing sites, vibe coding is transformative. There are no databases or server backdoors to breach.</li>
              <li><strong>Full-Stack Apps, User Authentication &amp; Payment Systems:</strong> <span style="color: #dc2626; font-weight: 700;">HAZARDOUS WITHOUT SECURITY REVIEWS.</span> AI models are trained on internet code repositories, which include millions of insecure code snippets.</li>
            </ul>

            <h3 style="color: #0f172a;">Common Security Bugs AI Introduces in Vibe-Coded Apps:</h3>
            <div class="pricing-table-responsive" style="overflow-x: auto; margin: 24px 0;">
              <table style="width: 100%; border-collapse: collapse; background: #fff; border: 1px solid #e2e8f0; border-radius: 8px;">
                <thead>
                  <tr style="background: #f8fafc; border-bottom: 2px solid #e2e8f0; text-align: left;">
                    <th style="padding: 12px 16px;">Vibe Coding Trap</th>
                    <th style="padding: 12px 16px;">What the AI Commonly Writes</th>
                    <th style="padding: 12px 16px;">The Disaster It Causes</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 12px 16px;"><strong>Hardcoded Credentials</strong></td>
                    <td style="padding: 12px 16px;"><code>const key = "sk-proj-948194..."</code> written directly in frontend JS</td>
                    <td style="padding: 12px 16px; color: #dc2626; font-weight: 700;">Scraped by bots within 90 seconds of pushing to GitHub; thousands billed</td>
                  </tr>
                  <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 12px 16px;"><strong>IDOR (Broken Authorization)</strong></td>
                    <td style="padding: 12px 16px;"><code>/api/invoices?id=1284</code> fetches invoice without session check</td>
                    <td style="padding: 12px 16px; color: #dc2626; font-weight: 700;">Any user can change 1284 to 1285 and read another customer's invoice</td>
                  </tr>
                  <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 12px 16px;"><strong>Unsanitized SQL / NoSQL</strong></td>
                    <td style="padding: 12px 16px;"><code>db.query(`SELECT * FROM users WHERE user = '${input}'`)</code></td>
                    <td style="padding: 12px 16px; color: #dc2626; font-weight: 700;">SQL Injection wipes or leaks the entire database table</td>
                  </tr>
                  <tr>
                    <td style="padding: 12px 16px;"><strong>No Rate Limiting</strong></td>
                    <td style="padding: 12px 16px;">Open <code>/api/generate-ai</code> endpoint accessible to the public</td>
                    <td style="padding: 12px 16px; color: #dc2626; font-weight: 700;">Attackers script automated loops, draining your OpenAI API credits</td>
                  </tr>
                </tbody>
              </table>
            </div>
            """
        },
        {
            "type": "h2",
            "title": "5. What Is the Worst Nightmare If You Don't Follow These Steps?",
            "text": """
            <p>If security best practices are ignored while running a VPS, managing domains, or deploying vibe-coded apps, here are the real-world scenarios:</p>

            <h3 style="color: #b91c1c;">Nightmare 1: The $15,000 API &amp; Cloud Billing Shock Overnight</h3>
            <ul>
              <li><strong>How it happens:</strong> You vibe-code a web tool that calls an AI or cloud API. The AI places the secret key in your <code>.env</code> or client file. You push the repository to GitHub as 'public', or you fail to put a rate-limiter on your backend endpoint.</li>
              <li><strong>The consequence:</strong> Automated bots scrape GitHub within seconds. They consume your API quota, spin up large cloud instances, and run up thousands of dollars before you wake up.</li>
            </ul>

            <h3 style="color: #b91c1c;">Nightmare 2: Automated Database Ransomware Wipes</h3>
            <ul>
              <li><strong>How it happens:</strong> You deploy PostgreSQL or MongoDB on your VPS. You map port <code>5432</code> or <code>27017</code> to <code>0.0.0.0</code> (open to the entire public internet) using a weak password or default configuration.</li>
              <li><strong>The consequence:</strong> Automated port scanners detect the open database within hours. A bot script connects, drops every table, exports your data, and leaves behind a single table named: <code>README_TO_RECOVER_YOUR_DATA</code> demanding 0.2 Bitcoin.</li>
            </ul>

            <h3 style="color: #b91c1c;">Nightmare 3: Your VPS Suspended as a 'Spambot / DDoS Zombie'</h3>
            <ul>
              <li><strong>How it happens:</strong> You run an unpatched Docker container or misconfigured PHP script. Attackers exploit a known vulnerability, gain root access, install a botnet script, and use your VPS to blast 800,000 spam emails per hour.</li>
              <li><strong>The consequence:</strong> Spamhaus blacklists your server IP and your business domain. Hostinger's abuse team immediately suspends your VPS service to protect network reputation, taking down all your websites and client apps without warning.</li>
            </ul>

            <h3 style="color: #b91c1c;">Nightmare 4: Domain Reputation Destruction (DNS Spam Hell)</h3>
            <ul>
              <li><strong>How it happens:</strong> You set up a VPS email server without configuring proper SPF (Sender Policy Framework), DKIM (DomainKeys Identified Mail), and DMARC (Domain-based Message Authentication) records.</li>
              <li><strong>The consequence:</strong> Spammers spoof your domain to send phishing emails. Within days, Google and Microsoft mark your domain as an untrusted spam source. Even legitimate invoices you email to clients go straight to their Junk folders.</li>
            </ul>

            <div style="background: #f0fdf4; border: 2px solid #86efac; border-radius: 12px; padding: 24px; margin-top: 32px;">
              <h3 style="color: #166534; margin-top: 0; font-size: 1.25rem;">The 5-Point Security Checklist for Your VPS &amp; Vibe-Coded Projects:</h3>
              <ol style="margin-bottom: 0; color: #1e293b; line-height: 1.6;">
                <li><strong>UFW Firewall on the VPS:</strong> Only leave ports <code>80</code> (HTTP), <code>443</code> (HTTPS), and your custom SSH port open. Never expose database ports (<code>5432</code>, <code>3306</code>, <code>6379</code>) to the public internet—databases should communicate with Coolify apps internally over Docker's bridge network (<code>127.0.0.1</code> or container names).</li>
                <li><strong>Disable Root Password SSH:</strong> In <code>/etc/ssh/sshd_config</code>, set <code>PasswordAuthentication no</code> and log in exclusively using <strong>SSH Public Key Authentication</strong>.</li>
                <li><strong>Set Hard Spending Limits:</strong> In your OpenAI, Anthropic, or AWS dashboards, configure strict monthly billing caps (e.g., maximum $50/month) so runaway loops can never bill surprise thousands.</li>
                <li><strong>Audit Your Environment Variables:</strong> Never expose variables without a private prefix. Secrets belong exclusively in server-side runtime environments, never compiled into client-side browser bundles.</li>
                <li><strong>3-2-1 Automated Backups:</strong> Configure Coolify or your VPS to dump databases nightly to an offsite S3-compatible bucket (such as Cloudflare R2 or Backblaze B2).</li>
              </ol>
            </div>
            """
        }
    ],
    "faqs": [
        ("Why do developers choose Coolify over Vercel or Heroku?", "Vercel and Heroku charge steep bandwidth fees and serverless execution markups as apps grow. Coolify gives you the exact same Git-push-to-deploy workflow on your own fixed-price VPS with zero per-user or bandwidth surcharges."),
        ("Can I host multiple different domains and databases on one Hostinger VPS?", "Yes! Coolify's built-in Traefik reverse proxy routes traffic for dozens of independent domain names and automatically manages separate SSL certificates for each site on a single VPS."),
        ("What is the single most important security rule when vibe coding with AI?", "Never put API keys or secrets in source code files, and always run authorization checks on database endpoints. Verify that a user actually owns the record they are trying to read or delete.")
    ]
}

def main():
    with open(DATA_ARTICLES_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    from data_articles import ARTICLES
    existing_slugs = {a["slug"] for a in ARTICLES}

    if FLAGSHIP_ARTICLE["slug"] in existing_slugs:
        print("Flagship article already exists in data_articles.py")
        return

    last_bracket_idx = content.rfind("]")
    if last_bracket_idx == -1:
        print("Error: Could not find closing bracket in data_articles.py")
        return

    additions_code = "    " + repr(FLAGSHIP_ARTICLE) + ",\n"

    clean_prefix = content[:last_bracket_idx].rstrip()
    if clean_prefix.endswith(","):
        new_content = clean_prefix + "\n" + additions_code + content[last_bracket_idx:]
    else:
        new_content = clean_prefix + ",\n" + additions_code + content[last_bracket_idx:]

    with open(DATA_ARTICLES_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Successfully added flagship VPS & Vibe Coding Security Guide to data_articles.py!")

if __name__ == "__main__":
    main()
