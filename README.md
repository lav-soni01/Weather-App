## bWeather App

## introduction

A simple python command-line application that fetches real time weather of different cities by using weather API .

The main focus of this project is learning API implementation .

## Features 

- Search weather by city name
- shows :
  
  region
  contry
  temperature
  wind speed (in kmph & mph)
  chance of rain
  wind direction
  pressure
  humidity
  last updated time
  current time of that city

  These are not the only things we can ask from the API , but for now the code only shows these things , but we can add more features when we want or need .


## Built with

- Python 3
- Requests Library
- Weather API

## Installation

1. clone the repository

```bash
git clone https://github.com/lav-soni01/Weather-App.git
```

2. Install the required package

```bash
pip install requests
```

3. Open `main.py`

4. Replace:

   ```python
   "<Your Key>"
   ```
   With your own API key

5. Run the program

  ```bash
  python main.py
  ```

## Example Output 

```text

Enter the ciy name: London

city: London
Region: city of london
Country: united Kingdom
Temperature: 23°C
humidity: 56
Wind Speed: 18 kmh
Wind Speed(in mph): x mph
local time: 2026-07-17 12:45
...
```
For accuret results check the ScreenShot attached with the file.

## What I Learned 

- Making API requests using the 'requests' library
- working with JSON responses
- using query parameters('params')
- Handling API data in python
- Basic Git and Github workflow

## License

This project is for learning and eductional purposes.

  

