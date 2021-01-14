      var map_links = {
        "confirmed": "/maps/confirmed/",
        "deaths": '/maps/deaths/',
        "recovered": '/maps/recovered/',
      }

      var lines_links = {
            "confirmed_lines": "/lines/confirmed/",
            "deaths_lines": '/lines/deaths/',
            "recovered_lines": '/lines/recovered/'
      }
      function switchMap(selectedObject) {
          var selected_option = selectedObject.value;
          showMap(map_links[selected_option]);
        }

        function showMap(map_url) {
          document.getElementById("show_map").src = map_url;
          console.log(map_url)
        }

        function showLines(selectedObject) {
          var selected_option = selectedObject.value;
          showMap(lines_links[selected_option]);
        }

        function showMap(map_url) {
          document.getElementById("show_lines").src = map_url;
          console.log(map_url)
        }