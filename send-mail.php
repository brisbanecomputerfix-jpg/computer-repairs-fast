<?php
// ==============================================================================
// Fast Computer Repairs - Emergency Dispatch Mail Handler
// Anti-Spam Protected • Dual-Routing to info@computerrepairsfast.com.au & aykut@kalmaz.com
// Supports: General Booking, Suburb Locations, Liquid Damage & Scam/Virus Removal
// ==============================================================================

header('X-Content-Type-Options: nosniff');

$to = 'info@computerrepairsfast.com.au, aykut@kalmaz.com';
$is_ajax = !empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) === 'xmlhttprequest';

// Only accept POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    if ($is_ajax) {
        header('Content-Type: application/json; charset=utf-8');
        http_response_code(405);
        echo json_encode(['success' => false, 'error' => 'Method not allowed']);
        exit;
    }
    header('Location: /');
    exit;
}

// ------------------------------------------------------------------------------
// ANTI-SPAM SHIELD 1: Double Honeypot Check (Invisible inputs for bots)
// ------------------------------------------------------------------------------
if (!empty($_POST['website_hp']) || !empty($_POST['company_hp'])) {
    if ($is_ajax) {
        header('Content-Type: application/json; charset=utf-8');
        echo json_encode(['success' => true, 'message' => 'Your request has been received.']);
        exit;
    }
    header('Location: /');
    exit;
}

// ------------------------------------------------------------------------------
// ANTI-SPAM SHIELD 2: Time-to-Submit Check (Humans take at least 2.0 seconds)
// ------------------------------------------------------------------------------
$form_timestamp = filter_input(INPUT_POST, 'form_timestamp', FILTER_VALIDATE_FLOAT) ?: 0;
if ($form_timestamp > 0) {
    $now = microtime(true);
    $time_elapsed = $now - $form_timestamp;
    if ($time_elapsed < 2.0) {
        if ($is_ajax) {
            header('Content-Type: application/json; charset=utf-8');
            echo json_encode(['success' => true, 'message' => 'Your request has been received.']);
            exit;
        }
        header('Location: /');
        exit;
    }
}

// ------------------------------------------------------------------------------
// ANTI-SPAM SHIELD 3: IP Rate Limiting (Max 5 requests per 10 minutes per IP)
// ------------------------------------------------------------------------------
$client_ip = $_SERVER['HTTP_CF_CONNECTING_IP'] ?? $_SERVER['HTTP_X_FORWARDED_FOR'] ?? $_SERVER['REMOTE_ADDR'] ?? '127.0.0.1';
$rate_file = sys_get_temp_dir() . '/crf_rate_' . md5($client_ip) . '.json';
$current_time = time();

if (file_exists($rate_file)) {
    $rate_data = json_decode(@file_get_contents($rate_file), true);
    if ($rate_data && is_array($rate_data)) {
        if ($current_time - $rate_data['start_time'] > 600) {
            $rate_data = ['count' => 1, 'start_time' => $current_time];
        } else {
            $rate_data['count']++;
            if ($rate_data['count'] > 5) {
                if ($is_ajax) {
                    header('Content-Type: application/json; charset=utf-8');
                    http_response_code(429);
                    echo json_encode(['success' => false, 'error' => 'Too many requests. Please call or text us directly on 0401 148 654.']);
                    exit;
                }
                die('Too many requests. Please call 0401 148 654.');
            }
        }
    } else {
        $rate_data = ['count' => 1, 'start_time' => $current_time];
    }
} else {
    $rate_data = ['count' => 1, 'start_time' => $current_time];
}
@file_put_contents($rate_file, json_encode($rate_data), LOCK_EX);

