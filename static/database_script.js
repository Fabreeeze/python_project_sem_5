function deleteItem(itemId) {
    fetch('/delete_item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ itemId: itemId })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.success) {
            // Remove the deleted item from the UI
            const itemElement = document.getElementById(itemId);
            if (itemElement) {
                itemElement.remove();
            }
        } 
        else {
            console.error('Error deleting item');
        }
    })
    .catch(error => console.error('Error:', error));
}


//this is repeated code below for now 
function changeTab(tabName) {
    var i, tabContent, tab;


    // Deactivates all tabs
    tab = document.getElementsByClassName("tab");
    for (i = 0; i < tab.length; i++) {
        tab[i].classList.remove("active");
    }

    // Activates the selected tab
    document.getElementById(tabName).classList.add("active");
}
