
// used to fetch data from api and render the query readable to user 
function search() {
    let search = document.querySelector("#search")
    fetch("https://api.edamam.com/api/recipes/v2?type=public&q=" + search.value + "&app_id=9c7c4f7b&app_key=320ec3f3dfec25144591bc7573633b36")
        // then statement used to return data inn json form
        .then(res => {
            return res.json();
        })
        .then(data => {
            // then statement returns data that is iterated through to retrieve desired information and display to user with for loops
            console.log(data)
            let results = document.querySelector("#results");
            let food = data.hits;
            let i = 0;
            let j = 0;
            for (recipe of food) {
                results.innerHTML += `<img src="${food[i].recipe.image}"><br><h2>${food[i].recipe.cuisineType}</h2><h4>${food[i].recipe.label}</h4><a href="${food[i].recipe.shareAs}">View
            Recipe</a><br>`
                // nested for loop used to retrieve more data to display to user
                for (let j = 0; j < food[i].recipe.ingredientLines.length; j++) {
                    results.innerHTML += `<h6>${food[i].recipe.ingredientLines[j]}
                </h6>`}
                i++;
            }
        })
}

        // function to show hidden results div until search
function show() {
    show = document.getElementById("hidden");
    show = show.style.visibility = "visible";
}

