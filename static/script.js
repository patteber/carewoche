document.addEventListener("DOMContentLoaded", function () {

    printCaretakerQueue = function(orderJson){
        var list = document.getElementById("caretakerQueue");
        order = JSON.parse(orderJson);
        var first = true;
        for(var key in order) {
            if(first){
                first = false;
                list.innerHTML = "<b>" + order[key] + "</b><br>";
            } else {
                list.innerHTML += order[key] + "<br>";
            }
        }
    }

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            printCaretakerQueue(xmlHttp.responseText);
    }
    xmlHttp.open("GET", "http://127.0.0.1:8000/order/", true); // true for asynchronous
    xmlHttp.send("'Content-Type': 'application/json'");

    // Next Button
    const Nextbutton = document.getElementById('next-btn');
    Nextbutton.addEventListener('click', async _ => {
      try {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                printCaretakerQueue(xmlHttp.responseText);
        }
        xmlHttp.open("POST", "http://127.0.0.1:8000/order/iterate/", true); // true for asynchronous
        xmlHttp.send("'Content-Type': 'application/json'");
        xmlHttp.send(null);

        } catch(err) {
        console.error(`Error: ${err}`);
      }
    });

    // Change Order Button
    const changeButton = document.getElementById('change-btn');
    changeButton.addEventListener("click", () => {
                document.getElementById("dialog")
                    .showModal();
            });
        document.getElementById("close-dialog")
            .addEventListener("click", () => {
                document.getElementById("dialog")
                    .close();
            });
    // change Dialog
    const postChangeButton = document.getElementById('postChange-btn');
    postChangeButton.addEventListener('click', async _ => {
        try {
            const name = document.getElementById('name-input').value;
            const offset = document.getElementById('offset-input').value;
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
                    printCaretakerQueue(xmlHttp.responseText);
                    document.getElementById("dialog").close();
                }
                if (xmlHttp.status === 404) {
                    alert("Name " + name + " not found!")
                }
            }
            xmlHttp.open("POST", "http://127.0.0.1:8000/order/change/", true);
            xmlHttp.setRequestHeader("Content-Type", "application/json");
            xmlHttp.send(JSON.stringify({"name": name, "offset": offset}));
        } catch(err) {
          console.error(`Error: ${err}`);
        }
    });
    
    // Edit Button 
    const editButton = document.getElementById('edit-btn');
    editButton.addEventListener('click', async _ => {
        try {
            alert("Not implemented yet.")
            /*
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
                    printCaretakerQueue(xmlHttp.responseText);
                    document.getElementById("dialog").close();
                }
                if (xmlHttp.status === 404) {
                    alert("Name " + name + " not found!")
                }
            }
            xmlHttp.open("POST", "http://127.0.0.1:8000/order/change/", true);
            xmlHttp.setRequestHeader("Content-Type", "application/json");
            xmlHttp.send(JSON.stringify({"name": name, "offset": offset}));
            */
        } catch(err) {
          console.error(`Error: ${err}`);
        }
    }); 

    /*var jsonData = [
        { Name: "Max", Alter: 25, Stadt: "Berlin" },
        { Name: "Anna", Alter: 30, Stadt: "Hamburg" },
        { Name: "Peter", Alter: 22, Stadt: "München" }
    ];*/
/*
    alert(res["Members"])
    var jsonData = res["Members"]

    // Tabelle erstellen
    var table = document.getElementById("jsonTable");

    // Tabellenkopf erstellen
    var thead = table.createTHead();
    var headerRow = thead.insertRow();
    Object.keys(jsonData[0]).forEach(function (key) {
        var th = document.createElement("th");
        th.appendChild(document.createTextNode(key));
        headerRow.appendChild(th);
    });

    // Tabelleninhalt erstellen
    var tbody = table.createTBody();
    jsonData.forEach(function (row) {
        var tr = tbody.insertRow();
        Object.values(row).forEach(function (value) {
            var td = tr.insertCell();
            td.appendChild(document.createTextNode(value));
        });
    });*/
});
