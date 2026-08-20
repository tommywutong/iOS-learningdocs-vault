---
title: PosterCircle
apple_id: DTS40007648
resource_type: Sample Code
platform: Safari|iOS
topic: null
technology: null
published: '2008-06-19'
source_url: https://developer.apple.com/library/archive/samplecode/PosterCircle/Listings/PosterCircle_css.html
archived_at: '2026-07-18T03:19:29.649302Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PosterCircle](PosterCircle.md)


[Next](PosterCircle.js.md)[Previous](index.html.md)

# PosterCircle.css

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
File: PosterCircle.css
Abstract: Defines CSS properties for the PosterCircle sample.
          Defines and styles each ring of the cylinder. Applies
          CSS transform and animation properties to these rings.
          Styles and controls the posters on each ring.



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


body 
{
    margin: 0px;
    background-color: rgba(142,53,87, 0.5);
}

/*
    We use three individual animations (x-spin, y-spin, back-y-spin) to create
    the cylinder's 3D rotation effect. The x-spin animation will perform a
    full rotation on the x-axis, we'll use that on the whole set of objects. 
    The y-spin and back-y-spin animations will perform a full rotation on 
    the y-axis in opposite directions, alternating directions between rings.
    We define each of these animations using the "@-webkit-keyframes" rule. 

    Note that since animations will take the shortest path between values
    and a rotation of 0 degrees is the same orientation as 360 degrees, it
    is necessary to specify an intermediate keyframe step that is half way
    around a full rotation. This way the animation will rotate to 180 degrees
    half way through the animation and then continue on to 360 degrees. */
@-webkit-keyframes x-spin 
{
    /* Rotate the cylinder by 0 degrees around the x-axis at the start of the animation */
    0%    { -webkit-transform: rotateX(0deg); }
    /* Rotate the cylinder by 180 degrees around the x-axis at 50% into the animation */
    50%   { -webkit-transform: rotateX(180deg); }
    /* Rotate the cylinder by 180 degrees around the x-axis when the animation is ending */
    100%  { -webkit-transform: rotateX(360deg); }
}


/* Performs rotations around the y-axis in the counterclockwise direction */
@-webkit-keyframes y-spin
{
    /* Rotate this ring of the cylinder by 0 degrees around the y-axis at the start of the animation */
    0%    { -webkit-transform: rotateY(0deg); }
    /* Rotate this ring by 180 degrees around the y-axis at 50% into the animation */
    50%   { -webkit-transform: rotateY(180deg); }
    /* Rotate this ring by 360 degrees around the y-axis when the animation is ending */
    100%  { -webkit-transform: rotateY(360deg); }
}


/* Performs rotations around the y-axis in the clockwise direction */
@-webkit-keyframes back-y-spin 
{
    /* Rotate this ring by 360 degrees around the y-axis at the start of the animation */
    0%    { -webkit-transform: rotateY(360deg); }
    /* Rotate this ring by 180 degrees around the y-axis at 50% into the animation */
    50%   { -webkit-transform: rotateY(180deg); }
    /* Rotate this ring of the cylinder by 0 degrees around the y-axis when the animation is ending */
    100%  { -webkit-transform: rotateY(0deg); }
}


/* Placeholder for the cylinder. Renders the cylinder in 3D space. */
#stage
{
    position: absolute;
    left: -40px;
    top: 95px;
    width: 600px;
    height: 400px;
    /* Ensure that the contents of the stage remain in 3D space, without being flattened */
    -webkit-transform-style: preserve-3d;
    /* Give some depth to the cylinder */
    -webkit-perspective: 2000;
}


/* Placeholder for the three rings of the cylinder. Makes all three rings appear like a cylinder.
   Rotates all three rings around the x-axis. */
#rotate 
{
    position: absolute;
    width: 600px;
    height: 400px;
    /* Ensure that we're in 3D space */
    -webkit-transform-style: preserve-3d;
    /* let's rotate all three rings along the x-axis over a period of 7 seconds */
    -webkit-animation-name: x-spin;
    -webkit-animation-duration: 7s;
    /* Let the rings rotate forever and linearly */
    -webkit-animation-iteration-count: infinite;
    -webkit-animation-timing-function: linear;
}


/* Styles each ring of the cylinder. Controls the position of each ring's posters in 3D space. */
.ring
{
    position: relative;
    height: 110px;
    width: 600px;
    margin: 20px 0px;
    /* Ensure that posters in each ring maintain their position in 3D */
    -webkit-transform-style: preserve-3d;
}


/* Styles all posters in the cylinder. Provides each poster with a round layout. */
.poster 
{
    position: absolute;
    left: 250px;
    width: 100px;
    height: 100px;
    /* Make each poster transparent */
    opacity: 0.7;
    color: rgba(0,0,0,0.9);
    background-color: rgb(142,53,87);
    /* Give a round layout to each poster */
    -webkit-border-radius: 10px;
}


/* Styles the number in each poster */
.poster > p 
{
    font-family: 'Georgia';
    font-size: 36px;
    text-align: center;
    margin-top: 28px;
    font-weight: bold;
}


/* Set up each row to have a different animation duration and alternating y-axis rotation direction */
/* This ring will continually rotate around the y-axis and in the counterclockwise direction over a period of 5 seconds */
#ring-1 
{
    -webkit-animation-name: y-spin;
    -webkit-animation-duration: 5s;
    -webkit-animation-iteration-count: infinite;
    -webkit-animation-timing-function: linear;
}


/* This ring will continually rotate around the y-axis and in the clockwise direction over a period of 4 seconds */
#ring-2 
{
    -webkit-animation-name: back-y-spin;
    -webkit-animation-duration: 4s;
    -webkit-animation-iteration-count: infinite;
    -webkit-animation-timing-function: linear;
}


/* This ring will continually rotate around the y-axis and in the counterclockwise direction over a period of 3 seconds */
#ring-3 
{
    -webkit-animation-name: y-spin;
    -webkit-animation-duration: 3s;
    -webkit-animation-iteration-count: infinite;
    -webkit-animation-timing-function: linear;
}
```

[Next](PosterCircle.js.md)[Previous](index.html.md)

