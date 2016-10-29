# Project 5:  Taco Bell Finder (Karaoke)

Implement Leaflet Plugin and Mapbox API with Flask to display nearby Taco Bell locations in Eugene

## Leaflet
Leaflet is the leading open-source JavaScript library for mobile-friendly interactive maps. Weighing just about 33 KB of JS, it has all the mapping features most developers ever need.

You can checkout the site at

###http://leafletjs.com/

## Mapbox

Mapbox is the mapping platform for developers. Build maps and applications on our simple and powerful APIs, and use our open source libraries for interactivity and control.

You can checkout the site and get your own API Key for use with Leaflet at:

###https://www.mapbox.com/developers/


## How to Run the Code
Before running the code, the API access token for mapbox must be added to 'karaoke.html'

If you'r using your own access token, you must also add your user ID to the file.


```
	git clone  YourRepositoryURL myTestArea
	cd myTestArea
	bash ./configure
	make test    # All tests should pass
	make service # Then I test from browser on another machine
```
Once running, if you're in Eugene Oregon, allow the application to access your location.
If you are not in Eugene, deny location access and by default it will position you in Eugene.


If you have issues with the service you can stop the service by typing the following:
```
	ps -e | grep gunicorn #Find the PID for gunicorn
	kill -9 pid #where pid is the process id returned by the last command
	make service
```
