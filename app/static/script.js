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
    var url = this.location.protocol + "//" + this.location.host
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            printCaretakerQueue(xmlHttp.responseText);
    }
    xmlHttp.open("GET", url + "/order/", true);
    xmlHttp.setRequestHeader("Content-Type", "application/json");
    xmlHttp.send(null);

    // Next Button
    const Nextbutton = document.getElementById('next-btn');
    Nextbutton.addEventListener('click', async _ => {
      try {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                printCaretakerQueue(xmlHttp.responseText);
        }
        xmlHttp.open("POST", url + "/order/iterate/", true);
        xmlHttp.setRequestHeader("Content-Type", "application/json");
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
            xmlHttp.open("POST", url + "/order/change/", true);
            xmlHttp.setRequestHeader("Content-Type", "application/json");
            xmlHttp.send(JSON.stringify({"name": name, "offset": offset}));
        } catch(err) {
          console.error(`Error: ${err}`);
        }
    });
});
