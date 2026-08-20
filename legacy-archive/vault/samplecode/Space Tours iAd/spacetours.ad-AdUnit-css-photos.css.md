---
title: Space Tours iAd
apple_id: DTS40010222
resource_type: Sample Code
platform: iAd Producer|iOS
topic: User Experience
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/samplecode/SpaceTours/Listings/spacetours_ad_AdUnit_css_photos_css.html
archived_at: '2026-07-18T03:25:14.414766Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Space Tours iAd](Space%20Tours%20iAd.md)


[Next](spacetours.ad-AdUnit-css-pricelist.css.md)[Previous](spacetours.ad-AdUnit-css-menu.css.md)

# spacetours.ad/AdUnit/css/photos.css

```
/*
    File: photos.css
Abstract: The photos CSS file.
 Version: 1.3

Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
Inc. ("Apple") in consideration of your agreement to the following
terms, and your use, installation, modification or redistribution of
this Apple software constitutes acceptance of these terms.  If you do
not agree with these terms, please do not use, install, modify or
redistribute this Apple software.

In consideration of your agreement to abide by the following terms, and
subject to these terms, Apple grants you a personal, non-exclusive
license, under Apple's copyrights in this original Apple software (the
"Apple Software"), to use, reproduce, modify and redistribute the Apple
Software, with or without modifications, in source and/or binary forms;
provided that if you redistribute the Apple Software in its entirety and
without modifications, you must retain this notice and the following
text and disclaimers in all such redistributions of the Apple Software.
Neither the name, trademarks, service marks or logos of Apple Inc. may
be used to endorse or promote products derived from the Apple Software
without specific prior written permission from Apple.  Except as
expressly stated in this notice, no other rights or licenses, express or
implied, are granted by Apple herein, including but not limited to any
patent rights that may be infringed by your derivative works or by other
works in which the Apple Software may be incorporated.

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

Copyright (C) 2011 Apple Inc. All Rights Reserved.

*/

#photos {
  position: absolute;
  width: 320px;
  height: 480px;
}

/* Make sure that when the menu is visible the photo frame hides itself. Note
   the transition specified above which causes this to be a fade rather
   than a quick snap. */
body.menu-visible #photos {
  opacity: 0;
}

/* Set up the display of the CoverFlow. This is quite important because
   much of the visual appearance is controlled by the style (the JavaScript
   code is mostly configuring interaction behaviour).
   In this case the flow will span the entire width of the application.
   It sets up a perspective which will cause the elements to be placed
   in a 3D environment, and gives a vanishing point (perspective
   origin) */

#photos .ad-flow-view {
  position: relative;
  left: 0px;
  top: 190px;
  width: 320px;
  height: 250px;
  background: black;
  -webkit-perspective: 700;
  -webkit-perspective-origin: 160px 115px;
}

/* This is the 'camera' object of the flow, which represents the point
   that the viewer is looking from. It is mostly a virtual object that
   is used for positioning its children. */
#photos .ad-flow-view .ad-flow-view-camera {
  position: absolute;
  left: 160px; /* left * 2 == width of flow view */
  width: 5px;
  height: 5px;
}

/* Each element in the flow is contained in a cell. The flow will position
   the cells along the axis, but it is important to center the cell over
   the middle of the view. For that reason, we offset the left value by
   half of the cell width. */
#photos .ad-flow-view .ad-flow-view-cell {
  position: absolute;
  top: 25px;
  left: -63px; /* center element */
  width: 125px;
  height: 175px; /* this is bigger than we need, so we have room for a reflection */
}

/* Next we have the actual content of each cell, in this case an image child.
   We add a little reflection to make it look like the elements are sitting on
   a plane. */
#photos .ad-flow-view .ad-flow-view-cell img {
  pointer-events: none;
  width: 125px;
  height: 125px;
  -webkit-box-reflect: below 0px -webkit-gradient(linear, left top, left bottom, from(transparent), color-stop(0.8, transparent), to(rgba(255,255,255,0.35)));
}

/* Position the save photo button */
#photos .save-button img {
  position: absolute;
  left: 135px;
  top: 370px;
  width: 50px;
  height: 40px;
}
```

[Next](spacetours.ad-AdUnit-css-pricelist.css.md)[Previous](spacetours.ad-AdUnit-css-menu.css.md)

