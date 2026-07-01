// Dark Mode Toggle

const darkModeBtn = document.getElementById("darkModeBtn");

darkModeBtn.addEventListener("click", () => {
  document.body.classList.toggle("light-mode");
});

// Chatbot Popup

const chatBtn = document.getElementById("chatBtn");
const chatPopup = document.getElementById("chatPopup");

chatBtn.addEventListener("click", () => {

  if (chatPopup.style.display === "none") {
    chatPopup.style.display = "block";
  } else {
    chatPopup.style.display = "none";
  }

});

// Search Functionality

const searchInput = document.getElementById("searchInput");
const cards = document.querySelectorAll(".card");

searchInput.addEventListener("keyup", () => {

  const searchValue = searchInput.value.toLowerCase();

  cards.forEach((card) => {

    const text = card.innerText.toLowerCase();

    if (text.includes(searchValue)) {
      card.style.display = "block";
    } else {
      card.style.display = "none";
    }

  });

});