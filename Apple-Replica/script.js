const slides = document.querySelectorAll(".slide");
const track = document.querySelector(".slider-track");
const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const hero = document.querySelector(".hero");
let current = 0;

function updateSlides() {
  slides.forEach((slide, i) => slide.classList.remove("active", "prev", "next"));

  // Set active slide
  slides[current].classList.add("active");

  // Set previous slide
  const prev = (current - 1 + slides.length) % slides.length;
  slides[prev].classList.add("prev");

  // Set next slide
  const next = (current + 1) % slides.length;
  slides[next].classList.add("next");

  // Move the track (center the active slide)
  const offset = -current * (slides[0].offsetWidth + (window.innerWidth * 0.04)); // accounts for margin
  track.style.transform = `translateX(${offset + window.innerWidth * 0.2}px)`; // keep 20% preview visible
}

function nextSlide() {
  current = (current + 1) % slides.length;
  updateSlides();
}

function prevSlide() {
  current = (current - 1 + slides.length) % slides.length;
  updateSlides();
}

// Hamburger menu toggle
hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("active");
  if (window.innerWidth <= 480) {
    if (navLinks.classList.contains("active")) {
      hero.style.marginTop = "250px"; // Increase margin-top when menu is open
    } else {
      hero.style.marginTop = "0"; // Reset margin-top when menu is closed
    }
  }
});

// Close menu when clicking outside or on a link
document.addEventListener("click", (e) => {
  if (!hamburger.contains(e.target) && !navLinks.contains(e.target)) {
    navLinks.classList.remove("active");
    if (window.innerWidth <= 480) {
      hero.style.marginTop = "0"; // Reset margin-top when menu is closed
    }
  }
});

updateSlides();
setInterval(nextSlide, 3000);

// Optional: resize handling for responsiveness
window.addEventListener("resize", updateSlides);
