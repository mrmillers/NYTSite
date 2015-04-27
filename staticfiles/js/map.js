function initialize() {
        var mapOptions = {
          center: new google.maps.LatLng(40.397, -74.644),
          zoom: 8,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("map_canvas"),
            mapOptions);
      }