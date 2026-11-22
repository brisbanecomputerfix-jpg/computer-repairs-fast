"""
Bespoke, non-AI isometric and technical vector illustrations for Computer Repairs Fast.
Clean, lightweight, mathematical SVG graphics:
- Isometric projection (30-degree angles, crisp lines, clean gradients)
- Topic-specific hardware, components, networking, security, and cloud tech
- Zero external image assets, zero AI slop, razor-sharp on Retina 4K displays
"""

def get_svg_illustration(theme: str) -> str:
    """Return crisp isometric SVG vector markup for the given theme."""
    
    # Common dimensions: viewBox="0 0 360 140"
    if theme == "screen-repair":
        # Isometric Laptop with display assembly, precision layer separation & digitizer grid
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="scr-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#f0f9ff"/>
      <stop offset="100%" stop-color="#e0f2fe"/>
    </linearGradient>
    <linearGradient id="scr-panel" x1="120" y1="20" x2="240" y2="90" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="scr-glass" x1="140" y1="30" x2="220" y2="80" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0.9"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#scr-bg)"/>
  <!-- Isometric Grid Subtle Floor -->
  <path d="M60 110 L180 70 L300 110 L180 135 Z" fill="#bae6fd" fill-opacity="0.35"/>
  <path d="M100 110 L180 83 L260 110 L180 126 Z" stroke="#38bdf8" stroke-width="0.75" stroke-dasharray="3 3" opacity="0.6"/>
  <!-- Laptop Base Chassis -->
  <polygon points="120,95 180,75 240,95 180,115" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.5"/>
  <polygon points="120,95 120,101 180,121 180,115" fill="#94a3b8"/>
  <polygon points="180,115 180,121 240,101 240,95" fill="#64748b"/>
  <!-- Keyboard area -->
  <polygon points="135,93 180,78 225,93 180,108" fill="#1e293b"/>
  <polygon points="160,107 180,101 200,107 180,113" fill="#475569"/>
  <!-- Laptop Screen Lid (Angled Back) -->
  <polygon points="120,93 180,73 180,25 120,45" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
  <polygon points="180,73 240,93 240,45 180,25" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
  <!-- Active Screen Display Glow -->
  <polygon points="126,89 176,72 176,31 126,48" fill="url(#scr-glass)"/>
  <polygon points="176,72 234,91 234,49 176,31" fill="url(#scr-panel)"/>
  <!-- Digitizer Matrix Touch Lines -->
  <line x1="135" y1="46" x2="165" y2="82" stroke="#ffffff" stroke-width="0.75" opacity="0.5"/>
  <line x1="145" y1="42" x2="175" y2="78" stroke="#ffffff" stroke-width="0.75" opacity="0.5"/>
  <line x1="185" y1="36" x2="225" y2="86" stroke="#ffffff" stroke-width="0.75" opacity="0.5"/>
  <!-- Exploded Digitizer Glass Layer Floating in Front -->
  <polygon points="195,60 255,80 255,35 195,15" fill="#0284c7" fill-opacity="0.18" stroke="#0ea5e9" stroke-width="1.5" stroke-dasharray="4 2"/>
  <!-- Screwdriver Calibrator Probe -->
  <line x1="280" y1="30" x2="245" y2="55" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <line x1="245" y1="55" x2="238" y2="60" stroke="#94a3b8" stroke-width="1.5" stroke-linecap="round"/>
  <!-- Measurement Badge -->
  <g transform="translate(42, 28)">
    <rect width="68" height="22" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="1.2"/>
    <text x="34" y="15" fill="#0369a1" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">1080p FHD</text>
  </g>
