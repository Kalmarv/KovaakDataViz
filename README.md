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
* Run python3 plotlyviz.py

This will start a local server at http://127.0.0.1:8050/ that will display the graphs.
