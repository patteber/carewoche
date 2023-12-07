document.addEventListener("DOMContentLoaded", function () {

    printMembers = function(orderJson){
        var list = document.getElementById("membersList");
        members = JSON.parse(orderJson);
        list.innerHTML = "";
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
    xmlHttp.open("GET", url + "/members/?skip=0&limit=100", true);
    xmlHttp.setRequestHeader("Content-Type", "application/json");
    xmlHttp.send(null);

    // New Button
    const newButton = document.getElementById('new-btn');
    newButton.addEventListener("click", () => {
                document.getElementById("newDialog")
                    .showModal();
            });
        document.getElementById("closeNew-dialog")
            .addEventListener("click", () => {
                document.getElementById("newDialog")
                    .close();
            });
    // New Dialog
    const postNewButton = document.getElementById('postNew-btn');
    postNewButton.addEventListener('click', async _ => {
        try {
            const name = document.getElementById('newName-input').value;
            var active = document.getElementById('newActive-input').checked ? true : false;
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4 && xmlHttp.status == 201){
                    printMembers(xmlHttp.responseText);
                    document.getElementById("newDialog").close();
                }
                if (xmlHttp.status === 404) {
                    alert("Name " + name + " not found!")
                }
            }
            xmlHttp.open("POST", url + "/members/", true);
            xmlHttp.setRequestHeader("Content-Type", "application/json");
            xmlHttp.send(JSON.stringify({"name": name, "active": active}));
        } catch(err) {
          console.error(`Error: ${err}`);
        }
    });

    // Del Button
    const delButton = document.getElementById('del-btn');
    delButton.addEventListener("click", () => {
                document.getElementById("delDialog")
                    .showModal();
            });
        document.getElementById("closedel-dialog")
            .addEventListener("click", () => {
                document.getElementById("delDialog")
                    .close();
            });
    // Del Dialog
    const postDelButton = document.getElementById('postdel-btn');
    postDelButton.addEventListener('click', async _ => {
        try {
            const name = document.getElementById('delName-input').value;
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
                    printMembers(xmlHttp.responseText);
                    document.getElementById("delDialog").close();
                }
                if (xmlHttp.status === 404) {
                    alert("Name " + name + " not found!")
                }
            }
            xmlHttp.open("DELETE", url + "/members/", true);
            xmlHttp.setRequestHeader("Content-Type", "application/json");
            xmlHttp.send(JSON.stringify({"name": name}));
        } catch(err) {
          console.error(`Error: ${err}`);
        }
    });

    // Update Button
    const updButton = document.getElementById('change2-btn');
    updButton.addEventListener("click", () => {
                document.getElementById("updDialog")
                    .showModal();
            });
        document.getElementById("closeupd-dialog")
            .addEventListener("click", () => {
                document.getElementById("updDialog")
                    .close();
            });
    // Update Dialog
    const postupdButton = document.getElementById('postupd-btn');
    postupdButton.addEventListener('click', async _ => {
        try {
            const name = document.getElementById('updName-input').value;
            var active = document.getElementById('updActive-input').checked ? true : false;
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4 && xmlHttp.status == 201){
                    printMembers(xmlHttp.responseText);
                    document.getElementById("updDialog").close();
                }
                if (xmlHttp.status === 404) {
                    alert("Name " + name + " not found!")
                }
            }
            xmlHttp.open("POST", url + "/members/", true);
            xmlHttp.setRequestHeader("Content-Type", "application/json");
            xmlHttp.send(JSON.stringify({"name": name, "active": active}));
        } catch(err) {
            console.error(`Error: ${err}`);
        }
    });

});
