---
title: Leaves
apple_id: DTS40007647
resource_type: Sample Code
platform: Safari|macOS
topic: null
technology: null
published: '2008-05-08'
source_url: https://developer.apple.com/library/archive/samplecode/Leaves/Listings/WithCSSExtensions_ReadMe_txt.html
archived_at: '2026-07-18T03:13:29.888584Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Leaves](Leaves.md)


[Next](WithoutCSSExtensions-Dropper.js.md)[Previous](WithCSSExtensions-Leaves.js.md)

# WithCSSExtensions/ReadMe.txt

```
Overview
"WithCSSExtensions" demonstrates how to use animation and transform extensions to CSS to animate objects in 2D space. It displays a poster with colored leaves falling down in the background. It animates the leaves by repeatedly updating their top and opacity properties. This sample uses CSS transforms and animations to update these properties. 

This sample contains the "index.html," "Leaves.js," and "Leaves.css" files. The "index.html" builds the poster and a placeholder for the leaves, "Leaves.js" creates them on the fly, and "Leaves.css" contains all required information to animate them. 


Creating the Leaves
The following steps describe how to create the leaves:
1. Create a placeholder for the leaves
This sample displays all leaves in a placeholder, "leafContainer." "index.html" creates "leafContainer" using a div element. 

2. Style the placeholder 
"Leaves.css" uses the "leafContainer" and "leafContainer > img" id selectors to style "leafContainer." The first id selector defines its position and dimensions. The second id selector defines the position and dimensions of the leaves (its content).  

3. Fill the placeholder 
"Leaves.js" declares a NUMBER_OF_LEAVES constant, which specifies the number of leaves to be used in an animation. It contains the "createALeaf" and "init" functions that respectively builds a leaf and repeatedly calls "createALeaf" to fill "leafContainer" with leaves. NUMBER_OF_LEAVES is set to 30 in this sample.

"createALeaf" uses the following steps to create a leaf:

a. Create a wrapper div
   Each leaf is contained in a div. This allows us to split off the animations.

b. Create an img element
   Each leaf is built using a img element.

c. Set its URL
This sample uses five different colored images for the leaves.
Randomly pick a leaf image using the "randomInteger" function and assign it to the created img element using its src property.

d. Set its top and left positions
This step provides the start position of a leaf on the screen. It uses "randomInteger" and the style.top and style.left declarations to randomly place a leaf on the screen.

e. Select a spin animation 
"Leaves.css" implements the "fade," "drop," "clockwiseSpin" and   
"counterclockwiseSpinAndFlip" animations. See the Animating the Leaves section    below to learn about them. 
Both "clockwiseSpin" and "counterclockwiseSpinAndFlip" are spin animations. Hence, "createALeaf" uses the Math.random function to determine which of these spin animations  should be applied to a leaf. 

f. Set the animations
Use the style.webkitAnimationName declaration to apply the "fade," "drop,"  
and "clockwiseSpin" or "counterclockwiseSpinAndFlip" animations to a leaf.

g. Select the length of the animation
Use the "randomFloat" function to randomly select values for the duration of  these animations. Create a list made of these values and update each 
leafÕs webkitAnimationDuration property with it using the  
style.webkitAnimationDuration declaration.

h. Append the created image to its wrapper div, return this div, and add it to "leafContainer" in "init" 

Repeat steps a to h until "leafContainer" contains 30 leaves. 


Animating the leaves
This sample implements four individual animations to animate the leaves: "fade," "drop," "clockwiseSpin," and "counterclockwiseSpinAndFlip." The first animation controls the opacity of a leaf and hides or shows it appropriately. The second animation manipulates the top position of a leaf, thus making it fall at given times. Both "clockwiseSpin" and "counterclockwiseSpinAndFlip" rotate the leaves around the y-axis in 2D space, but in opposite directions. "counterclockwiseSpinAndFlip" flips the leaves before spinning them. Use the @-webkit-keyframes rule to declare each of these animations. 

"Leaves.css" uses the -webkit-animation-iteration-count, -webkit-animation-timing-function, and -webkit-animation-duration properties to apply "fade," "drop," and "clockwiseSpin" or "counterclockwiseSpinAndFlip" to each leaf.


Further Reading
Read the following references to learn about all the CSS properties used in this sample:
CSS Animation Proposal
CSS Transforms Proposal
Safari CSS Reference
Safari CSS Animation Guide for iPhone OS
Safari CSS Transform Guide for iPhone OS
Note: You must log into the Web Apps Dev Center to access these references.


Using the Sample
Place this sampleÕs files on your own webserver (eg. Mac OS X Personal Web Server). Open index.html in an iPhone or iPod touch running OS 2.0 or iPhone Simulator with iPhone OS 2.0 (/Developer/Platforms/AspenSimulator.platform/Developer/Applications). You should see colored leaves falling down.


Feedback and Bug Reports
Please send all feedback about this sample by using the Feedback form on the bottom of the sample's webpage. Please submit any bug reports about this sample to the Bug Reporting <http://developer.apple.com/bugreporter> page. 
Copyright (C) 2008 Apple Inc. All Rights Reserved.
```

[Next](WithoutCSSExtensions-Dropper.js.md)[Previous](WithCSSExtensions-Leaves.js.md)

