---
title: Leaves
apple_id: DTS40007647
resource_type: Sample Code
platform: Safari|macOS
topic: null
technology: null
published: '2008-05-08'
source_url: https://developer.apple.com/library/archive/samplecode/Leaves/Listings/WithoutCSSExtensions_Dropper_js.html
archived_at: '2026-07-18T03:13:29.999214Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Leaves](Leaves.md)


[Next](WithoutCSSExtensions-index.html.md)[Previous](WithCSSExtensions-ReadMe.txt.md)

# WithoutCSSExtensions/Dropper.js

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
File: Dropper.js
Abstract: Defines JavaScript functionality for the Leaves sample.
          Creates a JavaScript object that contains all required 
          information to animate the leaves.


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

/*
    Creates a JavaScript object that implements fade and drop animations on the y-axis.
    Takes four parameters: element, startPosition, endPosition, and duration. 
    The element parameter refers to the html element to be animated, startPosition
    and endPosition respectively determine where to start and end the animations on the the y-axis,
    and duration specifies the length of the animation.
*/
function Dropper(element, startPosition, endPosition, duration)
{
    /* Track all parameters of the Dropper instance object */
    this.element = element;
    this.startPositionOnYAxis = startPosition;
    this.endPositionOnYAxis = endPosition;
    this.duration = duration;
    /* timeout will be used to start and stop the animation */
    this.timeout = null;
};


/*
    Updates both startTime and endTime variables that respectively specify the times at 
    which the animations will start and end. Calls the loop function to start the animations.
*/
Dropper.prototype.start = function ()
{
    /* Do nothing if the values of startPositionOnYAxis and endPositionOnYAxis are identical */
    if (this.startPositionOnYAxis == this.endPositionOnYAxis) 
    {
        return;
    }
    /* Track the animation time, get its starting time here */
    this.startTime = new Date();
    /* Get the current duration in milliseconds, add it to the above starting time, and assign it to the endTime variable */
    this.endTime = this.startTime.getTime() + (this.duration * 1000);
    /* Calls the loop function to start the animation */
    this.loop();
};


/* 
    Performs the animations. Check the elapsed time for the current animation.
    Moves the element to its final position, stops the current animation,
    and restarts the animation process if that time is equal to or greater than
    the current time. 
    Updates the top and opacity properties of the elements if we are still within
    the allocated time for the animation. 
*/
Dropper.prototype.loop = function ()
{
    /* Get the current time */
    var now = new Date();

    /* Check whether we have reached or gone past the end time */
    if (now >= this.endTime) 
    {
        /* If so, set the final position */
        this.setTopAttribute(this.endPositionOnYAxis);

        /* Clear current animation */
        window.clearTimeout(this.timeout);

        /* Restart the animation */
        this.start();
        return;
    }
    /* Otherwise, figure out how far along we are within the animation */
    var offset = (now - this.startTime) / (this.duration * 1000);

    /* Compute and set the current height based on offset */
    this.setTopAttribute(this.startPositionOnYAxis + (offset * (this.endPositionOnYAxis - this.startPositionOnYAxis)));

    /*And if we are real close to the end of the animation, update the opacity for a gradual fade out */
    this.setOpacity( (offset > 0.95) ? 1.0 - (offset - 0.95) * 20.0 : 1.0 );

    /* Finally, call the loop function again in 10 ms */
    var _this = this;
    this.timeout = window.setTimeout(function () { _this.loop() }, 10);
};


/*
    Updates the top position of an element.  
*/
Dropper.prototype.setTopAttribute = function (newTopPosition)
{
    this.element.style.top = pixelValue(newTopPosition);
};


/*
    Updates an element's opacity.
*/
Dropper.prototype.setOpacity = function (newOpacity)
{
    this.element.style.opacity = newOpacity;
};
```

[Next](WithoutCSSExtensions-index.html.md)[Previous](WithCSSExtensions-ReadMe.txt.md)

