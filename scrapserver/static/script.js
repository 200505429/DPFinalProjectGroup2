'use strict';

$(document).ready(function () {

  //Pulls the current date
  let NowMoment = moment().format("l");
  
  //adds days to moment for forecast
  let day1 = moment().add(1, "days").format("l");
  let day2 = moment().add(2, "days").format("l");
  let day3 = moment().add(3, "days").format("l");
  let day4 = moment().add(4, "days").format("l");
  let day5 = moment().add(5, "days").format("l");


    
    let queryURL = "http://13.58.69.12:5000/getdata";
    let coords = [];

    $.ajax({
      url: queryURL,
      method: "GET",
    }).then(function (response) {

    
      let cityName = response.name;
      let cityCond = response.weather;
      let cityTemp = response.temp;
      let cityHum = response.humidity;
      let cityWind = response.wind;
      let icon = response.condition;
     // $("#icon").html(
     //   `<img src="http://openweathermap.org/img/wn/${icon}@2x.png">`
     // );
      $("#city-name").html(cityName + " " + "(" + NowMoment + ")");
      $("#city-cond").text("Current Conditions: " + cityCond);
      $("#temp").text("Current Temp (F): " + cityTemp);
      $("#humidity").text("Humidity: " + cityHum + "%");
      $("#wind-speed").text("Wind Speed: " + cityWind + "mph");
      $("#date1").text(day1);
      $("#date2").text(day2);
      $("#date3").text(day3);
      $("#date4").text(day4);
      $("#date5").text(day5);

    }).fail(function (){
     
    });

    //Function to get 5-day forecast and UV index and put them on page
  
});



//End of line