// ------------------------------------------------------------------------------
// Sanitize & Validate Inputs (Handling all 9 forms)
// ------------------------------------------------------------------------------
$name          = trim(filter_input(INPUT_POST, 'name', FILTER_SANITIZE_SPECIAL_CHARS) ?: '');
$phone         = trim(filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_SPECIAL_CHARS) ?: '');
$email         = trim(filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL) ?: '');
$suburb        = trim(filter_input(INPUT_POST, 'suburb', FILTER_SANITIZE_SPECIAL_CHARS) ?: (filter_input(INPUT_POST, 'service_type', FILTER_SANITIZE_SPECIAL_CHARS) ?: 'Brisbane Metro'));
$problem       = trim(filter_input(INPUT_POST, 'problem', FILTER_SANITIZE_SPECIAL_CHARS) ?: '');
$liquid_type   = trim(filter_input(INPUT_POST, 'liquid_type', FILTER_SANITIZE_SPECIAL_CHARS) ?: '');
$laptop_model  = trim(filter_input(INPUT_POST, 'laptop_model', FILTER_SANITIZE_SPECIAL_CHARS) ?: '');
$incident_type = trim(filter_input(INPUT_POST, 'incident_type', FILTER_SANITIZE_SPECIAL_CHARS) ?: '');
$notes         = trim(filter_input(INPUT_POST, 'notes', FILTER_SANITIZE_SPECIAL_CHARS) ?: (filter_input(INPUT_POST, 'message', FILTER_SANITIZE_SPECIAL_CHARS) ?: ''));
$source_page   = trim(filter_input(INPUT_POST, 'source_page', FILTER_SANITIZE_SPECIAL_CHARS) ?: ($_SERVER['HTTP_REFERER'] ?? 'Website Form'));

// ------------------------------------------------------------------------------
// ANTI-SPAM SHIELD 4: Content & URL Spam Filter
// ------------------------------------------------------------------------------
$combined_text = strtolower($name . ' ' . $suburb . ' ' . $problem . ' ' . $notes . ' ' . $laptop_model);
$spam_triggers = ['http://', 'https://', 'www.', '[url]', '<a href', 'casino', 'viagra', 'cialis', 'crypto', 'bitcoin', 'telegram', 'whatsapp +', 'seo backlinks', 'dating', 'investment'];
foreach ($spam_triggers as $trigger) {
    if (strpos($combined_text, $trigger) !== false) {
        if ($is_ajax) {
            header('Content-Type: application/json; charset=utf-8');
            echo json_encode(['success' => true, 'message' => 'Your request has been received.']);
            exit;
        }
        header('Location: /');
        exit;
    }
}

// Cyrillic / non-standard script spam check
if (preg_match('/[\x{0400}-\x{04FF}]/u', $name . $suburb)) {
    if ($is_ajax) {
        header('Content-Type: application/json; charset=utf-8');
        echo json_encode(['success' => true]);
        exit;
    }
    header('Location: /');
    exit;
}

// ------------------------------------------------------------------------------
// Validation: Phone and Email
// ------------------------------------------------------------------------------
$clean_phone = preg_replace('/[^\d]/', '', $phone);
if (strlen($clean_phone) < 8 || strlen($clean_phone) > 15) {
    if ($is_ajax) {
        header('Content-Type: application/json; charset=utf-8');
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Please enter a valid contact phone number (at least 8-10 digits) so our technician can reach you.']);
        exit;
    }
}

if (!empty($email) && !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    if ($is_ajax) {
        header('Content-Type: application/json; charset=utf-8');
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Please enter a valid email address.']);
        exit;
    }
}

// ------------------------------------------------------------------------------
// Service & Problem Formatting
// ------------------------------------------------------------------------------
$problem_labels = [
    'not_starting'  => "Won't turn on / Black screen / Freezing",
    'scam_virus'    => "Bank scam call / Remote pop-up / Virus warning",
    'broken_screen' => "Broken or cracked laptop screen",
    'slow_computer' => "Extremely slow / Needs SSD speed upgrade",
    'lost_files'    => "Lost files or clicking hard drive (Data Recovery)",
    'lost_data'     => "Lost files or clicking hard drive (Data Recovery)",
    'other'         => "Other general computer issue"
];

$liquid_labels = [
    'water'        => 'Plain Water',
    'coffee_tea'   => 'Coffee or Tea (with/without sugar)',
    'beer_wine'    => 'Wine, Beer or Alcohol',
    'soft_drink'   => 'Soft Drink / Juice',
    'other'        => 'Other Liquid'
];

$incident_labels = [
    'phone_scam'    => 'Phone caller connected to computer (Fake Telstra/NBN/Bank)',
    'popup_lock'    => 'Red screen pop-up / loud siren locking screen',
    'banking_scare' => 'Scammer instructed customer to log into online banking',
    'virus_malware' => 'Computer very slow, strange toolbars & ads',
    'other'         => 'Other security issue'
];

