---
title: PosterCircle
apple_id: DTS40007648
resource_type: Sample Code
platform: Safari|iOS
topic: null
technology: null
published: '2008-06-19'
source_url: https://developer.apple.com/library/archive/samplecode/PosterCircle/Listings/PosterCircle_js.html
archived_at: '2026-07-18T03:19:29.731374Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PosterCircle](PosterCircle.md)


[Next](Document%20Revision%20History.md)[Previous](PosterCircle.css.md)

# PosterCircle.js

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
File: PosterCircle.js
Abstract: Defines JavaScript functionality for the PosterCircle sample.
          Implements each ring of the cylinder. Creates and appends 12 posters
          to each ring. Adds numbers to each poster. Translates and rotates 
          each of them.

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

/* Each ring of the cylinder contains 12 posters */
const POSTERS_PER_RING = 12;

/*
   Implements each ring of the cylinder that. Applies translation
   and rotation transformations to each poster.  
*/
function setup_posters(ring)
{
    /* We create a ring by creating and dividing a 360 degrees circle into 12 equal parts
       that each contains a poster */
    /* posterAngle has a value of 30 degrees */   
    var posterAngle = 360 / POSTERS_PER_RING;
    for (var index = 0; index < POSTERS_PER_RING; index ++) 
    {
        /* Each poster is a div element */
        var poster = document.createElement('div');

        /* Applies the CSS "poster" class to the poster */
        poster.className = 'poster';

        /* Compute and assign a transform to the poster */
        var transform = ['rotate3d(0,1,0,', (posterAngle * index), 'deg) translateZ(200px)'].join('');
        poster.style.webkitTransform = transform;

        /* Create a placeholder for the number on each number */
        var content = poster.appendChild(document.createElement('p'));

        /* Add a number to the poster */
        content.textContent = index;
        /* Add the poster to this ring */
        ring.appendChild(poster);
    }
}


/*
    Called when the "Poster Circle" page loads. Calls the setup_posters
    function to implement all three rings of the cylinder.
*/
function init()
{
    setup_posters(document.getElementById('ring-1'));
    setup_posters(document.getElementById('ring-2'));
    setup_posters(document.getElementById('ring-3'));
}

/* Call the init function when the "Poster Circle" page is fully loaded */
window.addEventListener('load', init, false);
```

[Next](Document%20Revision%20History.md)[Previous](PosterCircle.css.md)

