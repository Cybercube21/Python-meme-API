function loadFile(filePath) {
    var result = null;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", filePath, false);
    xmlhttp.send();
    result = xmlhttp.responseText;
    $("#api_calls_counter").text(result);
  }