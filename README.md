# KovaakDataViz

Python scipts to load your saved Kovaak's log files and output nice graphs.

![Graph 1](https://i.imgur.com/t5ync1h.png)

![Graph 2](https://i.imgur.com/9SX0wWI.png)

![Graph 2](https://i.imgur.com/ewCZ7Ku.png)

## Usage

Not yet optomized for general release so you'll have to setup a few things to use.

* Change the path variable in main.py to the location of your Kovaak's stats folder
  * Note that it uses /mnt because I'm running it from WSL, this will be updated in the future
* pip3 install all the dependants
  * pandas
  * dash
  * plotly
  * numpy

From Windows Subsystem for Linux:

* Run python3 main.py
  * This processes the Kovaaks's log files into nice pandas data frames
* Run python3 plotlyviz.py
  * This creates the server running at http://127.0.0.1:8050/ and creates the graphs

## Other Notes

* I'm pretty new to programming, and this is my first attempt at a real project, I'm sure there are a ton of issues with the code but I'm still learning
* I don't have any of the old Kovaak's log files, so it won't work with those
* It does not edit your files in the Kovaak's save folder, simply reads the data, and copies it to one master csv in the folder of the python scripts
* I'm open to suggestions, but no guarantees
* There is a chance it will not run for you as Kovaak's logs scenarios different for no discernible reason, and I have to deal with these as I find them. I will probably refactor the code to try and remedy this
