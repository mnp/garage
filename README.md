# Garage Door Controller

I wanted a quick way to see the state of my garage doors and actuate their
opener to change it. Perhaps I'm at work and want to let a contractor in,
or perhaps I'm in bed and want to make sure the kids remembered to closed
the doors.  I wanted to use various devices, such as my family's phones and
PCs.

Hopefully someone will find this useful.

# The Hardware 
* a Raspberry PI -- any will do, running Raspian.  If you want a different OS you might rewrite the init and log rotator.
* a relay board -- I chose a 4 channel board to raise 2 doors via the door opener's pushbutton circuits, plus keep 2 channels for expansion to other things later, like lights or outlets.
* magnetic door sensors to detect the garage door's positions
* a terminal strip to attach all the external wires
* a scrap of plywood to mount everything on

![assembled board photo](https://raw.githubusercontent.com/mnp/garage/master/assembled-board.jpg)

# The Software

**In progress**

* Written in Python, it is built around the RPi library and a Bottle webserver, which serves webpages for the UI.
* The webpage contains a little JS, Bootstrap, and HTML to show current state and actuate buttons for each door.
* There's also Raspian init.d and logrotate configs.

![This is what the very simple UI looks like.](https://raw.githubusercontent.com/mnp/garage/master/ui.png)

TODO
 - I'm currently using the RPi switch debouncer, which is needed for the magnetic sensors.  The UI however needs to reflect door moving states.
