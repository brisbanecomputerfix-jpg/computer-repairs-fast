/**
 * Simple, Instant Local Search Engine for ComputerRepairsFast.com.au
 * Searches services, guides, FAQs, suburbs & keywords directly from site content.
 * Displays results in a clean, instant dropdown under the search bar.
 */
(function() {
  let searchIndex = null;
  let activeIndex = -1;

  // Fallback services in case of network latency
  const FALLBACK_SERVICES = [
    { title: "Laptop Screen Replacement", url: "/services/laptop-screen-repairs.html", type: "service", badge: "⚡ Service", desc: "Cracked or flickering display? Fitted same-day in Brisbane. Standard FHD from $230." },
    { title: "Apple MacBook Repairs", url: "/services/apple-macbook-repairs.html", type: "service", badge: "⚡ Service", desc: "MacBook Air & Pro Retina screens, battery swelling, logic board & liquid spill cleaning." },
    { title: "Laptop Battery Replacement", url: "/services/laptop-battery-replacement.html", type: "service", badge: "⚡ Service", desc: "Swollen batteries, rapid battery drain, charging port fixes with OEM original parts." },
    { title: "Virus & Scamware Cleanup", url: "/services/scam-virus-removal.html", type: "service", badge: "⚡ Service", desc: "Immediate scam assistance, Telstra/NBN remote access tool purge, bank security check." },
    { title: "Slow PC to Fast NVMe SSD", url: "/services/slow-computer-speed-up.html", type: "service", badge: "⚡ Service", desc: "Make your computer 5x to 10x faster with a cloned SSD upgrade. Zero data loss." },
    { title: "Broken Laptop Hinge Repair", url: "/services/lenovo-laptop-repairs.html", type: "service", badge: "⚡ Service", desc: "Cracked brass standoffs and split palmrest hinge rebuilding. Save on new casing." }
  ];

  // Preload search index immediately on script load
  async function loadIndex() {
    if (searchIndex && searchIndex.length) return searchIndex;
    try {
      const res = await fetch('/search-index.json?v=2.4');
      if (res.ok) {
        searchIndex = await res.json();
        return searchIndex;
      }
    } catch (e) {
      console.warn('Search index fetch error, using fallback:', e);
    }
    searchIndex = FALLBACK_SERVICES;
    return searchIndex;
  }

  // Highlight matched terms
  function highlight(text, terms) {
    if (!text || !terms.length) return text || '';
    let escaped = terms.map(t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).filter(Boolean);
    if (!escaped.length) return text;
    let regex = new RegExp(`(${escaped.join('|')})`, 'gi');
    return text.replace(regex, '<mark class="search-hl">$1</mark>');
  }

  // Core search matching & scoring
  function search(query) {
    if (!searchIndex) searchIndex = FALLBACK_SERVICES;
    const cleanQuery = query.toLowerCase().trim();
    if (!cleanQuery) return [];

    const terms = cleanQuery.split(/\s+/).filter(Boolean);

    let matches = searchIndex.filter(item => {
      const haystack = (
        (item.title || '') + ' ' +
        (item.desc || '') + ' ' +
        (item.keywords || '') + ' ' +
        (item.category || '')
      ).toLowerCase();
      return terms.every(t => haystack.includes(t));
    });

    // Score: exact match > prefix > title includes > service priority > keyword match
    matches.sort((a, b) => {
      const aTitle = (a.title || '').toLowerCase();
      const bTitle = (b.title || '').toLowerCase();
      let aScore = 0;
      let bScore = 0;

      if (aTitle === cleanQuery) aScore += 300;
      if (bTitle === cleanQuery) bScore += 300;

      if (aTitle.startsWith(cleanQuery)) aScore += 150;
      if (bTitle.startsWith(cleanQuery)) bScore += 150;

      if (aTitle.includes(cleanQuery)) aScore += 80;
      if (bTitle.includes(cleanQuery)) bScore += 80;

      if (a.type === 'service') aScore += 40;
      if (b.type === 'service') bScore += 40;

      terms.forEach(t => {
        if (aTitle.includes(t)) aScore += 25;
        if (bTitle.includes(t)) bScore += 25;
        if (a.keywords && a.keywords.includes(t)) aScore += 15;
        if (b.keywords && b.keywords.includes(t)) bScore += 15;
      });

      return bScore - aScore;
    });

    return matches.slice(0, 8); // Top 8 most relevant matches
  }

  // Render dropdown results
  function renderDropdown(container, results, query) {
    if (!container) return;
    activeIndex = -1;

    if (!query) {
      // Show popular recommendations when focused but empty
      container.innerHTML = `
        <div class="search-dd-header">
          <span>🔥 Popular Repairs in Brisbane:</span>
        </div>
        <div class="search-dd-list">
          ${FALLBACK_SERVICES.slice(0, 4).map((item, idx) => `
            <a href="${item.url}" class="search-dd-item" data-index="${idx}">
              <span class="search-dd-badge badge-service">⚡ Service</span>
              <div class="search-dd-info">
                <div class="search-dd-title">${item.title}</div>
                <div class="search-dd-desc">${item.desc}</div>
              </div>
              <span class="search-dd-arrow" aria-hidden="true">→</span>
            </a>
          `).join('')}
        </div>
      `;
      container.style.display = 'block';
      return;
    }

    const terms = query.toLowerCase().split(/\s+/).filter(Boolean);

    if (!results.length) {
      container.innerHTML = `
        <div class="search-dd-empty">
          <div class="empty-title">No direct matches for "${query}"</div>
          <p class="empty-sub">We repair 100+ hardware and software issues across Greater Brisbane. Speak with a mobile technician:</p>
          <div class="empty-actions">
            <a href="tel:0401148654" class="btn btn-emergency btn-sm dynamic-phone">📞 Call 0401 148 654</a>
            <a href="sms:0401148654?body=Hi%20Computer%20Repairs%20Fast,%20I'm%20asking%20about:%20${encodeURIComponent(query)}" class="btn btn-white btn-sm">💬 Send SMS</a>
          </div>
        </div>
      `;
      container.style.display = 'block';
      return;
    }

    container.innerHTML = `
      <div class="search-dd-header">
        <span>Found <strong>${results.length}</strong> matching services &amp; guides:</span>
        <span class="search-dd-tip">Press ↵ Enter to view</span>
      </div>
      <div class="search-dd-list">
        ${results.map((item, idx) => {
          const badgeType = item.type === 'service' ? 'badge-service' :
                            item.type === 'guide' ? 'badge-guide' :
                            item.type === 'location' ? 'badge-location' :
                            item.type === 'faq' ? 'badge-faq' : 'badge-core';
          const badgeLabel = item.badge || item.category || 'Service';

          return `
            <a href="${item.url}" class="search-dd-item" data-index="${idx}">
              <span class="search-dd-badge ${badgeType}">${badgeLabel}</span>
              <div class="search-dd-info">
                <div class="search-dd-title">${highlight(item.title, terms)}</div>
                <div class="search-dd-desc">${highlight(item.desc || '', terms)}</div>
              </div>
              <span class="search-dd-arrow" aria-hidden="true">→</span>
            </a>
          `;
        }).join('')}
      </div>
      <div class="search-dd-footer">
        <span>Need urgent help? <a href="tel:0401148654" class="dynamic-phone">Call 0401 148 654</a> for same-day mobile dispatch.</span>
      </div>
    `;
    container.style.display = 'block';
  }

  // Bind a search input element
  function setupSearchComponent(inputEl, clearBtnEl, dropdownEl) {
    if (!inputEl || !dropdownEl) return;

    // Load index in background
    loadIndex();

    // Input typing
    inputEl.addEventListener('input', () => {
      const q = inputEl.value.trim();
      if (clearBtnEl) clearBtnEl.style.display = q ? 'block' : 'none';
      if (!q) {
        dropdownEl.style.display = 'none';
        return;
      }
      const results = search(q);
      renderDropdown(dropdownEl, results, q);
    });

    // Focus
    inputEl.addEventListener('focus', () => {
      const q = inputEl.value.trim();
      if (!q) {
        renderDropdown(dropdownEl, [], '');
      } else {
        const results = search(q);
        renderDropdown(dropdownEl, results, q);
      }
    });

    // Clear button
    if (clearBtnEl) {
      clearBtnEl.addEventListener('click', (e) => {
        e.preventDefault();
        inputEl.value = '';
        clearBtnEl.style.display = 'none';
        dropdownEl.style.display = 'none';
        inputEl.focus();
      });
    }

    // Keyboard navigation
    inputEl.addEventListener('keydown', (e) => {
      const items = dropdownEl.querySelectorAll('.search-dd-item');
      if (!items.length) return;

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        activeIndex = (activeIndex + 1) % items.length;
        updateSelection(items);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        activeIndex = (activeIndex - 1 + items.length) % items.length;
        updateSelection(items);
      } else if (e.key === 'Enter') {
        if (activeIndex >= 0 && items[activeIndex]) {
          e.preventDefault();
          window.location.href = items[activeIndex].getAttribute('href');
        } else if (items.length > 0) {
          e.preventDefault();
          window.location.href = items[0].getAttribute('href');
        }
      } else if (e.key === 'Escape') {
        dropdownEl.style.display = 'none';
      }
    });

    function updateSelection(items) {
      items.forEach((item, idx) => {
        if (idx === activeIndex) {
          item.classList.add('is-active');
          item.scrollIntoView({ block: 'nearest' });
        } else {
          item.classList.remove('is-active');
        }
      });
    }

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!inputEl.contains(e.target) && !dropdownEl.contains(e.target) && (!clearBtnEl || !clearBtnEl.contains(e.target))) {
        dropdownEl.style.display = 'none';
      }
    });
  }

  // Initialize on page load
  document.addEventListener('DOMContentLoaded', () => {
    // 1. Subbar Search
    const subbarInput = document.getElementById('siteGlobalSearchInput');
    const subbarClear = document.getElementById('siteGlobalSearchClear');
    const subbarDropdown = document.getElementById('siteGlobalSearchDropdown');
    if (subbarInput) {
      setupSearchComponent(subbarInput, subbarClear, subbarDropdown);
    }

    // 2. Hero Search on home or articles hub (if present)
    const heroInput = document.getElementById('heroSearchInput');
    const heroClear = document.getElementById('heroSearchClear');
    let heroDropdown = document.getElementById('heroSearchDropdown');
    if (heroInput) {
      if (!heroDropdown) {
        heroDropdown = document.createElement('div');
        heroDropdown.id = 'heroSearchDropdown';
        heroDropdown.className = 'subbar-search-dropdown hero-search-dropdown';
        heroDropdown.style.display = 'none';
        heroInput.parentNode.appendChild(heroDropdown);
      }
      setupSearchComponent(heroInput, heroClear, heroDropdown);
    }

    // 3. Quick Popular Tag Pills (click to search)
    document.querySelectorAll('.search-quick-pill, .hero-search-tag, .popular-tag-btn').forEach(pill => {
      pill.addEventListener('click', (e) => {
        e.preventDefault();
        const query = pill.getAttribute('data-query') || pill.getAttribute('data-search') || pill.textContent.replace(/[^\w\s]/gi, '').trim();
        const targetInput = subbarInput || heroInput;
        const targetDropdown = subbarDropdown || heroDropdown;
        if (targetInput && targetDropdown) {
          targetInput.value = query;
          targetInput.focus();
          if (subbarClear) subbarClear.style.display = 'block';
          const results = search(query);
          renderDropdown(targetDropdown, results, query);
        }
      });
    });
  });
})();
