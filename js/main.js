document.addEventListener("DOMContentLoaded", () => {
  // Repair Pricing Matrix
  const pricingData = {
    screen: {
      windows: { range: "$230 – $330", time: "Same Day (1–3 Hours)", note: "Genuine OEM Full HD panels (School touchscreens $350–$430)" },
      macbook: { range: "$290 – $550+", time: "Same Day / 24 Hours", note: "Retina display assembly calibration" },
      gaming: { range: "$260 – $390", time: "Same Day (144Hz–240Hz)", note: "High refresh-rate gaming panels" },
      desktop: { range: "$150 – $250", time: "1–2 Hours", note: "Monitor advice / GPU bench diagnostic" }
    },
    battery: {
      windows: { range: "Market Part + Labor", time: "Same Day (1–2 Hours)", note: "Original high-capacity batteries" },
      macbook: { range: "Market Part + Labor", time: "Same Day", note: "OEM cells with battery health reset" },
      gaming: { range: "Market Part + Labor", time: "Same Day", note: "High-drain gaming battery modules" },
      desktop: { range: "CMOS replacement ($45)", time: "30 Mins", note: "CMOS battery & BIOS reset" }
    },
    boot: {
      windows: { range: "$150 – $250", time: "2–4 Hours", note: "BSOD, Windows repair, bootloop fix" },
      macbook: { range: "$150 – $260", time: "2–4 Hours", note: "macOS reinstall, flashing folder fix" },
      gaming: { range: "$150 – $250", time: "2–4 Hours", note: "RAM/BIOS/SSD hardware diagnostic" },
      desktop: { range: "$150 – $250", time: "1–3 Hours", note: "Power supply & motherboard check" }
    },
    ssd: {
      windows: { range: "Part Cost + $180 Fee", time: "Same Day (2–3 Hours)", note: "New SSD at market price + 100% full sector clone" },
      macbook: { range: "Part Cost + $180 Fee", time: "Same Day", note: "High-speed upgrade + OS migration" },
      gaming: { range: "Part Cost + $180 Fee", time: "Same Day", note: "Gen4 M.2 NVMe blazing fast storage" },
      desktop: { range: "Part Cost + $180 Fee", time: "Same Day", note: "SATA or NVMe + Data transfer" }
    },
    data: {
      windows: { range: "$150 – $500", time: "Same Day / Next Day", note: "Logical file recovery, clicking drives & dead SSDs (No Data, No Fee)" },
      macbook: { range: "$150 – $500", time: "Same Day / Next Day", note: "Apple APFS / FileVault recovery (No Data, No Fee)" },
      gaming: { range: "$150 – $500", time: "Same Day / Next Day", note: "SSD file recovery & game saves (No Data, No Fee)" },
      desktop: { range: "$150 – $500", time: "Same Day / Next Day", note: "Emergency lab recovery (No Data, No Fee)" }
    },
    virus: {
      windows: { range: "$150 – $250", time: "Same Day (1–2 Hours)", note: "Bank scam, remote access purge, written bank report" },
      macbook: { range: "$150 – $250", time: "Same Day (1–2 Hours)", note: "Malware, fake popups, browser hijack" },
      gaming: { range: "$150 – $250", time: "Same Day", note: "Rootkit purge & background bloatware" },
      desktop: { range: "$150 – $250", time: "Same Day (1–2 Hours)", note: "Total system scan & security report" }
    }
  };

  const deviceSelect = document.getElementById("quoteDevice");
  const issueSelect = document.getElementById("quoteIssue");
  const priceDisplay = document.getElementById("quotePrice");
  const timeDisplay = document.getElementById("quoteTime");
  const noteDisplay = document.getElementById("quoteNote");

  function updateEstimate() {
    if (!deviceSelect || !issueSelect || !priceDisplay) return;
    const device = deviceSelect.value || "windows";
    const issue = issueSelect.value || "screen";

    const data = pricingData[issue]?.[device] || {
      range: "$130 – $190",
      time: "Same Day",
      note: "Standard flat-rate diagnostic included"
    };

    priceDisplay.textContent = data.range;
    timeDisplay.textContent = `⚡ Typical Turnaround: ${data.time}`;
    if (noteDisplay) {
      noteDisplay.textContent = data.note;
    }
  }

  if (deviceSelect && issueSelect) {
    deviceSelect.addEventListener("change", updateEstimate);
    issueSelect.addEventListener("change", updateEstimate);
    updateEstimate();
  }

  // FAQ Accordion (Supporting .faq-question, .faq-q, and .faq-card)
  const faqButtons = document.querySelectorAll(".faq-question, .faq-q");
  faqButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      const card = btn.closest(".faq-card") || btn.parentElement;
      const answer = btn.nextElementSibling || card.querySelector(".faq-a, .faq-answer");
      if (!answer) return;

      const isCurrentlyOpen = answer.style.display === "block" || answer.classList.contains("is-open");
      const icon = btn.querySelector(".faq-toggle-icon, span:last-child");

      // Optional: keep container siblings independent or close other cards in same group
      const parentContainer = card.parentElement;
      if (parentContainer) {
        parentContainer.querySelectorAll(".faq-a, .faq-answer").forEach(a => {
          if (a !== answer) {
            a.style.display = "none";
            a.classList.remove("is-open");
            const siblingBtn = a.previousElementSibling;
            if (siblingBtn) {
              siblingBtn.setAttribute("aria-expanded", "false");
              const sibIcon = siblingBtn.querySelector(".faq-toggle-icon, span:last-child");
              if (sibIcon && (sibIcon.textContent === "−" || sibIcon.textContent === "+")) sibIcon.textContent = "+";
            }
          }
        });
      }

      if (isCurrentlyOpen) {
        answer.style.display = "none";
        answer.classList.remove("is-open");
        btn.setAttribute("aria-expanded", "false");
        if (icon && (icon.textContent === "−" || icon.textContent === "+")) icon.textContent = "+";
      } else {
        answer.style.display = "block";
        answer.classList.add("is-open");
        btn.setAttribute("aria-expanded", "true");
        if (icon && (icon.textContent === "−" || icon.textContent === "+")) icon.textContent = "−";
      }
    });
  });

  // Dedicated FAQ Page Search & Category Filter
  const faqSearchInput = document.getElementById("faqSearchInput");
  if (faqSearchInput) {
    faqSearchInput.addEventListener("input", (e) => {
      const term = e.target.value.toLowerCase().trim();
      const allCards = document.querySelectorAll(".faq-card");
      let visibleCount = 0;

      allCards.forEach(card => {
        const text = card.textContent.toLowerCase();
        if (!term || text.includes(term)) {
          card.style.display = "";
          visibleCount++;
        } else {
          card.style.display = "none";
        }
      });

      // Show/hide empty state
      const noResultsMsg = document.getElementById("faqNoResults");
      if (noResultsMsg) {
        noResultsMsg.style.display = visibleCount === 0 ? "block" : "none";
      }
    });
  }

  // AJAX Booking Form Handler
  const pageLoadTimestamp = Date.now() / 1000;

  document.querySelectorAll(".ajax-booking-form").forEach(form => {
    // Stamp load timestamp into anti-spam field
    let timeInput = form.querySelector("input[name='form_timestamp']");
    if (!timeInput) {
      timeInput = document.createElement("input");
      timeInput.type = "hidden";
      timeInput.name = "form_timestamp";
      form.appendChild(timeInput);
    }
    timeInput.value = pageLoadTimestamp;

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector("button[type='submit']");
      const originalBtnText = submitBtn ? submitBtn.innerHTML : "Book";
      
      // Remove any previous error message
      const existingError = form.querySelector(".form-error-msg");
      if (existingError) existingError.remove();

      const formData = new FormData(form);
      const customerPhone = (formData.get("phone") || "").toString().trim();
      const cleanPhoneDigits = customerPhone.replace(/\D/g, "");

      // Client-side phone validation
      if (cleanPhoneDigits.length < 8) {
        const errDiv = document.createElement("div");
        errDiv.className = "form-error-msg";
        errDiv.style.cssText = "background: #fef2f2; border: 1.5px solid #ef4444; color: #b91c1c; padding: 12px; border-radius: 8px; margin-bottom: 14px; font-weight: 700; font-size: 0.95rem;";
        errDiv.textContent = "Please enter a valid phone number (at least 8-10 digits) so our technician can reach you.";
        form.insertBefore(errDiv, submitBtn);
        return;
      }

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = "⏳ Sending Request to Technician...";
      }

      try {
        const response = await fetch(form.action, {
          method: "POST",
          body: formData,
          headers: {
            "X-Requested-With": "XMLHttpRequest"
          }
        });

        const result = await response.json();
        if (result.success) {
          form.innerHTML = `
            <div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 12px; padding: 24px 20px; text-align: center; margin: 10px 0;">
              <div style="font-size: 44px; margin-bottom: 10px;">✅</div>
              <h3 style="color: #166534; font-size: 1.45rem; font-weight: 800; margin-bottom: 8px; letter-spacing: -0.02em;">Repair Request Dispatched!</h3>
              <p style="color: #15803d; font-size: 1.05rem; line-height: 1.5; margin-bottom: 18px;">
                Thank you! Our on-duty technician has been notified and will call you on <strong>${customerPhone}</strong> shortly.
              </p>
              <div style="background: #ffffff; border: 1.5px solid #bbf7d0; border-radius: 10px; padding: 16px; margin-bottom: 12px;">
                <p style="margin: 0 0 10px; font-weight: 700; color: #0f172a; font-size: 0.95rem;">Need immediate emergency support?</p>
                <div style="display: flex; gap: 8px; justify-content: center; flex-wrap: wrap;">
                  <a href="tel:0401148654" class="btn btn-emergency dynamic-phone" style="font-size: 0.95rem; padding: 10px 18px;">
                    📞 Call 0401 148 654
                  </a>
                  <a href="sms:0401148654?body=Hi%20Computer%20Repairs%20Fast,%20I%20just%20submitted%20a%20booking%20for%20my%20computer" class="btn" style="background: #0284c7; color: #ffffff; font-size: 0.95rem; padding: 10px 18px; border-radius: 8px; text-decoration: none; font-weight: 700;">
                    💬 Text / SMS
                  </a>
                </div>
              </div>
              <p style="margin: 0; font-size: 0.88rem; color: #166534; font-weight: 600;">
                💡 Fixed $80 diagnostic fee is inside your repair fee (credited towards total quote). Zero call-out fee.
              </p>
            </div>
          `;
        } else {
          // Display validation error
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalBtnText;
          }
          const errDiv = document.createElement("div");
          errDiv.className = "form-error-msg";
          errDiv.style.cssText = "background: #fef2f2; border: 1.5px solid #ef4444; color: #b91c1c; padding: 12px; border-radius: 8px; margin-bottom: 14px; font-weight: 700; font-size: 0.95rem;";
          errDiv.textContent = result.error || "Submission failed. Please check your details and try again.";
          form.insertBefore(errDiv, submitBtn);
        }
      } catch (err) {
        console.warn("AJAX submission fallback:", err);
        // Fallback to native submission
        form.submit();
      }
    });
  });

  // Phone placeholder updater if needed
  window.updateGlobalPhone = function(newPhone, cleanTel) {
    document.querySelectorAll(".dynamic-phone").forEach(el => {
      el.textContent = newPhone;
    });
    document.querySelectorAll("a[href^='tel:']").forEach(el => {
      el.href = `tel:${cleanTel}`;
    });
  };

  // ============================================================================
  // Top Navigation & Dropdown Menus (Desktop & Mobile)
  // ============================================================================
  const mobileToggle = document.getElementById("mobileMenuToggle") || document.getElementById("mobileMenuBtn");
  const mobileDrawer = document.getElementById("mobileNavDrawer") || document.getElementById("mobileDrawer");

  if (mobileToggle && mobileDrawer) {
    function toggleMobileMenu(forceClose = false) {
      const shouldOpen = forceClose ? false : !mobileDrawer.classList.contains("is-open");
      if (shouldOpen) {
        mobileDrawer.classList.add("is-open");
        mobileToggle.classList.add("is-active");
        mobileToggle.setAttribute("aria-expanded", "true");
        mobileDrawer.setAttribute("aria-hidden", "false");
        document.body.style.overflow = "hidden";
      } else {
        mobileDrawer.classList.remove("is-open");
        mobileToggle.classList.remove("is-active");
        mobileToggle.setAttribute("aria-expanded", "false");
        mobileDrawer.setAttribute("aria-hidden", "true");
        document.body.style.overflow = "";
      }
    }

    mobileToggle.addEventListener("click", (e) => {
      e.stopPropagation();
      toggleMobileMenu();
    });

    // Dedicated Drawer Close Button
    const drawerCloseBtn = document.getElementById("drawerCloseBtn") || document.getElementById("closeDrawerBtn") || mobileDrawer.querySelector(".drawer-close-btn, .close-drawer-btn");
    if (drawerCloseBtn) {
      drawerCloseBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        toggleMobileMenu(true);
      });
    }

    // Auto-close drawer when clicking an internal link
    mobileDrawer.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", () => {
        toggleMobileMenu(true);
      });
    });

    // Keyboard ESC key closes mobile drawer and desktop dropdowns
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" || e.key === "Esc") {
        if (mobileDrawer.classList.contains("is-open")) {
          toggleMobileMenu(true);
          mobileToggle.focus();
        }
        document.querySelectorAll(".nav-item.dropdown-active").forEach(item => {
          item.classList.remove("dropdown-active");
          const btn = item.querySelector(".dropdown-toggle");
          if (btn) btn.setAttribute("aria-expanded", "false");
        });
      }
    });

    // Mobile Accordion Items
    document.querySelectorAll(".drawer-acc-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const item = btn.closest(".drawer-acc-item");
        const isOpen = item.classList.contains("is-open");
        
        // Close other accordions
        document.querySelectorAll(".drawer-acc-item").forEach(other => {
          if (other !== item) {
            other.classList.remove("is-open");
            const otherBtn = other.querySelector(".drawer-acc-btn");
            if (otherBtn) otherBtn.setAttribute("aria-expanded", "false");
          }
        });

        if (isOpen) {
          item.classList.remove("is-open");
          btn.setAttribute("aria-expanded", "false");
        } else {
          item.classList.add("is-open");
          btn.setAttribute("aria-expanded", "true");
        }
      });
    });

    // Close drawer when any sublink or CTA is tapped
    document.querySelectorAll(".drawer-sublink, .drawer-single-btn, .drawer-cta-row a").forEach(link => {
      link.addEventListener("click", () => {
        toggleMobileMenu(true);
      });
    });

    // Close on resize to desktop
    window.addEventListener("resize", () => {
      if (window.innerWidth > 992 && mobileDrawer.classList.contains("is-open")) {
        toggleMobileMenu(true);
      }
    });
  }

  // Desktop Dropdown Toggles (for touch-enabled laptops/tablets)
  document.querySelectorAll(".dropdown-toggle").forEach(toggle => {
    toggle.addEventListener("click", (e) => {
      e.stopPropagation();
      const item = toggle.closest(".nav-item");
      const isActive = item.classList.contains("dropdown-active");
      
      document.querySelectorAll(".nav-item.dropdown-active").forEach(other => {
        if (other !== item) {
          other.classList.remove("dropdown-active");
          const otherBtn = other.querySelector(".dropdown-toggle");
          if (otherBtn) otherBtn.setAttribute("aria-expanded", "false");
        }
      });

      if (isActive) {
        item.classList.remove("dropdown-active");
        toggle.setAttribute("aria-expanded", "false");
      } else {
        item.classList.add("dropdown-active");
        toggle.setAttribute("aria-expanded", "true");
      }
    });
  });

  // Close desktop dropdown on click outside
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".nav-item")) {
      document.querySelectorAll(".nav-item.dropdown-active").forEach(item => {
        item.classList.remove("dropdown-active");
        const btn = item.querySelector(".dropdown-toggle");
        if (btn) btn.setAttribute("aria-expanded", "false");
      });
    }
  });

  // ============================================================================
  // Navigate to Top Button (Smooth Scroll)
  // ============================================================================
  const backToTopBtn = document.getElementById("backToTopBtn");
  if (backToTopBtn) {
    let scrollTicking = false;
    const updateBackToTopVisibility = () => {
      if (window.scrollY > 300) {
        backToTopBtn.classList.add("is-visible");
      } else {
        backToTopBtn.classList.remove("is-visible");
      }
      scrollTicking = false;
    };

    window.addEventListener("scroll", () => {
      if (!scrollTicking) {
        window.requestAnimationFrame(updateBackToTopVisibility);
        scrollTicking = true;
      }
    }, { passive: true });

    // Initial check on load
    updateBackToTopVisibility();

    backToTopBtn.addEventListener("click", () => {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    });
  }

  /* ==============================================================================
     Google Business Profile Reviews Carousel Controller
     Touch-friendly, auto-sliding, location-filterable, keyboard accessible
     ============================================================================== */
  const reviewsTrack = document.getElementById("reviewsTrack");
  if (reviewsTrack) {
    const prevBtn = document.getElementById("reviewsPrevBtn");
    const nextBtn = document.getElementById("reviewsNextBtn");
    const dotsContainer = document.getElementById("carouselDots");
    const filterPills = document.querySelectorAll(".filter-pill");
    const allCards = Array.from(reviewsTrack.querySelectorAll(".review-card"));
    
    let currentIndex = 0;
    let autoPlayTimer = null;
    let touchStartX = 0;
    let touchCurrentX = 0;
    let isSwiping = false;

    // Get cards per view based on viewport width
    const getCardsPerView = () => {
      const w = window.innerWidth;
      if (w <= 680) return 1;
      if (w <= 992) return 2;
      return 3;
    };

    // Filter cards
    let activeFilter = "all";
    const getVisibleCards = () => {
      if (activeFilter === "all") return allCards;
      return allCards.filter(card => card.getAttribute("data-location") === activeFilter);
    };

    // Update slides & dots
    const updateCarousel = (animate = true) => {
      // Show/hide cards according to filter
      allCards.forEach(card => {
        if (activeFilter === "all" || card.getAttribute("data-location") === activeFilter) {
          card.classList.remove("hidden");
        } else {
          card.classList.add("hidden");
        }
      });

      const visibleCards = getVisibleCards();
      const cardsPerView = getCardsPerView();
      const maxIndex = Math.max(0, visibleCards.length - cardsPerView);

      if (currentIndex > maxIndex) currentIndex = maxIndex;
      if (currentIndex < 0) currentIndex = 0;

      // Calculate shift
      if (visibleCards.length > 0 && visibleCards[0]) {
        const cardWidth = visibleCards[0].offsetWidth;
        const gap = 24; // matches css gap
        const shift = currentIndex * (cardWidth + gap);
        reviewsTrack.style.transition = animate ? "transform 0.45s cubic-bezier(0.25, 1, 0.5, 1)" : "none";
        reviewsTrack.style.transform = `translateX(-${shift}px)`;
      } else {
        reviewsTrack.style.transform = "translateX(0px)";
      }

      // Render dots
      const numDots = Math.max(1, visibleCards.length - cardsPerView + 1);
      if (dotsContainer) {
        dotsContainer.innerHTML = "";
        for (let i = 0; i < numDots; i++) {
          const dot = document.createElement("button");
          dot.type = "button";
          dot.className = `carousel-dot ${i === currentIndex ? "active" : ""}`;
          dot.setAttribute("role", "tab");
          dot.setAttribute("aria-selected", i === currentIndex ? "true" : "false");
          dot.setAttribute("aria-label", `Go to review slide ${i + 1}`);
          dot.addEventListener("click", () => {
            currentIndex = i;
            updateCarousel();
            restartAutoPlay();
          });
          dotsContainer.appendChild(dot);
        }
      }

      // Arrows visual feedback
      if (prevBtn) {
        prevBtn.style.opacity = (currentIndex === 0 && maxIndex === 0) ? "0.4" : "1";
      }
      if (nextBtn) {
        nextBtn.style.opacity = (currentIndex >= maxIndex && maxIndex === 0) ? "0.4" : "1";
      }
    };

    // Navigation buttons
    if (prevBtn) {
      prevBtn.addEventListener("click", () => {
        const visibleCards = getVisibleCards();
        const cardsPerView = getCardsPerView();
        const maxIndex = Math.max(0, visibleCards.length - cardsPerView);
        if (currentIndex > 0) {
          currentIndex--;
        } else {
          currentIndex = maxIndex; // loop
        }
        updateCarousel();
        restartAutoPlay();
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener("click", () => {
        const visibleCards = getVisibleCards();
        const cardsPerView = getCardsPerView();
        const maxIndex = Math.max(0, visibleCards.length - cardsPerView);
        if (currentIndex < maxIndex) {
          currentIndex++;
        } else {
          currentIndex = 0; // loop
        }
        updateCarousel();
        restartAutoPlay();
      });
    }

    // Filter pill buttons
    filterPills.forEach(pill => {
      pill.addEventListener("click", () => {
        filterPills.forEach(p => {
          p.classList.remove("active");
          p.setAttribute("aria-selected", "false");
        });
        pill.classList.add("active");
        pill.setAttribute("aria-selected", "true");
        activeFilter = pill.getAttribute("data-filter") || "all";
        currentIndex = 0;
        updateCarousel();
        restartAutoPlay();
      });
    });

    // Auto Play (5500ms)
    const startAutoPlay = () => {
      stopAutoPlay();
      autoPlayTimer = setInterval(() => {
        const visibleCards = getVisibleCards();
        const cardsPerView = getCardsPerView();
        const maxIndex = Math.max(0, visibleCards.length - cardsPerView);
        if (maxIndex > 0) {
          if (currentIndex < maxIndex) {
            currentIndex++;
          } else {
            currentIndex = 0;
          }
          updateCarousel();
        }
      }, 5500);
    };

    const stopAutoPlay = () => {
      if (autoPlayTimer) {
        clearInterval(autoPlayTimer);
        autoPlayTimer = null;
      }
    };

    const restartAutoPlay = () => {
      stopAutoPlay();
      startAutoPlay();
    };

    // Pause on hover
    const wrapper = document.querySelector(".reviews-carousel-wrapper");
    if (wrapper) {
      wrapper.addEventListener("mouseenter", stopAutoPlay);
      wrapper.addEventListener("mouseleave", startAutoPlay);
    }

    // Touch swipe support
    const viewport = document.getElementById("reviewsViewport");
    if (viewport) {
      viewport.addEventListener("touchstart", (e) => {
        touchStartX = e.touches[0].clientX;
        touchCurrentX = touchStartX;
        isSwiping = true;
        stopAutoPlay();
      }, { passive: true });

      viewport.addEventListener("touchmove", (e) => {
        if (!isSwiping) return;
        touchCurrentX = e.touches[0].clientX;
      }, { passive: true });

      viewport.addEventListener("touchend", () => {
        if (!isSwiping) return;
        isSwiping = false;
        const diffX = touchStartX - touchCurrentX;
        const threshold = 40; // min swipe distance in px
        const visibleCards = getVisibleCards();
        const cardsPerView = getCardsPerView();
        const maxIndex = Math.max(0, visibleCards.length - cardsPerView);

        if (diffX > threshold) {
          // swipe left -> next
          if (currentIndex < maxIndex) currentIndex++;
          else currentIndex = 0;
          updateCarousel();
        } else if (diffX < -threshold) {
          // swipe right -> prev
          if (currentIndex > 0) currentIndex--;
          else currentIndex = maxIndex;
          updateCarousel();
        }
        startAutoPlay();
      }, { passive: true });
    }

    // Resize listener
    window.addEventListener("resize", () => {
      updateCarousel(false);
    });

    // Initial setup
    updateCarousel(false);
    startAutoPlay();
  }


  // Initialize Suburb Coverage & Postcode Checker
  initSuburbChecker();


// ==========================================================================
// Interactive Suburb Coverage & Postcode Checker
// ==========================================================================
// ==========================================================================
// Interactive Suburb Coverage & Postcode Checker (Redesigned & Sleek)
// ==========================================================================
function initSuburbChecker() {
  const container = document.getElementById("suburb-checker");
  if (!container) return;

  const searchInput = document.getElementById("suburbSearchInput");
  const clearBtn = document.getElementById("suburbClearBtn");
  const dropdown = document.getElementById("suburbDropdownMenu");
  const quickPills = container.querySelectorAll(".quick-suburb-pill");
  const toggleDirBtn = document.getElementById("toggleAllDirBtn");
  const allDir = document.getElementById("allSuburbsDirectory");
  const dirItems = container.querySelectorAll(".dir-suburb-item");

  const resultTitle = document.getElementById("resultSuburbTitle");
  const resultSummary = document.getElementById("resultDispatchSummary");
  const resultHub = document.getElementById("resultHubName");
  const resultTime = document.getElementById("resultResponseTime");
  const resultSpan = document.getElementById("resultSuburbSpan");
  const resultSms = document.getElementById("resultSmsLink");

  // Collect all suburbs data from dir-suburb-items
  const allSuburbs = Array.from(dirItems).map((item) => ({
    name: item.dataset.name || "",
    postcode: item.dataset.postcode || "",
    hub: item.dataset.hub || "",
    time: item.dataset.time || "",
    dropoff: item.dataset.dropoff || "",
    el: item
  }));

  function setSuburb(name, postcode, hub, time, dropoff, scrollIntoView = false) {
    if (resultTitle) resultTitle.textContent = `${name}, QLD ${postcode}`;
    if (resultSummary) {
      resultSummary.innerHTML = `Primary mobile technician dispatched from our <strong>${hub}</strong> (approx. ${time} arrival). Workshop drop-off also available at <strong>${dropoff}</strong> with free dedicated parking.`;
    }
    if (resultHub) resultHub.textContent = hub;
    if (resultTime) resultTime.textContent = `Est. ${time} travel window`;
    if (resultSpan) resultSpan.textContent = name;
    if (resultSms) {
      resultSms.href = `sms:0401148654?body=${encodeURIComponent(
        `Hi ComputerRepairsFast, I need a repair quote for my computer in ${name} (${postcode}):`
      )}`;
    }

    // Update active quick pills
    quickPills.forEach((p) => {
      if (p.dataset.name === name) {
        p.classList.add("active");
      } else {
        p.classList.remove("active");
      }
    });

    if (searchInput) {
      searchInput.value = `${name} (${postcode})`;
      if (clearBtn) clearBtn.style.display = "flex";
    }

    if (dropdown) dropdown.style.display = "none";

    if (scrollIntoView) {
      const card = document.getElementById("coverageResultCard");
      if (card) {
        card.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
    }
  }

  // Quick pick pill clicks
  quickPills.forEach((pill) => {
    pill.addEventListener("click", () => {
      setSuburb(
        pill.dataset.name,
        pill.dataset.postcode,
        pill.dataset.hub,
        pill.dataset.time,
        pill.dataset.dropoff,
        true
      );
    });
  });

  // Directory item clicks
  dirItems.forEach((item) => {
    item.addEventListener("click", () => {
      setSuburb(
        item.dataset.name,
        item.dataset.postcode,
        item.dataset.hub,
        item.dataset.time,
        item.dataset.dropoff,
        true
      );
    });
  });

  // Toggle directory
  if (toggleDirBtn && allDir) {
    toggleDirBtn.addEventListener("click", () => {
      const isHidden = allDir.style.display === "none";
      allDir.style.display = isHidden ? "block" : "none";
      toggleDirBtn.innerHTML = isHidden
        ? "▴ Hide Suburbs Directory"
        : "▾ Browse All 70 Suburbs by Region";
    });
  }

  // Search input and autocomplete
  if (searchInput && dropdown) {
    searchInput.addEventListener("input", (e) => {
      const q = e.target.value.toLowerCase().trim();
      if (!q) {
        dropdown.style.display = "none";
        if (clearBtn) clearBtn.style.display = "none";
        return;
      }
      if (clearBtn) clearBtn.style.display = "flex";

      const matches = allSuburbs.filter(
        (s) =>
          s.name.toLowerCase().includes(q) || s.postcode.includes(q)
      ).slice(0, 7);

      if (matches.length > 0) {
        dropdown.innerHTML = matches
          .map(
            (m) => `
          <button type="button" class="dropdown-match-item" data-name="${m.name}" data-postcode="${m.postcode}" data-hub="${m.hub}" data-time="${m.time}" data-dropoff="${m.dropoff}">
            <span class="dropdown-match-name">
              ${m.name} <span class="match-zip">${m.postcode}</span>
            </span>
            <span class="dropdown-match-meta">✓ $0 Call-Out (${m.time})</span>
          </button>
        `
          )
          .join("");
        dropdown.style.display = "block";

        // Bind clicks to dropdown items
        dropdown.querySelectorAll(".dropdown-match-item").forEach((btn) => {
          btn.addEventListener("click", () => {
            setSuburb(
              btn.dataset.name,
              btn.dataset.postcode,
              btn.dataset.hub,
              btn.dataset.time,
              btn.dataset.dropoff,
              true
            );
          });
        });
      } else {
        dropdown.innerHTML = `
          <div style="padding: 12px; font-size: 0.88rem; color: #64748b; text-align: center;">
            No direct match for "${q}". We service all Brisbane Greater Metro! 
            <a href="tel:0401148654" style="color: #dc2626; font-weight: 700;">Call 0401 148 654</a>
          </div>
        `;
        dropdown.style.display = "block";
      }
    });

    searchInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        e.preventDefault();
        const firstBtn = dropdown.querySelector(".dropdown-match-item");
        if (firstBtn) firstBtn.click();
      }
    });

    // Close dropdown on click outside
    document.addEventListener("click", (e) => {
      if (!container.contains(e.target)) {
        dropdown.style.display = "none";
      }
    });
  }

  // Clear button
  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      if (searchInput) {
        searchInput.value = "";
        searchInput.focus();
      }
      clearBtn.style.display = "none";
      if (dropdown) dropdown.style.display = "none";
    });
  }

  // Initial set East Brisbane
  const defaultPill = Array.from(quickPills).find((p) => p.dataset.name === "Carindale") || quickPills[0];
  if (defaultPill) {
    setSuburb(
      defaultPill.dataset.name,
      defaultPill.dataset.postcode,
      defaultPill.dataset.hub,
      defaultPill.dataset.time,
      defaultPill.dataset.dropoff,
      false
    );
  }
}

  // Quote Request Template Copy Function
  window.copyQuoteTemplate = function(btnId, targetId) {
    const el = document.getElementById(targetId || 'quoteTemplateText');
    if (!el) return;
    const text = el.innerText || el.textContent;
    navigator.clipboard.writeText(text).then(() => {
      const btn = document.getElementById(btnId || 'copyQuoteBtn');
      if (btn) {
        const originalHtml = btn.innerHTML;
        btn.innerHTML = '<span>✓ Copied to Clipboard!</span>';
        btn.style.background = '#16a34a';
        setTimeout(() => {
          btn.innerHTML = originalHtml;
          btn.style.background = '';
        }, 3000);
      }
    }).catch(err => {
      console.warn('Clipboard copy failed:', err);
    });
  };

});

// Search bar removed