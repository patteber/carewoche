document.addEventListener("DOMContentLoaded", function () {

    printMembers = function(orderJson){
        var list = document.getElementById("membersList");
        members = JSON.parse(orderJson);
        for(var key in members) {
            if(members[key]["IsActive"]){
                list.innerHTML += "<b>"+key+"</b>"; 
            }else{
                list.innerHTML += key;
            }
            list.innerHTML += "<br>";   
        }
        
    }

    var url = this.location.protocol + "//" + this.location.host
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            printMembers(xmlHttp.responseText);
    }
    xmlHttp.open("GET", url + "/members/", true); // true for asynchronous
    xmlHttp.send("'Content-Type': 'application/json'");

});
