document.addEventListener("DOMContentLoaded", function () {
  const error = document.getElementById("not-found");
  const weatherBoxElement = document.getElementById("weather-box");
  const weatherDetailsElement = document.getElementById("weather-details");
  const containerElement = document.querySelector(".container");

  // const descriptionText = json_data["weather"][0]["description"]; // Get the weather description from Django context
  const descriptionText = "{{data.description | escapejs}}";
  console.log(descriptionText);
  const weatherImage = document.querySelector(".weather-box weather img");

  const weatherImages = {
    "clear sky": "{% static 'images/mist.png' %}",
    "few clouds": "{% static 'images/clouds2.png' %}",
    "scattered clouds": "{% static 'images/clouds.png' %}",
    "broken clouds": "{% static 'images/clouds.png' %}",
    "shower rain": "{% static 'images/rain.png' %}",
    rain: "{% static 'images/rain.png' %}",
    thunderstorm: "{% static 'images/rain.png' %}",
    snow: "{% static 'images/snow.png' %}",
    mist: "{% static 'images/mist.png' %}",
  };

  if (descriptionText && weatherImage) {
    const imageUrl =
      weatherImages[descriptionText.toLowerCase()] ||
      "{% static 'images/clouds2.png' %}";
    weatherImage.src = imageUrl;
  }

  if (error) {
    error.classList.add("active");
    if (weatherBoxElement) weatherBoxElement.classList.remove("active");
    if (weatherDetailsElement) weatherDetailsElement.classList.remove("active");
    containerElement.style.height = "50vh"; // Adjust container height for error state
  } else {
    if (weatherBoxElement) weatherBoxElement.classList.add("active");
    if (weatherDetailsElement) weatherDetailsElement.classList.add("active");
    containerElement.style.height = "85vh"; // Adjust container height for success state
  }

  const date = new Date();
  const today = new Intl.DateTimeFormat("en-US", {
    dateStyle: "full",
    timeStyle: "long",
  }).format(date);
});
