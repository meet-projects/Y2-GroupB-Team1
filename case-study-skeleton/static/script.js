document.addEventListener("DOMContentLoaded", () => {
  let currentSlide = 0;
  const slides = document.getElementsByClassName("slide");
  const dots = document.getElementsByClassName("dot");
  let timer;

  function showSlide(slideIndex) {
    if (slideIndex >= slides.length) {
      currentSlide = 0;
    } else if (slideIndex < 0) {
      currentSlide = slides.length - 1;
    } else {
      currentSlide = slideIndex;
    }

    for (let i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    slides[currentSlide].style.display = "block";

    for (let i = 0; i < dots.length; i++) {
      dots[i].classList.remove("active");
    }
    dots[currentSlide].classList.add("active");
  }

  function prevSlide() {
    showSlide(currentSlide - 1);
  }

  function nextSlide() {
    showSlide(currentSlide + 1);
  }

  // Function to make text go down when hovering over the image
  const slideTextContainers = document.querySelectorAll(".slide-text-container");
  slideTextContainers.forEach(container => {
    const slideText = container.querySelector(".slide-text");
    const lineHeight = parseInt(window.getComputedStyle(slideText).lineHeight);
    const maxLines = 3; // Set the maximum number of lines for the text

    // Check if the text exceeds the maximum lines
    if (slideText.clientHeight > lineHeight * maxLines) {
      container.style.overflow = "hidden";
      slideText.style.transition = "transform 0.3s ease";

      // Make the text go down when hovering over the image
      container.addEventListener("mouseenter", () => {
        const lines = slideText.clientHeight / lineHeight;
        const translateY = (lines - maxLines) * lineHeight * -1;
        slideText.style.transform = `translateY(${translateY}px)`;
      });

      // Reset the text position when not hovering
      container.addEventListener("mouseleave", () => {
        slideText.style.transform = "translateY(0)";
      });
    }
  });

  function autoSlide() {
    nextSlide();
  }

  function startTimer() {
    timer = setInterval(autoSlide, 3000);
  }

  function stopTimer() {
    clearInterval(timer);
  }

  // Show the first slide
  showSlide(currentSlide);

  // Start the timer
  startTimer();

  // Update click event listener for right arrow on the pictures
  const rightArrow = document.querySelector(".next");
  rightArrow.addEventListener("click", () => {
    stopTimer();
    nextSlide();
    startTimer();
  });

  // Update click event listener for left arrow on the pictures
  const leftArrow = document.querySelector(".prev");
  leftArrow.addEventListener("click", () => {
    stopTimer();
    prevSlide();
    startTimer();
  });
});