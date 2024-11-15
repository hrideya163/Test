// Object to keep track of the number of times each item is clicked
let itemCounts = {};

function addItem(foodItem) {
    if (itemCounts[foodItem]) {
        itemCounts[foodItem]++;
    } else {
        itemCounts[foodItem] = 1;
    }

    // Send data to the backend
    fetch('/calculate_calories', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(itemCounts)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('totalCalories').innerText = 'Total Calories: ' + data.total_calories;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
