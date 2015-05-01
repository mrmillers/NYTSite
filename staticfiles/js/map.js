var map;
var geocoder;
function show_data(xmlhttp){
    if (xmlhttp.readyState==4 && xmlhttp.status==200){
    //document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
        alert(xmlhttp.responseText);
    }
}
function search(){
    var location = document.getElementById("location").value;
    var people = document.getElementById("people").value;
    var key = document.getElementById("key").value;
    var start_time = document.getElementById("time_start").value;
    var end_time = document.getElementById("time_end").value;

    var query = "/query?key=" + key + "&location=" + location + "&people=" + people + "&start_time=" + start_time + "&end_time=" + end_time;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange= function f(){ show_data(xmlhttp);};
    xmlhttp.open("GET",query,true);
    xmlhttp.send();
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