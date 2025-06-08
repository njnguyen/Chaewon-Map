# Chaewon-Map
GPS map that creates a "Chaewon" shaped route

Do YOU love Chaewon so much that you would follow her to the ends of the Earth and anywhere you go? Chaewon Follower is an app for only the most HARDCORE Chaewon stans that allows you to do just that! (literally). An add-on to the ever-popular GPS map system, Chaewon Follower will enable you to grace your journeys with Her name.

How-to:
* input destination and origin as you would a regular GPS (super user friendly! no additional learning curve required!)
* follow the dynamically™ generated path that takes you to your destination via the most CHAEWON path


How does it work?
* User input for origin/destination is taken
* Local map is pulled using OpenStreetMap API
* Street pattern is processed as an image using the scikit-image package and converted into a numpy array (WIP)
* Chaewon letter pattern is feature-matched onto processed map image to find the most CONVENIENT Chaewon-shaped path (WIP)
* Coordinates of Chaewon lettering is converted back from numpy array into longitude/latitude coordinates (WIP)
* Coordinates are then passed back to OpenStreetMap to create a route to display to the end-user (WIP)