</svg>"""

    elif theme == "macbook-apple":
        # Isometric Apple MacBook Unibody, Retina Display & Mini-LED Backlight
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="mac-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#f5f3ff"/>
      <stop offset="100%" stop-color="#ede9fe"/>
    </linearGradient>
    <linearGradient id="mac-screen" x1="130" y1="20" x2="230" y2="90" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#6366f1"/>
      <stop offset="50%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#4f46e5"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#mac-bg)"/>
  <!-- Floor Shadow -->
  <ellipse cx="180" cy="112" rx="85" ry="18" fill="#c4b5fd" fill-opacity="0.4"/>
  <!-- MacBook Unibody Base -->
  <polygon points="110,95 180,72 250,95 180,118" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>
  <polygon points="110,95 110,100 180,123 180,118" fill="#cbd5e1"/>
  <polygon points="180,118 180,123 250,100 250,95" fill="#94a3b8"/>
  <!-- Force Touch Trackpad -->
  <polygon points="165,108 180,103 195,108 180,113" fill="#cbd5e1" stroke="#94a3b8" stroke-width="0.75"/>
  <!-- Magic Keyboard Well -->
  <polygon points="125,93 180,75 235,93 180,107" fill="#0f172a"/>
  <!-- Display Lid Assembly -->
  <polygon points="120,90 180,70 180,20 120,40" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <polygon points="180,70 240,90 240,40 180,20" fill="#1e293b" stroke="#334155" stroke-width="1.2"/>
  <!-- Retina Liquid Display Surface -->
  <polygon points="125,86 177,69 177,25 125,43" fill="url(#mac-screen)"/>
  <polygon points="177,69 235,88 235,44 177,25" fill="url(#mac-screen)"/>
  <!-- Camera Notch -->
  <polygon points="174,24 183,24 183,28 174,28" fill="#0f172a"/>
  <circle cx="178.5" cy="26" r="1.2" fill="#22c55e"/>
  <!-- Apple Silicon M-Series Chip floating on side -->
  <g transform="translate(255, 35)">
    <polygon points="25,12 50,0 50,28 25,40" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.2"/>
    <polygon points="0,0 25,12 25,40 0,28" fill="#312e81" stroke="#6366f1" stroke-width="1.2"/>
    <polygon points="0,0 25,-12 50,0 25,12" fill="#4338ca" stroke="#6366f1" stroke-width="1.2"/>
    <text x="25" y="15" fill="#ffffff" font-size="9" font-weight="800" font-family="sans-serif" text-anchor="middle">M-CHIP</text>
  </g>
  <!-- Retina Tag -->
  <g transform="translate(38, 30)">
    <rect width="66" height="22" rx="4" fill="#ffffff" stroke="#8b5cf6" stroke-width="1.2"/>
    <text x="33" y="15" fill="#6d28d9" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">Retina OLED</text>
  </g>
</svg>"""

    elif theme == "battery-power":
        # Isometric Lithium Battery Pack with swell expansion & BMS IC protection
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="bat-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#fffbeb"/>
      <stop offset="100%" stop-color="#fef3c7"/>
    </linearGradient>
    <linearGradient id="cell-grad" x1="120" y1="50" x2="240" y2="110" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#bat-bg)"/>
  <!-- Isometric Ground Shadow -->
  <ellipse cx="180" cy="115" rx="80" ry="16" fill="#fde68a" fill-opacity="0.6"/>
  <!-- 3-Cell Battery Pack Assembly -->
  <!-- Cell 1 -->
  <polygon points="100,75 140,55 160,65 120,85" fill="#334155" stroke="#475569" stroke-width="1.2"/>
  <polygon points="100,75 100,88 120,98 120,85" fill="#1e293b"/>
  <polygon points="120,85 120,98 160,78 160,65" fill="#0f172a"/>
  <!-- Cell 2 (Slightly Swollen Pouch Effect) -->
  <polygon points="142,54 182,34 202,44 162,64" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
  <polygon points="142,54 142,70 162,80 162,64" fill="#b45309"/>
  <polygon points="162,64 162,80 202,60 202,44" fill="#78350f"/>
  <!-- Cell 3 -->
  <polygon points="184,33 224,13 244,23 204,43" fill="#334155" stroke="#475569" stroke-width="1.2"/>
  <polygon points="184,33 184,46 204,56 204,43" fill="#1e293b"/>
  <polygon points="204,43 204,56 244,36 244,23" fill="#0f172a"/>
  <!-- BMS Circuit Board (Green PCB ribbon) -->
  <polygon points="90,85 130,65 240,120 200,140" fill="none"/>
  <path d="M120 98 L230 45" stroke="#10b981" stroke-width="3" stroke-linecap="round"/>
  <!-- Power Spark & Caution Badge -->
  <g transform="translate(265, 45)">
    <polygon points="18,0 36,30 0,30" fill="#ef4444" stroke="#b91c1c" stroke-width="1.5"/>
    <text x="18" y="25" fill="#ffffff" font-size="16" font-weight="900" font-family="sans-serif" text-anchor="middle">!</text>
  </g>
  <!-- Voltage / Health Spec Tag -->
  <g transform="translate(38, 30)">
    <rect width="78" height="24" rx="4" fill="#ffffff" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="39" y="16" fill="#b45309" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">Li-Ion OEM</text>
  </g>
  <!-- Power flow indicator -->
  <circle cx="172" cy="54" r="5" fill="#fbbf24"/>
  <path d="M172 51 L170 54 L174 54 L172 57" stroke="#b45309" stroke-width="1.2" stroke-linecap="round"/>
