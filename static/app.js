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
