---
title: Space Tours iAd
apple_id: DTS40010222
resource_type: Sample Code
platform: iAd Producer|iOS
topic: User Experience
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/samplecode/SpaceTours/Listings/spacetours_ad_AdUnit_js_conf_js.html
archived_at: '2026-07-18T03:25:14.909107Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Space Tours iAd](Space%20Tours%20iAd.md)


[Next](spacetours.ad-AdUnit-js-main.js.md)[Previous](spacetours.ad-AdUnit-index.html.md)

# spacetours.ad/AdUnit/js/conf.js

```
/*
    File: conf.js
Abstract: The application configuration.
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

// The list of items from the store we are selling. Make sure we
// choose free items, just in case a user of this code goes
// through with a purchase. The items here are the Apple Remote
// application, the Find My iPhone application, and the Apple
// Store application.

const StoreItems = [284417350, 376101648, 375380948];

// An array of houses we'd like to show as pins on the map

const MapLocations = [
  // [id, name, description, lat, long]
  [0, "Showroom", "River Oaks", 37.41559, -121.899423],
  [1, "Sales office", "Palo Alto", 37.443901, -122.170898],
  [2, "Headquarters", "San Francisco", 37.7888, -122.406553]
];

// Configuration information for the view controllers

var MenuConfiguration = {
  id : 'menu',
  requiredFileURIs : {
    contentView : 'views/menu.html'
  }
};

var MapsConfiguration = {
  id : 'maps',
  requiredFileURIs : {
    contentView : 'views/maps.html'
  }
};

var PricelistConfiguration = {
  id : 'pricelist',
  requiredFileURIs : {
    contentView : 'views/pricelist.html'
  }
};

var VideoConfiguration = {
  id : 'video',
  requiredFileURIs : {
    contentView : 'views/video.html'
  }
};

var StoreConfiguration = {
  id : 'store',
  requiredFileURIs : {
    contentView : 'views/store.html'
  }
};

var PhotosConfiguration = {
  id : 'photos',
  requiredFileURIs : {
    contentView : 'views/photos.html'
  }
};
```

[Next](spacetours.ad-AdUnit-js-main.js.md)[Previous](spacetours.ad-AdUnit-index.html.md)

