document.addEventListener("DOMContentLoaded", function () {
    // JSON-Daten laden (Beispiel-Daten)
/*    fetch('http://127.0.0.1:8000/members/', {
    headers: {
        'Content-Type': 'application/json'
    }
    })
    .then(response => response.text())
    .then(text => console.log(text))
  */  
     callback = function(t) {alert(t)}

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", "http://127.0.0.1:8000/members/", true); // true for asynchronous 
    xmlHttp.send("'Content-Type': 'application/json'");
    alert("here we go")
    var res = xmlHttp.responseText
    
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
