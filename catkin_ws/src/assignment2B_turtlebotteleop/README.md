# Circle.py

## Analysis
Our thinking for the open-loop circle test would be to try to create the same radius circle for each run. Slow and medium runs should go as expected and we would crank the speed for fast until some unexpected behavior occured. To set the same radius for each run we used the equation:

v = rw --> r = v_x / w_z

Basically, we had to choose a v_x and w_z that would create a circle that fit in our space. Then increase v_x and w_z by the same factor to maintain our radius.

We started by setting v_x and w_z to 1. This made a circle, as expected. We then multiplied both by v_x and w_z by 2 and got a way smaller circle. We knew something was wrong. We didn't know what units the turtlebot was interpretting when we told it v_x = 1 so we decided to run a straight line calibration test. 

We setup a 2m straight line, commanded the turtlebot to move at a certain v_x (w_z = 0) and timed how long it took to travel it. Assuming constant velocity, we could derive the actual velocity using this equation:

v = d/t where d = 2m and t = our timed result.

These were our results:

![](images/linearVel_linearANDsaturation.png)

We began by setting our v_x to 1 and w_z to 1.

 should show image below
 <!-- Need this space so image and text won't be on same line -->


### Figures



# Square.py

## Analysis

### Figures