</svg>"""

    elif theme == "liquid-spill":
        # Motherboard PCB with ultrasonic cleaning waves, corrosion shield
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="spill-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#fef2f2"/>
      <stop offset="100%" stop-color="#fee2e2"/>
    </linearGradient>
    <linearGradient id="pcb-grad" x1="120" y1="40" x2="240" y2="110" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#15803d"/>
      <stop offset="100%" stop-color="#166534"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#spill-bg)"/>
  <!-- Motherboard Isometric PCB -->
  <polygon points="100,85 180,45 260,85 180,125" fill="url(#pcb-grad)" stroke="#14532d" stroke-width="1.5"/>
  <polygon points="100,85 100,92 180,132 180,125" fill="#14532d"/>
  <polygon points="180,125 180,132 260,92 260,85" fill="#052e16"/>
  <!-- Gold Traces & Solder Points -->
  <path d="M120 85 L150 70 L180 85" stroke="#facc15" stroke-width="1.2"/>
  <path d="M150 85 L180 70 L210 85" stroke="#facc15" stroke-width="1.2"/>
  <circle cx="140" cy="75" r="2" fill="#fef08a"/>
  <circle cx="170" cy="90" r="2" fill="#fef08a"/>
  <circle cx="200" cy="75" r="2" fill="#fef08a"/>
  <!-- CPU / Chipset Socket -->
  <polygon points="160,75 180,65 200,75 180,85" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <!-- Droplet / Spill Splash (Amber coffee/tea drop intercepted) -->
  <path d="M180 25 C175 40 165 48 165 56 A15 15 0 0 0 195 56 C195 48 185 40 180 25 Z" fill="#ef4444" fill-opacity="0.85" stroke="#dc2626" stroke-width="1.2"/>
  <!-- Ultrasonic Neutralizing Waves -->
  <ellipse cx="180" cy="85" rx="50" ry="16" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 3"/>
  <ellipse cx="180" cy="85" rx="70" ry="22" fill="none" stroke="#0ea5e9" stroke-width="1" stroke-dasharray="6 4" opacity="0.7"/>
  <!-- First Aid Cross Badge -->
  <g transform="translate(38, 28)">
    <rect width="82" height="24" rx="4" fill="#ffffff" stroke="#dc2626" stroke-width="1.2"/>
    <text x="41" y="16" fill="#b91c1c" font-size="10" font-weight="800" font-family="sans-serif" text-anchor="middle">🚑 Ultrasonic</text>
  </g>
</svg>"""

    elif theme == "ssd-speed":
        # Isometric M.2 NVMe SSD with PCIe 4.0 interface & gold contacts
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="ssd-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ecfeff"/>
      <stop offset="100%" stop-color="#cffafe"/>
    </linearGradient>
    <linearGradient id="pcie-grad" x1="100" y1="60" x2="260" y2="100" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0e7490"/>
      <stop offset="100%" stop-color="#155e75"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#ssd-bg)"/>
  <!-- Floor Speed Glow -->
  <ellipse cx="180" cy="110" rx="90" ry="18" fill="#a5f3fc" fill-opacity="0.5"/>
  <!-- M.2 SSD PCB Stick (Angled Isometric) -->
  <polygon points="100,85 220,25 260,45 140,105" fill="url(#pcie-grad)" stroke="#083344" stroke-width="1.5"/>
  <polygon points="100,85 100,90 140,110 140,105" fill="#083344"/>
  <polygon points="140,105 140,110 260,50 260,45" fill="#042f2e"/>
  <!-- PCIe Gold Contact Notch Fingers -->
  <polygon points="98,84 108,79 116,83 106,88" fill="#eab308" stroke="#ca8a04" stroke-width="0.75"/>
  <!-- NAND Flash Chip 1 -->
  <polygon points="135,75 165,60 180,68 150,83" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <!-- NAND Flash Chip 2 -->
  <polygon points="175,55 205,40 220,48 190,63" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <!-- Fast Controller IC -->
  <polygon points="120,68 135,60 145,65 130,73" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
  <!-- High Speed PCIe 7,000 MB/s Vector Arrows -->
  <g transform="translate(245, 60)">
    <path d="M0 20 L25 10 L0 0 Z" fill="#06b6d4"/>
    <path d="M15 20 L40 10 L15 0 Z" fill="#0891b2"/>
  </g>
  <!-- Speed Badge -->
  <g transform="translate(38, 28)">
    <rect width="84" height="24" rx="4" fill="#ffffff" stroke="#0891b2" stroke-width="1.2"/>
    <text x="42" y="16" fill="#0e7490" font-size="10" font-weight="800" font-family="sans-serif" text-anchor="middle">⚡ 7,000 MB/s</text>
  </g>
