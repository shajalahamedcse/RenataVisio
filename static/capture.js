var buttonCapture = document.getElementById("capture");
var buttonTrain=document.getElementById("train")

buttonCapture.onclick = function() {
    // var url = window.location.href + "record_status";
   
    
    // XMLHttpRequest
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
             alert(xhr.responseText);
        }
    }
    xhr.open("POST", "/capture_status");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status:"true" }));
};

buttonTrain.onclick = function() {
    // var url = window.location.href + "record_status";
   
    
    // XMLHttpRequest
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
             alert(xhr.responseText);
        }
    }
    xhr.open("POST", "/train_status");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ train:"true" }));
};