---
title: Space Tours iAd
apple_id: DTS40010222
resource_type: Sample Code
platform: iAd Producer|iOS
topic: User Experience
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/samplecode/SpaceTours/Listings/spacetours_ad_AdUnit_js_main_js.html
archived_at: '2026-07-18T03:25:14.974549Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Space Tours iAd](Space%20Tours%20iAd.md)


[Next](spacetours.ad-AdUnit-js-maps.js.md)[Previous](spacetours.ad-AdUnit-js-conf.js.md)

# spacetours.ad/AdUnit/js/main.js

```
/*
    File: main.js
Abstract: The main application code.
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

// Assign a global variable to indicate whether or not
// we are running in the iAd system. This allows us to
// guard against iAd specific code yet still develop
// in Safari.
// All we do is look for the existence of a window.ad
// property.

var runningInAdContext = window.hasOwnProperty('ad');

// Configure the ApplicationController class

iAd.Class({
  name: 'ApplicationController',
  superclass: iAd.RootViewController
});

// The main entry point to the ad - the constructor of the
// ApplicationController.

ApplicationController.prototype.init = function() {
  this.callSuper();

  // Create the menu and add it to the root view of
  // the application.

  this.menu = new MenuController(MenuConfiguration);
  iAd.RootView.sharedRoot.addSubview(this.menu.view);

  // Create a view controller for each of the "pages" in the
  // ad. The pricelist view is simple - it
  // can use the generic view controller class. The others
  // have their own view controller implementation.

  this.pricelist = new iAd.ViewController(PricelistConfiguration);
  this.photos = new PhotosController(PhotosConfiguration);
  this.maps = new MapsController(MapsConfiguration);
  this.video = new VideoController(VideoConfiguration);
  this.store = new StoreController(StoreConfiguration);

  // The video controller needs to be notified when the visibility
  // of the menu changes, so it can stop video playback when the menu appears.
  this.menu.addPropertyObserver('visible', this.video, 'menuVisibilityChanged');
};

// When the document is ready, we create an instance
// of the ApplicationController. iAd JS will take care of
// the rest.

window.addEventListener('DOMContentLoaded', function () {
  window.controller = new ApplicationController();
}, false);
```

[Next](spacetours.ad-AdUnit-js-maps.js.md)[Previous](spacetours.ad-AdUnit-js-conf.js.md)