</svg>"""

    elif theme == "hinge-casing":
        # Mechanical Laptop Hinge, Brass Threaded Inserts & Casing Anchor
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="hng-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#f1f5f9"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#hng-bg)"/>
  <!-- Isometric Ground -->
  <polygon points="80,105 180,65 280,105 180,135" fill="#e2e8f0" fill-opacity="0.6"/>
  <!-- Casing Corner Frame -->
  <polygon points="110,85 180,50 210,65 140,100" fill="#475569" stroke="#334155" stroke-width="1.5"/>
  <!-- Steel Hinge Bracket Arm -->
  <polygon points="130,75 190,45 198,49 138,79" fill="#94a3b8" stroke="#64748b" stroke-width="1.2"/>
  <!-- Hinge Rotating Barrel (Cylinder) -->
  <ellipse cx="190" cy="45" rx="8" ry="12" fill="#cbd5e1" stroke="#475569" stroke-width="1.2"/>
  <path d="M190 33 L205 40 L205 52 L190 45 Z" fill="#94a3b8"/>
  <ellipse cx="205" cy="46" rx="8" ry="12" fill="#e2e8f0" stroke="#475569" stroke-width="1.2"/>
  <!-- Knurled Brass Threaded Bushing Socket -->
  <g transform="translate(145, 78)">
    <polygon points="0,8 16,0 32,8 16,16" fill="#eab308" stroke="#ca8a04" stroke-width="1"/>
    <polygon points="0,8 0,16 16,24 16,16" fill="#ca8a04"/>
    <polygon points="16,16 16,24 32,16 32,8" fill="#a16207"/>
    <!-- Thread Hole -->
    <ellipse cx="16" cy="8" rx="6" ry="3" fill="#713f12"/>
  </g>
  <!-- Reinforcement Structural Anchor Badge -->
  <g transform="translate(38, 28)">
    <rect width="86" height="24" rx="4" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>
    <text x="43" y="16" fill="#334155" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">🔧 Steel Hinge</text>
  </g>
</svg>"""

    elif theme == "cybersecurity-scams":
        # 3D Cyber Defense Shield, Padlock Vault & Threat Interception
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="scam-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ecfdf5"/>
      <stop offset="100%" stop-color="#d1fae5"/>
    </linearGradient>
    <linearGradient id="shield-grad" x1="150" y1="20" x2="210" y2="100" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#scam-bg)"/>
  <!-- Security Radar Ring -->
  <ellipse cx="180" cy="115" rx="85" ry="18" fill="#a7f3d0" fill-opacity="0.5"/>
  <ellipse cx="180" cy="115" rx="60" ry="12" fill="none" stroke="#10b981" stroke-width="1" stroke-dasharray="3 3"/>
  <!-- 3D Security Shield -->
  <g transform="translate(150, 20)">
    <path d="M30 0 L60 12 C60 48 30 75 30 75 C30 75 0 48 0 12 Z" fill="url(#shield-grad)" stroke="#065f46" stroke-width="1.8"/>
    <!-- Padlock inside Shield -->
    <!-- Shackle -->
    <path d="M22 32 V24 A8 8 0 0 1 38 24 V32" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <!-- Body -->
    <rect x="18" y="32" width="24" height="20" rx="3" fill="#facc15" stroke="#ca8a04" stroke-width="1.2"/>
    <circle cx="30" cy="40" r="2.5" fill="#713f12"/>
    <path d="M30 42.5 V46" stroke="#713f12" stroke-width="1.8"/>
  </g>
  <!-- Verified Protection Badge -->
  <g transform="translate(38, 28)">
    <rect width="88" height="24" rx="4" fill="#ffffff" stroke="#10b981" stroke-width="1.2"/>
    <text x="44" y="16" fill="#047857" font-size="10" font-weight="800" font-family="sans-serif" text-anchor="middle">🛡️ Anti-Fraud</text>
  </g>
  <!-- Intercepted Remote Scam Threat Tag -->
  <g transform="translate(250, 42)">
    <rect width="70" height="22" rx="4" fill="#fee2e2" stroke="#ef4444" stroke-width="1"/>
    <text x="35" y="15" fill="#b91c1c" font-size="9" font-weight="700" font-family="sans-serif" text-anchor="middle">Blocked ✕</text>
  </g>
</svg>"""

    elif theme == "vpn-privacy":
        # Encrypted Network Tunnel, Zero-Telemetry, Private Gateway
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="vpn-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#eef2ff"/>
      <stop offset="100%" stop-color="#e0e7ff"/>
    </linearGradient>
    <linearGradient id="tunnel-grad" x1="120" y1="30" x2="240" y2="100" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#vpn-bg)"/>
  <!-- Encrypted Tunnel Rings -->
  <ellipse cx="140" cy="70" rx="25" ry="40" fill="none" stroke="#6366f1" stroke-width="2" opacity="0.4"/>
  <ellipse cx="180" cy="70" rx="30" ry="45" fill="none" stroke="#4f46e5" stroke-width="2.5"/>
  <ellipse cx="220" cy="70" rx="25" ry="40" fill="none" stroke="#4338ca" stroke-width="2" opacity="0.4"/>
  <!-- Tunnel Beam -->
  <path d="M120 70 L240 70" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" stroke-dasharray="6 4"/>
  <!-- Privacy Keylock Node -->
  <circle cx="180" cy="70" r="16" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
  <path d="M174 70 A6 6 0 0 1 186 70" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <rect x="173" y="70" width="14" height="10" rx="2" fill="#38bdf8"/>
  <!-- No Tracking Tag -->
  <g transform="translate(38, 28)">
    <rect width="84" height="24" rx="4" fill="#ffffff" stroke="#4f46e5" stroke-width="1.2"/>
    <text x="42" y="16" fill="#3730a3" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">🔒 Zero-Track</text>
  </g>
</svg>"""

    elif theme == "wfh-office-network":
        # Dual Desktop Monitors, Thunderbolt Dock & Wi-Fi 6 Router
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="wfh-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#f0f9ff"/>
      <stop offset="100%" stop-color="#e0f2fe"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#wfh-bg)"/>
  <!-- Desk Surface -->
  <polygon points="70,110 180,65 290,110 180,135" fill="#e2e8f0" fill-opacity="0.8"/>
  <!-- Monitor 1 (Left Angled) -->
  <polygon points="105,85 155,65 155,25 105,45" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <polygon points="109,82 151,65 151,30 109,47" fill="#0284c7"/>
  <polygon points="128,85 132,83 132,95 128,95" fill="#64748b"/>
  <!-- Monitor 2 (Right Angled) -->
  <polygon points="160,63 210,83 210,43 160,23" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <polygon points="164,63 206,80 206,47 164,30" fill="#38bdf8"/>
  <polygon points="183,83 187,85 187,95 183,95" fill="#64748b"/>
  <!-- Docking Station Hub -->
  <polygon points="165,100 185,92 200,98 180,106" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <!-- Wi-Fi 6 Waves from Router -->
  <g transform="translate(245, 65)">
    <!-- Router Box -->
    <polygon points="10,25 30,17 45,23 25,31" fill="#0f172a"/>
    <line x1="20" y1="20" x2="20" y2="5" stroke="#0f172a" stroke-width="2"/>
    <path d="M12 5 A10 10 0 0 1 28 5" fill="none" stroke="#0ea5e9" stroke-width="1.5"/>
    <path d="M8 0 A15 15 0 0 1 32 0" fill="none" stroke="#0284c7" stroke-width="1.5"/>
  </g>
  <!-- WFH Setup Tag -->
  <g transform="translate(38, 28)">
    <rect width="84" height="24" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="1.2"/>
    <text x="42" y="16" fill="#0369a1" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">🏢 WFH Setup</text>
  </g>
