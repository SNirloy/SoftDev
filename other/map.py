import requests
import json

def map_api(location):
    start = "https://www.openstreetmap.org/#map=18"
    for coor in location:
        start += "/"
        start += coor
    


<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=-118.36705863475801%2C33.96750144744307%2C-118.36497992277147%2C33.96950125161611&amp;layer=mapnik" style="border: 1px solid black"></iframe><br/><small><a href="https://www.openstreetmap.org/#map=19/33.96850/-118.36602">View Larger Map</a></small>
<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=-118.47804576158525%2C73.92214423714418%2C-118.47596704959871%2C73.9228120186592&amp;layer=mapnik" style="border: 1px solid black"></iframe><br/><small><a href="https://www.openstreetmap.org/#map=19/73.92248/-118.47701">View Larger Map</a></small>
<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=-8.478049635887148%2C73.92214646560348%2C-8.475970923900606%2C73.9228142470284&amp;layer=mapnik" style="border: 1px solid black"></iframe><br/><small><a href="https://www.openstreetmap.org/#map=19/73.92248/-8.47701">View Larger Map</a></small>

print(-118.36705863475801 - (-118.36497992277147))
print(- 8.478049635887148 - ())