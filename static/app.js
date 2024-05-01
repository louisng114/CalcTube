// Add dark mode functionalities
function toggleDarkMode() {
    const htmlTag = document.getElementsByTagName("html")[0];
    const switchIcon = document.querySelector('.form-check .icon');
    const integralSymbols = document.querySelectorAll('.integral');
    if (htmlTag.dataset.bsTheme === 'dark') {
        htmlTag.dataset.bsTheme = 'light';
        switchIcon.innerHTML = '<i class="fas fa-sun"></i>'; //change switch icon
        integralSymbols.forEach((image) => image.src = "../static/images/integral-symbol.png");
        localStorage.setItem('darkMode', 'light'); // Store dark mode state in localStorage
    } else {
        htmlTag.dataset.bsTheme = 'dark';
        switchIcon.innerHTML = '<i class="fas fa-moon"></i>'; //change switch icon
        integralSymbols.forEach((image) => image.src = "../static/images/integral-symbol-dark.png");
        localStorage.setItem('darkMode', 'dark'); // Store dark mode state in localStorage
    }
}
  
// Function to check and apply dark mode state from localStorage
function applyDarkModeFromStorage() {
    const darkModeState = localStorage.getItem('darkMode');
    const switchIcon = document.querySelector('.form-check .icon');
    const integralSymbols = document.querySelectorAll('.integral');
    if (darkModeState === 'dark') {
        const htmlTag = document.getElementsByTagName('html')[0];
        htmlTag.dataset.bsTheme = 'dark';
        integralSymbols.forEach((image) => image.src = "../static/images/integral-symbol-dark.png");
        switchIcon.innerHTML = '<i class="fas fa-moon"></i>';
    } else {
        switchIcon.innerHTML = '<i class="fas fa-sun"></i>';
    }
}
  
  // Listen for the Bootstrap dark mode toggle event
  document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.querySelector('[data-bs-toggle="dark"]');
    if (toggle) {
      toggle.addEventListener('click', toggleDarkMode);
    }
    
    // Apply dark mode state from localStorage
    applyDarkModeFromStorage();
});
  

// Listen for the Bootstrap dark mode toggle event
document.addEventListener('DOMContentLoaded', function() {
  const toggle = document.querySelector('[data-bs-toggle="dark"]');
  if (toggle) {
    toggle.addEventListener('click', toggleDarkMode);
  }
});
// Add vote buttons functionalities
document.addEventListener('DOMContentLoaded', function() {
    const voteForms = document.querySelectorAll('.voteForm');

    voteForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            vote(form);
        });
    });
});

const vote = async function (form) {
    const response = await axios.post(form.getAttribute("action"));
    const data = response.data;

    // update vote count
    const voteCountElement = form.parentElement.querySelector(".voteCount");
    voteCountElement.innerText = data.voteCount;

    // update vote icon
    const iconElement = form.querySelector(".voteIcon");
    if (data.voted) {
        iconElement.classList.add('fa-solid');
        iconElement.classList.remove('fa-regular');
    } else {
        iconElement.classList.remove('fa-solid');
        iconElement.classList.add('fa-regular');
    }
}

// Add favorite button functionalities
document.addEventListener('DOMContentLoaded', function() {
    const favForms = document.querySelectorAll('.favForm');

    favForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            favorite(form);
        });
    });
});

const favorite = async function (form) {
    const response = await axios.post(form.getAttribute("action"));
    const data = response.data;

    // update vote icon
    const iconElement = form.querySelector(".voteIcon");
    if (data.voted) {
        iconElement.classList.add('fa-solid');
        iconElement.classList.remove('fa-regular');
    } else {
        iconElement.classList.remove('fa-solid');
        iconElement.classList.add('fa-regular');
    }
}

// Add Bootstrap styles to topics form items
document.addEventListener('DOMContentLoaded', function() {
    const topicsForm = document.querySelector(".topicsForm");
    if (topicsForm) {
        const topicList = topicsForm.querySelector("ul");    
        const topicItems = topicsForm.querySelectorAll("li");
    
        topicList.classList.add("row");
    
        for (let item of topicItems) {
            item.classList.add("col-md-6", "col-xl-4", "col-xxl-3");
        }
    }
});