</svg>"""

    elif theme == "printer-wifi":
        # Desktop Wireless Printer with Wi-Fi Signals & Static IP beacon
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="prn-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#eff6ff"/>
      <stop offset="100%" stop-color="#dbeafe"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#prn-bg)"/>
  <ellipse cx="180" cy="115" rx="75" ry="16" fill="#bfdbfe" fill-opacity="0.5"/>
  <!-- Printer Main Body -->
  <polygon points="120,80 180,55 240,80 180,105" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
  <polygon points="120,80 120,100 180,125 180,105" fill="#e2e8f0"/>
  <polygon points="180,105 180,125 240,100 240,80" fill="#cbd5e1"/>
  <!-- Paper Output Slot -->
  <polygon points="140,95 180,80 220,95 180,110" fill="#0f172a"/>
  <!-- Printed Document Coming Out -->
  <polygon points="150,92 180,80 210,92 180,104" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
  <line x1="165" y1="94" x2="195" y2="94" stroke="#94a3b8" stroke-width="1"/>
  <!-- Wi-Fi Online Beacon Waves -->
  <g transform="translate(180, 32)">
    <circle cx="0" cy="15" r="3" fill="#22c55e"/>
    <path d="M-8 10 A12 12 0 0 1 8 10" fill="none" stroke="#2563eb" stroke-width="2"/>
    <path d="M-14 4 A20 20 0 0 1 14 4" fill="none" stroke="#3b82f6" stroke-width="2"/>
  </g>
  <!-- Wi-Fi Guide Tag -->
  <g transform="translate(38, 28)">
    <rect width="84" height="24" rx="4" fill="#ffffff" stroke="#2563eb" stroke-width="1.2"/>
    <text x="42" y="16" fill="#1d4ed8" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">🖨️ Wi-Fi Setup</text>
  </g>
</svg>"""

    elif theme == "email-migration":
        # Cloud Mailbox Hub, Microsoft 365 Cloud Bridge & Synchronized Envelopes
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="eml-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#f0f9ff"/>
      <stop offset="100%" stop-color="#e0f2fe"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#eml-bg)"/>
  <!-- Cloud Foundation -->
  <ellipse cx="180" cy="115" rx="85" ry="16" fill="#bae6fd" fill-opacity="0.4"/>
  <!-- Source Mailbox (BigPond / Optus) -->
  <g transform="translate(90, 50)">
    <rect width="50" height="36" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
    <path d="M0 0 L25 18 L50 0" stroke="#0284c7" stroke-width="1.5" fill="none"/>
    <text x="25" y="30" fill="#0369a1" font-size="9" font-weight="800" font-family="sans-serif" text-anchor="middle">POP3</text>
  </g>
  <!-- Cloud Migration Tunnel -->
  <path d="M145 68 C165 50 195 50 215 68" stroke="#0284c7" stroke-width="3" stroke-dasharray="4 3"/>
  <polygon points="218,68 210,63 213,72" fill="#0284c7"/>
  <!-- Destination Mailbox (Microsoft 365 Cloud) -->
  <g transform="translate(220, 50)">
    <rect width="50" height="36" rx="4" fill="#0284c7" stroke="#0369a1" stroke-width="1.5"/>
    <path d="M0 0 L25 18 L50 0" stroke="#ffffff" stroke-width="1.5" fill="none"/>
    <text x="25" y="30" fill="#ffffff" font-size="9" font-weight="800" font-family="sans-serif" text-anchor="middle">M365</text>
  </g>
  <!-- Success Verification Checkmark Badge -->
  <circle cx="180" cy="50" r="10" fill="#22c55e"/>
  <path d="M175 50 L178 53 L185 46" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <!-- Tag -->
  <g transform="translate(38, 28)">
    <rect width="84" height="24" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="1.2"/>
    <text x="42" y="16" fill="#0369a1" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">✉️ 365 Cloud</text>
  </g>