// Determine job category & display title
$job_type = "REPAIR";
$details_summary = "";

if (!empty($liquid_type)) {
    $job_type = "LIQUID SPILL";
    $liquid_desc = $liquid_labels[$liquid_type] ?? $liquid_type;
    $details_summary = "Liquid: {$liquid_desc}";
    if (!empty($laptop_model)) {
        $details_summary .= " • Device: {$laptop_model}";
    }
} elseif (!empty($incident_type)) {
    $job_type = "SCAM & VIRUS";
    $incident_desc = $incident_labels[$incident_type] ?? $incident_type;
    $details_summary = "Incident: {$incident_desc}";
} else {
    $problem_desc = $problem_labels[$problem] ?? ($problem ?: "General Diagnostic & Repair");
    $details_summary = $problem_desc;
}

if (!empty($notes)) {
    $details_summary .= " (Notes: {$notes})";
}

// ------------------------------------------------------------------------------
// Compose Emergency Email Subject & Body
// ------------------------------------------------------------------------------
$clean_name = htmlspecialchars_decode($name, ENT_QUOTES);
$clean_suburb = htmlspecialchars_decode($suburb, ENT_QUOTES);
$subject = "🚨 {$job_type}: {$clean_name} ({$clean_suburb}) - {$phone}";

$email_row = '';
if (!empty($email)) {
    $email_row = "
      <div class='item'>
        <div class='label'>Customer Email</div>
        <div class='value'>
          <a href='mailto:{$email}' style='color: #2563eb; font-weight: 700; text-decoration: underline;'>{$email}</a>
        </div>
      </div>";
}

$device_row = '';
if (!empty($laptop_model)) {
    $device_row = "
      <div class='item'>
        <div class='label'>Laptop Brand &amp; Model</div>
        <div class='value' style='font-weight: 700; color: #0f172a;'>{$laptop_model}</div>
      </div>";
}

$notes_row = '';
if (!empty($notes)) {
    $notes_row = "
      <div class='item'>
        <div class='label'>Customer Notes / Description</div>
        <div class='value' style='background: #fffbeb; padding: 12px; border-radius: 6px; border-left: 3px solid #f59e0b; color: #92400e; font-size: 15px;'>{$notes}</div>
      </div>";
}

