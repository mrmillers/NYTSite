var map;
var geocoder;
function search(){
    document.getElementById("news_list").innerHTML = "Searching...";
    var location = document.getElementById("location").value;
    var people = document.getElementById("people").value;
    var key = document.getElementById("key").value;
    var start_time = document.getElementById("time_start").value;
    var end_time = document.getElementById("time_end").value;

    var query = "/query?key=" + key + "&location=" + location + "&people=" + people + "&start_time=" + start_time + "&end_time=" + end_time;
    $.getJSON(query,function (data){
        var list = "<ol>";
        $.each(data,function (key){
            list += "<li><p><a target=\"_blank\" href=\"/article/" + data[key]["nid"] +  "\">" + data[key]["title"] +"</a></p><p>";
            if (data[key]["author"]!="") list+= "Author:" + data[key]["author"];
            if (data[key]["location"]!="") list+= "Location:" + data[key]["location"];
            if (data[key]["date"]!="") list+= "Date:" + data[key]["date"];
            list += "</p></li>";
        });
        list += "</ol>"
        document.getElementById("news_list").innerHTML = list;

    });
    /*
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange= function f(){ show_data(xmlhttp);};
    xmlhttp.open("GET",query,true);
    xmlhttp.send();
    */
}

function initialize() {
    geocoder = new google.maps.Geocoder();
    var mapOptions = {
        center: new google.maps.LatLng(40.397, -74.644),
        zoom: 8,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map_canvas"),mapOptions);
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(40.397, -74.644),
        title:"Hello World!"
    });
    marker.setMap(map);
}