</svg>"""

    elif theme == "backup-ransomware":
        # Enterprise RAID Storage NAS, Cloud Mirroring & Immutable Shield
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="nas-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#faf5ff"/>
      <stop offset="100%" stop-color="#f3e8ff"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#nas-bg)"/>
  <ellipse cx="180" cy="115" rx="80" ry="16" fill="#e9d5ff" fill-opacity="0.6"/>
  <!-- NAS Storage Enclosure -->
  <polygon points="130,70 190,45 230,62 170,87" fill="#1e1b4b" stroke="#312e81" stroke-width="1.5"/>
  <polygon points="130,70 130,105 170,122 170,87" fill="#312e81"/>
  <polygon points="170,87 170,122 230,97 230,62" fill="#4338ca"/>
  <!-- Drive Trays -->
  <line x1="135" y1="80" x2="165" y2="92" stroke="#9333ea" stroke-width="2"/>
  <line x1="135" y1="92" x2="165" y2="104" stroke="#9333ea" stroke-width="2"/>
  <line x1="135" y1="104" x2="165" y2="116" stroke="#9333ea" stroke-width="2"/>
  <circle cx="160" cy="80" r="1.5" fill="#22c55e"/>
  <circle cx="160" cy="92" r="1.5" fill="#22c55e"/>
  <circle cx="160" cy="104" r="1.5" fill="#22c55e"/>
  <!-- 3-2-1 Backup Shield -->
  <g transform="translate(240, 35)">
    <path d="M20 0 L40 8 C40 28 20 42 20 42 C20 42 0 28 0 8 Z" fill="#9333ea"/>
    <text x="20" y="24" fill="#ffffff" font-size="11" font-weight="900" font-family="sans-serif" text-anchor="middle">3-2-1</text>
  </g>
  <!-- Tag -->
  <g transform="translate(38, 28)">
    <rect width="84" height="24" rx="4" fill="#ffffff" stroke="#9333ea" stroke-width="1.2"/>
    <text x="42" y="16" fill="#7e22ce" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">💾 RAID NAS</text>
  </g>
</svg>"""

    elif theme == "accounting-software":
        # Business Accounting Ledger, Database Tables & Compatibility Container
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="act-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#f0fdf4"/>
      <stop offset="100%" stop-color="#dcfce7"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#act-bg)"/>
  <ellipse cx="180" cy="115" rx="80" ry="16" fill="#bbf7d0" fill-opacity="0.6"/>
  <!-- Database Storage Cube -->
  <polygon points="140,65 180,45 220,65 180,85" fill="#059669" stroke="#047857" stroke-width="1.5"/>
  <polygon points="140,65 140,95 180,115 180,85" fill="#047857"/>
  <polygon points="180,85 180,115 220,95 220,65" fill="#065f46"/>
  <!-- Ledger Rows -->
  <line x1="148" y1="78" x2="175" y2="92" stroke="#a7f3d0" stroke-width="1.5"/>
  <line x1="148" y1="88" x2="175" y2="102" stroke="#a7f3d0" stroke-width="1.5"/>
  <!-- Windows 11 Shield Badge -->
  <g transform="translate(235, 40)">
    <rect width="40" height="40" rx="6" fill="#ffffff" stroke="#059669" stroke-width="1.5"/>
    <text x="20" y="24" fill="#059669" font-size="10" font-weight="800" font-family="sans-serif" text-anchor="middle">MYOB</text>
  </g>
  <!-- Tag -->
  <g transform="translate(38, 28)">
    <rect width="84" height="24" rx="4" fill="#ffffff" stroke="#059669" stroke-width="1.2"/>
    <text x="42" y="16" fill="#047857" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">📊 v19 Migration</text>
  </g>