$message = "
<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='utf-8'>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f1f5f9; margin: 0; padding: 20px; color: #0f172a; }
    .card { max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 12px; border: 2px solid #dc2626; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
    .header { background: #dc2626; color: #ffffff; padding: 20px 24px; text-align: center; }
    .header h2 { margin: 0; font-size: 22px; font-weight: 800; letter-spacing: -0.02em; }
    .content { padding: 24px; }
    .item { margin-bottom: 16px; border-bottom: 1px solid #e2e8f0; padding-bottom: 12px; }
    .item:last-child { border-bottom: none; }
    .label { font-size: 12px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px; }
    .value { font-size: 17px; font-weight: 600; color: #0f172a; line-height: 1.4; }
    .action-btn-row { margin-top: 10px; }
    .phone-btn { display: inline-block; background: #dc2626; color: #ffffff !important; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: 800; font-size: 16px; margin-right: 8px; }
    .sms-btn { display: inline-block; background: #0284c7; color: #ffffff !important; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: 800; font-size: 16px; }
    .footer { background: #f8fafc; padding: 16px 24px; font-size: 13px; color: #64748b; text-align: center; border-top: 1px solid #e2e8f0; }
  </style>
</head>
<body>
  <div class='card'>
    <div class='header'>
      <h2>✚ NEW EMERGENCY DISPATCH: {$job_type}</h2>
      <p style='margin: 6px 0 0; opacity: 0.95; font-size: 14px;'>Delivered to info@computerrepairsfast.com.au &amp; aykut@kalmaz.com</p>
    </div>
    <div class='content'>
      <div class='item'>
        <div class='label'>Customer Name</div>
        <div class='value'>{$name}</div>
      </div>
      <div class='item'>
        <div class='label'>Contact Phone &amp; Instant Technician Actions</div>
        <div class='value'>
          <div style='font-size: 20px; font-weight: 800; margin-bottom: 8px; color: #dc2626;'>{$phone}</div>
          <div class='action-btn-row'>
            <a href='tel:{$phone}' class='phone-btn'>📞 Call Customer Now</a>
            <a href='sms:{$phone}' class='sms-btn'>💬 SMS Customer</a>
          </div>
        </div>
      </div>
      {$email_row}
      <div class='item'>
        <div class='label'>Suburb / Location / Workshop Preference</div>
        <div class='value'>📍 {$suburb}</div>
      </div>
      {$device_row}
      <div class='item'>
        <div class='label'>Fault / Problem / Incident Summary</div>
        <div class='value' style='color: #dc2626; font-weight: 700;'>{$details_summary}</div>
      </div>
      {$notes_row}
      <div class='item'>
        <div class='label'>Pricing Policy Stated to Customer</div>
        <div class='value' style='font-size: 15px;'>$80 Fixed Diagnostic (Credited inside total repair fee • $0 Call-Out Fee across Brisbane)</div>
      </div>
      <div class='item'>
        <div class='label'>Booking Source Page</div>
        <div class='value' style='font-size: 14px; color: #64748b;'>{$source_page}</div>
      </div>
    </div>
    <div class='footer'>
      Computer Repairs Fast Emergency Dispatch • 0401 148 654 • info@computerrepairsfast.com.au
    </div>
  </div>
</body>
</html>
";

// Email headers
$reply_to = !empty($email) ? "{$name} <{$email}>" : "info@computerrepairsfast.com.au";
$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8\r\n";
$headers .= "From: Computer Repairs Fast <no-reply@computerrepairsfast.com.au>\r\n";
$headers .= "Reply-To: {$reply_to}\r\n";
$headers .= "X-Mailer: PHP/" . phpversion();

// Send email with envelope sender (-f) for strict SPF/DMARC alignment on Hostinger
$mail_sent = @mail($to, $subject, $message, $headers, "-f no-reply@computerrepairsfast.com.au");

if ($is_ajax) {
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode([
        'success' => true,
        'message' => 'Thank you! Your emergency repair request has been received. Our technician will call you shortly on ' . $phone . '.'
    ]);
    exit;
}

// Fallback HTML Confirmation page for non-JS browsers
?>
<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Booking Received | Computer Repairs Fast</title>
  <link rel="stylesheet" href="/css/style.css">
</head>
<body style="display: flex; min-height: 100vh; flex-direction: column; justify-content: center; align-items: center; background: #f8fafc; padding: 20px; text-align: center;">
  <div style="max-width: 540px; background: #fff; border: 2px solid #dc2626; border-radius: 16px; padding: 40px; box-shadow: 0 10px 25px rgba(0,0,0,0.08);">
    <div style="font-size: 54px; margin-bottom: 16px;">✅</div>
    <h1 style="color: #0f172a; font-size: 28px; font-weight: 900; margin-bottom: 12px;">Repair Request Dispatched!</h1>
    <p style="font-size: 18px; color: #475569; line-height: 1.6; margin-bottom: 24px;">
      Thank you, <strong><?php echo $name; ?></strong>. We have alerted our on-duty mobile technician. We will call you on <strong><?php echo $phone; ?></strong> shortly.
    </p>
    <div style="background: #fef2f2; border: 1.5px solid #fee2e2; border-radius: 10px; padding: 16px; margin-bottom: 24px;">
      <p style="margin: 0; color: #991b1b; font-weight: 700; font-size: 16px;">
        Need immediate emergency service?
      </p>
      <div style="display: flex; gap: 10px; justify-content: center; margin-top: 12px; flex-wrap: wrap;">
        <a href="tel:0401148654" class="btn btn-emergency dynamic-phone" style="font-size: 16px; padding: 10px 20px;">
          📞 Call: 0401 148 654
        </a>
        <a href="sms:0401148654?body=Hi%20Computer%20Repairs%20Fast,%20I%20just%20submitted%20a%20booking" class="btn btn-secondary" style="font-size: 16px; padding: 10px 20px; background: #0284c7; color: #fff;">
          💬 Text / SMS
        </a>
      </div>
    </div>
    <a href="/" style="color: #64748b; font-weight: 700; text-decoration: underline;">← Return to Homepage</a>
  </div>
</body>
</html>