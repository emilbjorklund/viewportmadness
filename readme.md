# Viewport madness
## Well, this is just silly.

This is just a small python script to read the CSV data exported from a constantly growing list of devices and their viewport dimensions (found at http://bit.ly/TbbXRy), and creating a CSS file with @media-queries for them expressed as min width, with the platform and OS versions as comments.

I made it over lunch, inspired by http://opensignalmaps.com/reports/fragmentation.php and Tom Armitage's talk at dConstruct 2012 about the value of playing with things and putting stuff out there despite it not really having any apparent meaning yet, apart from being silly.

So, to conclude: shitload of viewport width media queries with comments, lunch break, python file (2.6 and up, I believe), run it and it regenerates the css, silly stuff, do not generally base your media queries on devices because it gets ridiculous, right?.