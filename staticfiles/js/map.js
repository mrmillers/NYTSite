var map;
var lat = []
var markers = []
function showList(rank, showGeo){
    var list = "<ol>";
    $.each(rank,function (key,value){
            if (showGeo < 0 || value["geoIndex"] == showGeo){
                list += "<li><p><a target=\"_blank\" href=\"/article/" + value["nid"] +  "\">" + value["title"] +"</a></p><p>";
                if (value["author"]!="") list+= "Author:" + value["author"];
                if (value["location"]!="") list+= "Location:" + value["location"];
                if (value["date"]!="") list+= "Date:" + value["date"];
                list += "</p></li>";
            }
    });
    list += "</ol>"
    document.getElementById("news_list").innerHTML = list;
}
function search(){
    document.getElementById("news_list").innerHTML = "Searching...";
    var location = document.getElementById("location").value;
    var people = document.getElementById("people").value;
    var key = document.getElementById("key").value;
    var start_time = document.getElementById("time_start").value;
    var end_time = document.getElementById("time_end").value;

    var query = "/query?key=" + key + "&location=" + location + "&people=" + people + "&start_time=" + start_time + "&end_time=" + end_time;
    $.getJSON(query,function (data){
        rank=data["rank"]
        geo=data["geo"]
        showList(rank, -1)
        lat = []
        bad = 0
        $.each(markers,function(key,value){ value.setMap(null)});
        markers = []
        var markerBounds = new google.maps.LatLngBounds();
        $.each(geo,function(key,value) {
            var geocoder = new google.maps.Geocoder();
            geocoder.geocode( { 'address': value["location"]}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    lat.push(results[0].geometry.location)
                    var marker = new google.maps.Marker({
                        map: map,
                        position: results[0].geometry.location
                    });
                     google.maps.event.addListener(marker, 'click', function() {
                        map.panTo(marker.getPosition());
                        showList(rank, key);
                      });
                      markerBounds.extend(marker.position);
                    markers.push(marker);
                }
                else{ bad += 1;}
                if (lat.length + bad >= geo.length){
                    //alert(lat)
                    map.fitBounds(markerBounds);
                    // map.setCenter(markerBounds.getCenter(),map.getBoundsZoomLevel(markerBounds));
                }
                //alert(lat.length + " " + bad + " " + geo.length)
            });
        });
    });
    /*
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange= function f(){ show_data(xmlhttp);};
    xmlhttp.open("GET",query,true);
    xmlhttp.send();
    */
}

function initialize() {
    var mapOptions = {
        center: new google.maps.LatLng(40.397, -74.644),
        zoom: 8,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map_canvas"),mapOptions);
    /*var marker = new google.maps.Marker({
        position: new google.maps.LatLng(40.397, -74.644),
        title:"Hello World!"
    });
    marker.setMap(map);*/
}