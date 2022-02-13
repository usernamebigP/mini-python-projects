function addMovie(e){
    let movie=e.target.parentNode.childNodes[1].value

    $.get("/getMovie",{m:movie},function(data){
        //form_box=document.getElementById("1")
        //form_box.style.display="none"
        let data_box=document.createElement("div")
        data_box.innerHTML+=`<br><img src=${data.poster}><br><br>title:${data.title}<br> year:${data.year}<br> rating:${data.rating}<br> user_reviews:${data.user_reviews}<br>rated:${data.rated}<br>hours:${data.hours}<br>genre:${data.genre}<br> release-date:${data.rdate} <br> summary:${data.summary} <br> cast: <br>`
        
        for(let char in data.cast){
            data_box.innerHTML+=`<br>Actor : ${char} , Role : ${data.cast[char]}</br>`
        }
        e.target.parentNode.appendChild(data_box)
        })
}