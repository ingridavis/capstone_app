// using js to help automatically slugify the title 


const titleInput = document.querySelector('input[name=title');
const slugInput = document.querySelector('input[name=slug');

// auto changing the title to better slugify
const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g,'-and-')   // and becomes &
        .replace(/[\s\W]+/g,'-') // spaces becomes dash

};

titleInput.addEventListener('keyup',(e) =>{
    slugInput.setAttribute('value', slugify(titleInput.value));
});