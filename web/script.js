document.addEventListener("DOMContentLoaded", function () {
    // JSON-Daten laden (Beispiel-Daten)
    var jsonData = [
        { Name: "Max", Alter: 25, Stadt: "Berlin" },
        { Name: "Anna", Alter: 30, Stadt: "Hamburg" },
        { Name: "Peter", Alter: 22, Stadt: "München" }
    ];

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
    });
});
