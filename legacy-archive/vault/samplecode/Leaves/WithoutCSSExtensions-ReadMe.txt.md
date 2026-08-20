---
title: Leaves
apple_id: DTS40007647
resource_type: Sample Code
platform: Safari|macOS
topic: null
technology: null
published: '2008-05-08'
source_url: https://developer.apple.com/library/archive/samplecode/Leaves/Listings/WithoutCSSExtensions_ReadMe_txt.html
archived_at: '2026-07-18T03:13:30.226672Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Leaves](Leaves.md)


[Next](Document%20Revision%20History.md)[Previous](WithoutCSSExtensions-Leaves.js.md)

# WithoutCSSExtensions/ReadMe.txt

```
Overview
"WithoutCSSExtensions" uses JavaScript techniques to create and animate objects in 2D space. It displays a poster with colored leaves falling down in the background. It animates  the leaves by repeatedly updating their top and opacity properties. This sample uses "Dropper" a custom JavaScript object and the setTimeout function to update these properties. 

This sample contains the "index.html," "Leaves.js," "Dropper.js," and "Leaves.css" files. The "index.html" builds the poster and a placeholder for the leaves, "Leaves.js" creates them on the fly, "Dropper.js" animates them, and "Leaves.css" defines their appearance. 


Creating the Leaves
The following steps describe how to create the leaves:

1. Create a placeholder for the leaves
This sample displays all leaves in a placeholder, "leafContainer." 
"index.html" creates "leafContainer" using a div element. 

2. Style the placeholder 
"Leaves.css" uses the "leafContainer" and "leafContainer > img" id selectors to style "leafContainer." The first id selector defines its position and dimensions. The second id selector defines the position and dimensions of the leaves (its content).  

3. Fill the placeholder 
"Leaves.js" defines a NUMBER_OF_LEAVES constant, which specifies the number of leaves to be used in an animation. It contains the "createALeaf" and "init" functions that respectively builds a leaf and repeatedly calls "createALeaf" to fill "leafContainer" with leaves. NUMBER_OF_LEAVES is set to 30 in this sample.

"createALeaf" uses the following steps to create a leaf:

a. Create an img element
Each leaf is built using a img element.

b. Set its URL 
This sample uses five different colored images for the leaves.
Randomly pick a leaf image using the "randomInteger" function and assign it to the created img element using its src property.

c. Set the start and end positions of its animation
This step consists of getting the positions at which the animation will start and end. Randomly choose values for these positions and store them in the "startPositionOnYAxis" and "endPositionOnYAxis" variables. 

d. Select the length of the animation
Use the "randomFloat" function to randomly select a value for the duration of the animation and store it in the "duration" variable.

e. Set its top and left positions
This step provides the start position of a leaf on the screen. It uses "randomInteger" and the style.left declaration to randomly left align a leaf on the screen. It sets the leaf’s top property to the above "startPositionOnYAxis" using the style.top declaration. 

f. Appends the created image to "leafContainer" 

g. Create an instance of "Dropper" 
This sample uses the "Dropper" object to animate the leaves. Use the new  
operator to create an instance of "Dropper." Fill the "Dropper" constructor 
with a reference to the newly created leaf, "startPositionOnYAxis" and  "endPositionOnYAxis," and "duration."

h. Start the animation
Call the "start" function of "Dropper" to animate this leaf.  

Repeat steps a to h until "leafContainer" contains 30 leaves. 


Animating the leaves
This sample uses a custom JavaScript object "Dropper" to animate each leaf.
"Dropper" takes four arguments as described in step g: element (reference to a leaf), "startPositionOnYAxis" and  "endPositionOnYAxis," and "duration." It declares the "startTime" and "endTime" variables and implements the "setTopAttribute," "setOpacity," "loop," and "start" functions.

"startTime" and "endTime" respectively keep track of the times at which an animation will start and end. 

The "setTopAttribute" and "setOpacity" functions are respectively used to update the top and opacity properties of a leaf. 

"loop" animates the leaves by repeatedly calling the "setTopAttribute" and "setOpacity" functions. This is achieved by using the setTimeout function that calls "loop" every 10 milliseconds. "loop" checks the elapsed time for the current animation of a leaf, moves this leaf to its final position and restarts the animation if this time is equal to or greater than the current time. It updates the top and opacity properties of the leaf if this time is less than the current time. 

"start" sets "startTime" and "endTime" and calls "loop" to animate the leaves.


Further Reading
Read the following references to learn about all the CSS properties used in this sample:
Safari CSS Reference
Note: You must log into the Web Apps Dev Center to access these references.


Using the Sample
Place this sample’s files on your own webserver (eg. Mac OS X Personal Web Server). Open index.html in an iPhone or iPod touch running OS 2.0 or iPhone Simulator with iPhone OS 2.0 (/Developer/Platforms/AspenSimulator.platform/Developer/Applications). You should see colored leaves falling down.


Feedback and Bug Reports
Please send all feedback about this sample by using the Feedback form on the bottom of the sample's webpage. Please submit any bug reports about this sample to the Bug Reporting <http://developer.apple.com/bugreporter> page. 
Copyright (C) 2008 Apple Inc. All Rights Reserved.
```

[Next](Document%20Revision%20History.md)[Previous](WithoutCSSExtensions-Leaves.js.md)

