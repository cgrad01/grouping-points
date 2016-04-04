# grouping-points

This is a submission I made to coding challenge for a developer position.

The prompt asked me to take a user specified json file of random points (each of which had a lat, long, and id), and output a json file containing a user specified number of groups, in which would be points, clustered by proximity to one another.

In order to run this program:

  1. Clone the repository to your desktop.
  2. In your terminal, navigate into the folder titled "grouping-points"
  3. Enter the command "python runner.py"
  4. Follow the instructions (default input file is titled 'points.json')
  5. See your results in the file title "groups.json"

If you would like to input a different file, simply copy the file into the grouping-points folder, and use the name of that file when prompted.

*PLEASE NOTE - The only external library used is an implementation of the Haversine formula, used to convert from lat/lon degrees to kilometers. To install, simply run the command "pip install haversine" prior to instructions above. View the Haversine Gist [here](https://gist.github.com/rochacbruno/2883505)

Thanks!