</svg>"""

    elif theme == "senior-lessons-community":
        # High-Contrast Senior Screen, Verified Padlock & Friendly Guide
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="snr-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#fff1f2"/>
      <stop offset="100%" stop-color="#ffe4e6"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#snr-bg)"/>
  <ellipse cx="180" cy="115" rx="80" ry="16" fill="#fecdd3" fill-opacity="0.6"/>
  <!-- Clean Big-Text Friendly Tablet / Laptop -->
  <polygon points="120,85 180,60 240,85 180,110" fill="#ffffff" stroke="#e11d48" stroke-width="1.5"/>
  <polygon points="120,85 180,60 180,30 120,55" fill="#be123c"/>
  <polygon points="180,60 240,85 240,55 180,30" fill="#e11d48"/>
  <!-- High Contrast Icons on Screen -->
  <rect x="135" y="45" width="22" height="14" rx="2" fill="#ffffff"/>
  <text x="146" y="55" fill="#be123c" font-size="8" font-weight="900" font-family="sans-serif" text-anchor="middle">PASS</text>
  <!-- Magnifying Glass Compass Guide -->
  <g transform="translate(230, 45)">
    <circle cx="18" cy="18" r="14" fill="none" stroke="#e11d48" stroke-width="3"/>
    <line x1="28" y1="28" x2="40" y2="40" stroke="#be123c" stroke-width="4" stroke-linecap="round"/>
  </g>
  <!-- Tag -->
  <g transform="translate(38, 28)">
    <rect width="84" height="24" rx="4" fill="#ffffff" stroke="#e11d48" stroke-width="1.2"/>
    <text x="42" y="16" fill="#be123c" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">🎓 Brisbane Tech</text>
  </g>
</svg>"""

    elif theme == "cooling-dust-maintenance":
        # Dual Aerodynamic Cooling Turbine, Copper Heatpipes & Thermal Paste Syringe
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="cool-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#f0fdfa"/>
      <stop offset="100%" stop-color="#ccfbf1"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#cool-bg)"/>
  <ellipse cx="180" cy="115" rx="80" ry="16" fill="#99f6e4" fill-opacity="0.5"/>
  <!-- Copper Heatpipes Assembly -->
  <path d="M110 80 Q180 50 250 80" stroke="#ea580c" stroke-width="6" stroke-linecap="round" fill="none"/>
  <!-- Cooling Fan 1 -->
  <circle cx="140" cy="75" r="22" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
  <circle cx="140" cy="75" r="6" fill="#38bdf8"/>
  <!-- Fan Blades -->
  <path d="M140 57 L140 69 M140 81 L140 93 M122 75 L134 75 M146 75 L158 75" stroke="#ffffff" stroke-width="2"/>
  <!-- Cooling Fan 2 -->
  <circle cx="220" cy="75" r="22" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
  <circle cx="220" cy="75" r="6" fill="#38bdf8"/>
  <path d="M220 57 L220 69 M220 81 L220 93 M202 75 L214 75 M226 75 L238 75" stroke="#ffffff" stroke-width="2"/>
  <!-- High Conductivity Thermal Syringe -->
  <g transform="translate(170, 20)">
    <rect width="18" height="40" rx="2" fill="#cbd5e1" stroke="#475569" stroke-width="1"/>
    <line x1="9" y1="40" x2="9" y2="48" stroke="#94a3b8" stroke-width="2"/>
    <circle cx="9" cy="50" r="2" fill="#64748b"/>
  </g>
  <!-- Tag -->
  <g transform="translate(38, 28)">
    <rect width="84" height="24" rx="4" fill="#ffffff" stroke="#0d9488" stroke-width="1.2"/>
    <text x="42" y="16" fill="#0f766e" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">❄️ Repasting</text>
  </g>
</svg>"""

    elif theme == "photo-organization":
        # Folder Hierarchy Tree, Photo Indexes & Deduplication Scanner
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="pho-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#fffbeb"/>
      <stop offset="100%" stop-color="#fef3c7"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#pho-bg)"/>
  <ellipse cx="180" cy="115" rx="75" ry="16" fill="#fde68a" fill-opacity="0.6"/>
  <!-- Main Folder -->
  <g transform="translate(130, 45)">
    <path d="M0 6 L12 6 L18 12 L50 12 L50 44 L0 44 Z" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
    <rect x="6" y="16" width="38" height="24" rx="2" fill="#ffffff"/>
    <circle cx="16" cy="24" r="3" fill="#ea580c"/>
    <polygon points="12,34 22,26 30,34" fill="#f59e0b"/>
  </g>
  <!-- Duplicate Finder Scanner Beam -->
  <line x1="120" y1="35" x2="230" y2="90" stroke="#ef4444" stroke-width="2" stroke-dasharray="4 2"/>
  <!-- Dedup Tag -->
  <g transform="translate(38, 28)">
    <rect width="84" height="24" rx="4" fill="#ffffff" stroke="#d97706" stroke-width="1.2"/>
    <text x="42" y="16" fill="#b45309" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">📁 Deduplicate</text>
  </g>
</svg>"""

    elif theme == "vps-coolify-devops":
        # Cloud Server Rack, Docker Containers & AI LM Studio Terminal
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="vps-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#vps-bg)"/>
  <ellipse cx="180" cy="120" rx="80" ry="14" fill="#38bdf8" fill-opacity="0.15"/>
  <!-- Server Rack Enclosure -->
  <polygon points="140,50 190,30 220,45 170,65" fill="#1e293b" stroke="#334155" stroke-width="1.2"/>
  <polygon points="140,50 140,110 170,125 170,65" fill="#334155"/>
  <polygon points="170,65 170,125 220,105 220,45" fill="#475569"/>
  <!-- 1U Server Units with Blinking LEDs -->
  <line x1="145" y1="65" x2="165" y2="75" stroke="#38bdf8" stroke-width="2"/>
  <line x1="145" y1="80" x2="165" y2="90" stroke="#10b981" stroke-width="2"/>
  <line x1="145" y1="95" x2="165" y2="105" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="160" cy="65" r="1.5" fill="#38bdf8"/>
  <circle cx="160" cy="80" r="1.5" fill="#10b981"/>
  <circle cx="160" cy="95" r="1.5" fill="#22c55e"/>
  <!-- Floating Coolify / Docker Container Cube -->
  <g transform="translate(230, 45)">
    <polygon points="20,10 40,0 40,22 20,32" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
    <polygon points="0,0 20,10 20,32 0,22" fill="#0369a1" stroke="#38bdf8" stroke-width="1"/>
    <polygon points="0,0 20,-10 40,0 20,10" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>
    <text x="20" y="12" fill="#ffffff" font-size="8" font-weight="900" font-family="sans-serif" text-anchor="middle">APP</text>
  </g>
  <!-- Tag -->
  <g transform="translate(38, 28)">
    <rect width="84" height="24" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="42" y="16" fill="#38bdf8" font-size="10" font-weight="800" font-family="sans-serif" text-anchor="middle">⚡ Coolify VPS</text>
  </g>
