# Kojima Turn Demonstration

## Introduction
This python project is a direct implementation of the sreadsheet produced by Kojima-san on his micromouse blog in a 
series of posts about wall-tracking control.

The original posts are here:
- https://kojimousenote.blogspot.com/2011/12/blog-post_04.html
- https://kojimousenote.blogspot.com/2011/12/y.html
- https://kojimousenote.blogspot.com/2011/12/blog-post_8223.html
- https://kojimousenote.blogspot.com/2011/12/blog-post_11.html

The spreadsheet is linked to in the last of those posts as : http://www.kikaiken.org/lib/micromouse/111211/PDs_sim.xls

(note that the file may not download from within the page - try the direct link)

## Summary
The controller described in the blog posts attempts to reduce the lateral and angular error of the mouse to zero as 
measured by the sensors. Lateral error is a value in the y-axis of the mouse reference frame. The angular error is 
denoted by theta. The controller output 
is an angular acceleration that is applied to the rotation controller 
of the mouse. While the sensors are not able to directly measure the values of y and theta they may be inferred from 
the changing value of the sensor reading as the robot moves forward. Although not done in the blog posts, the 
angle may also be determined from the gyro if one is present.

## Implementation
The calculations in the original spreadsheet are copied exactly except that the python script uses mm and degrees 
where appropriate rather than the original metres and radians. After some experimentation the initial conditions in 
the script are different to those shown in the spreadsheet. There are four key constants in the controller that have 
apparently arbitrary values. You will find that changing these may cause the controller to 'blow up' in the sense 
that the output will cause the mouse to go out of control.

Two of these constants, K1 and K2, are supposed to be measured form the mouse though I do not know how that should be 
done or quite what they represent.

The other two Kp and Kd are the more familiar proportional and derivative constants for a PD controller.

Honestly, I do not fully understand the derivation Kojima-san uses (yet).

## Operation
You will be able to freely change the values in any of the spin boxes to the right of the application window and the 
plots will immediately update.

If everything goes weird, press the `reset` button to put everything back to the original settings at launch.

The charts are scrollable and zoomable with hte x-axes being linked. Drag your mouse around and use the scroll wheel 
to see their effect. Hover the mouse pointer in the lower left of any charts and a small button marked with an `A` 
will appear. that will autoscale that chart. Right-clicking a chart produces other options that you will have to 
discover for yourself.

## Observations
Without knowing how to determine values for K1 and K1 and what their physical reality is for the mouse it is hard to 
know how effective this controller really is on a real mouse. However Kojima-san says that he has used this basic 
scheme for many years with great success and that newcomers at the mouse training day were successful in making an 
implementation.

To my mind the controller does not necessarily address one of the common issues seen which is that the behaviour 
depends upon speed. In one of the posts it is hinted that it may not perform well enough at higher speeds. Overall 
it would be better to have a tracking controller that lets you determine the constants in terms of settling distance.
This is possible with the Kanayama tracker although this controller seems to be a close cousin.

### Notes 

- The simulation provides an upper limit on the available angular acceleration and you should match 
this to 
the capabilities of your mouse.
- The controller cycle time is hard coded at 0.001 seconds per cycle
- the implementation uses Python 3.10, Numpy, PyqtGraph and PyQt5
- See the `requirements.txt` file for any Python modules you will need.