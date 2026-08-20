---
title: Leaves
apple_id: DTS40007647
resource_type: Sample Code
platform: Safari|macOS
topic: null
technology: null
published: '2008-05-08'
source_url: https://developer.apple.com/library/archive/samplecode/Leaves/Listings/WithoutCSSExtensions_Leaves_js.html
archived_at: '2026-07-18T03:13:30.145207Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Leaves](Leaves.md)


[Next](WithoutCSSExtensions-ReadMe.txt.md)[Previous](WithoutCSSExtensions-Leaves.css.md)

# WithoutCSSExtensions/Leaves.js

```
/*
Important:

This is sample code demonstrating API, technology or techniques in development.
Although this sample code has been reviewed for technical accuracy, it is not 
final. Apple is supplying this information to help you plan for the adoption of 
the technologies and programming interfaces described herein. This information 
is subject to change, and software implemented based on this sample code should 
be tested with final operating system software and final documentation. Newer 
versions of this sample code may be provided with future seeds of the API or 
technology. For information about updates to this and other developer 
documentation, view the New & Updated sidebars in subsequent documentation seeds.
*/

/*
File: Leaves.js
Abstract: Defines JavaScript functionality for the Leaves sample.
          Creates all leaves in the sample. Calls the Dropper object
          to animate them. 


Version: 1.0

Disclaimer: IMPORTANT:  This Apple software is supplied to you by
Apple Inc. ("Apple") in consideration of your agreement to the
following terms, and your use, installation, modification or
redistribution of this Apple software constitutes acceptance of these
terms.  If you do not agree with these terms, please do not use,
install, modify or redistribute this Apple software.

In consideration of your agreement to abide by the following terms, and
subject to these terms, Apple grants you a personal, non-exclusive
license, under Apple's copyrights in this original Apple software (the
"Apple Software"), to use, reproduce, modify and redistribute the Apple
Software, with or without modifications, in source and/or binary forms;
provided that if you redistribute the Apple Software in its entirety and
without modifications, you must retain this notice and the following
text and disclaimers in all such redistributions of the Apple Software.
Neither the name, trademarks, service marks or logos of Apple Inc.
may be used to endorse or promote products derived from the Apple
Software without specific prior written permission from Apple.  Except
as expressly stated in this notice, no other rights or licenses, express
or implied, are granted by Apple herein, including but not limited to
any patent rights that may be infringed by your derivative works or by
other works in which the Apple Software may be incorporated.

The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

Copyright (C) 2008 Apple Inc. All Rights Reserved.

*/


/* Define the number of leaves to be used in the animation */
const NUMBER_OF_LEAVES = 30;

/* 
    Called when the "Falling Leaves -- Not Using CSS Animations and Transforms" page 
    is completely loaded.
*/
function init()
{
  /* Get a reference to the element that will contain the leaves */
  var container = document.getElementById('leafContainer');
  /* Fill the empty container with new leaves */
  for (var i = 0; i < NUMBER_OF_LEAVES; i++) 
  {
       CreateALeaf(container);
  }
}


/*
    Receives the lowest and highest values of a range and
    returns a random integer that falls within that range.
*/
function randomInteger(low, high)
{
  return low + Math.floor(Math.random() * (high - low));
}


/*
   Receives the lowest and highest values of a range and
   returns a random float that falls within that range.
*/
function randomFloat(low, high)
{
  return low + Math.random() * (high - low);
}


/*
    Receives a number and returns its CSS pixel value.
*/
function pixelValue(value)
{
  return value + 'px';
}


/*
    Uses an img element to create each leaf of the animation.
*/
function CreateALeaf(container)
{
  /* Start by creating an empty img element */
  var image = document.createElement('img');

  /* Randomly choose a leaf image and assign it to the newly created element */
  image.src = ['images/leaf', randomInteger(1, 5), '.png'].join('');

  /* Figure out the random start and end y-axis positions of the image */
  var startPositionOnYAxis = randomInteger(-300, 0);
  var endPositionOnYAxis = randomInteger(600, 700);

  /* Compute a random duration for the animation */
  var duration = randomFloat(5, 11);

  /* Position the leaf at a random start location within the screen */
  image.style.top = pixelValue(startPositionOnYAxis);
  image.style.left = pixelValue(randomInteger(0, 500));  
  /* Now that the image is set up, add it to the container */
  container.appendChild(image);
  /* Finally, create and start an animation using Dropper */
  new Dropper(image, startPositionOnYAxis, endPositionOnYAxis, duration).start();
}

/* Calls the init function when "Falling Leaves -- Not Using CSS Animations and Transforms" is fully loaded */
window.addEventListener('load', init, false);
```

[Next](WithoutCSSExtensions-ReadMe.txt.md)[Previous](WithoutCSSExtensions-Leaves.css.md)