</svg>"""

    else:
        # Default: buying-quote-guide (Multimeter probe, itemized pricing balance, warranty stamp)
        return """<svg viewBox="0 0 360 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="iso-svg">
  <defs>
    <linearGradient id="qte-bg" x1="0" y1="0" x2="360" y2="140" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#f1f5f9"/>
    </linearGradient>
  </defs>
  <rect width="360" height="140" fill="url(#qte-bg)"/>
  <ellipse cx="180" cy="115" rx="80" ry="16" fill="#e2e8f0" fill-opacity="0.6"/>
  <!-- Itemized Transparent Quote Clipboard -->
  <polygon points="130,70 190,45 230,62 170,87" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <polygon points="130,70 130,105 170,122 170,87" fill="#f8fafc"/>
  <polygon points="170,87 170,122 230,97 230,62" fill="#f1f5f9"/>
  <!-- Itemized Rows -->
  <line x1="138" y1="80" x2="165" y2="92" stroke="#2563eb" stroke-width="2"/>
  <line x1="138" y1="92" x2="165" y2="104" stroke="#64748b" stroke-width="2"/>
  <line x1="138" y1="104" x2="165" y2="116" stroke="#22c55e" stroke-width="2"/>
  <!-- Multimeter Precision Probe -->
  <line x1="220" y1="35" x2="190" y2="65" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <line x1="190" y1="65" x2="183" y2="72" stroke="#94a3b8" stroke-width="1.5" stroke-linecap="round"/>
  <!-- Guaranteed Quote Tag -->
  <g transform="translate(38, 28)">
    <rect width="86" height="24" rx="4" fill="#ffffff" stroke="#2563eb" stroke-width="1.2"/>
    <text x="43" y="16" fill="#1d4ed8" font-size="10" font-weight="700" font-family="sans-serif" text-anchor="middle">📋 Fixed Quote</text>
  </g>
</svg>"""


def assign_illustration_theme(art: dict) -> str:
    """Map an article dictionary to its matching illustration theme."""
    slug = art.get("slug", "").lower()
    cat = art.get("category", "").lower()
    title = art.get("h1", "").lower()
    text = f"{slug} {cat} {title}"

    if "senior" in text or "courses" in text or "community" in text or "lessons" in text:
        return "senior-lessons-community"
    elif "macbook" in text or "apple" in text or "retina" in text or "flexgate" in text or "olm" in text:
        return "macbook-apple"
    elif "touchscreen" in text or "screen-replacement" in text or "cracked-touch" in text or "screen-repair" in text or "school-laptop" in text or "screen" in text:
        return "screen-repair"
    elif "battery" in text or "swelling" in text:
        return "battery-power"
    elif "liquid" in text or "spill" in text or "coffee" in text or "motherboard" in text:
        return "liquid-spill"
    elif "ssd" in text or "speed-comparison" in text or "dual-boot" in text:
        return "ssd-speed"
    elif "hinge" in text or "casing" in text:
        return "hinge-casing"
    elif "vpn" in text or "torrent" in text or "browser" in text or "smart-tv" in text:
        return "vpn-privacy"
    elif "scam" in text or "bank" in text or "antivirus" in text or "norton" in text or "mcafee" in text or "cyber" in text:
        return "cybersecurity-scams"
    elif "printer" in text:
        return "printer-wifi"
    elif "bigpond" in text or "optus" in text or "email" in text or "gmail" in text or "aliases" in text or "thunderbird" in text:
        return "email-migration"
    elif "backup" in text or "ransomware" in text or "deleted-files" in text or "pc-to-new-pc" in text or "transfer-everything" in text:
        return "backup-ransomware"
    elif "myob" in text or "reckon" in text:
        return "accounting-software"
    elif "gaming" in text or "cooling" in text or "dust" in text or "overheating" in text:
        return "cooling-dust-maintenance"
    elif "photo" in text or "duplicate" in text:
        return "photo-organization"
    elif "vps" in text or "coolify" in text or "lm-studio" in text or "vibe-coding" in text:
        return "vps-coolify-devops"
    elif "dual-monitor" in text or "docking" in text or "wfh" in text or "remote-work" in text or "wifi" in text or "it-support" in text or "small-business" in text:
        return "wfh-office-network"
    elif "quote" in text or "choose-a-laptop" in text or "expensive-thing" in text:
        return "buying-quote-guide"
    else:
        return "buying-quote-guide"
