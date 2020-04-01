


// 
myForm = document.forms["recipe-form"]
function validate() {

    if (myForm["recipeName"].value == "") {
        alert("Please provide your Recipe Name!");
        myForm["recipeName"].focus();
        return false;
    }
    if (myForm["ingredients"].value == "") {
        alert("Please provide your ingredients");
        myForm["ingredients"].focus();
        return false;
    }
    if (myForm["how_to"].value == "") {
        alert("Please provide your Steps");
        myForm["how_to"].focus();
        return false;
    }
    let file = myForm["recipe_image"].value
    image = isImage(file)
    alert(image)
    if (!image) {
        alert("Please provide a image");
        return false
    }
    return (true);
}
function isImage(file) {
    let splitEx = file.split('.').pop();
    let allowedExtentions = ["jpg", "jpeg", "png", "gif"]
    let res = allowedExtentions.includes(splitEx)
    return res;//returns true or false
}

$(document).ready(function () {
    myForm.onsubmit = function () {
        // do what you want
        
        return false
    }
})
