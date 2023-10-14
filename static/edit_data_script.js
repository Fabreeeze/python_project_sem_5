document.addEventListener('DOMContentLoaded',() => {
    const form = document.querySelector('form');


    form.addEventListener('submit', async(e) =>{
        e.preventDefault;
        const formData = new FormData(form);
        const response = await fetch('/submit_edited_data',{
            method : 'POST',
            body : formData
        })
        const result = await response.json();
        console.log("formdata = "+formdata);
        console.log("result = "+result);
        if(result.success){
            console.log("image data successfully stored in db");
        }
    })
})