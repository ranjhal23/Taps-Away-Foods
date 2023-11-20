const search = () =>{
    const searchbox=document.getElementById("search-item").value.toUpperCase()
    const storeitems=document.getElementById("menu-items")
    const product= document.querySelectorAll(".card")
    const pname= document.getElementsByTagName("h2")
    for (var i = 0; i< pname.length; i++) {
        let match = product[i].getElementsByTagName('h2')[0];
        if(match){

            let textvalue = match.textContent || match.innerHTML

            if(textvalue.toUpperCase().indexOf(searchbox) > -1){
                product[i].style.display = "";
            }
            else{
                product[i].style.display = "none";
            }
        } 
        
    }
}
function openNewDiv() {
    var openedDiv = document.getElementById('openedDiv');

    // Toggle the display property between 'none' and 'block'
    if (openedDiv.style.display === 'none') {
      openedDiv.style.display = 'block';
    } else {
      openedDiv.style.display = 'none';
    }
  }