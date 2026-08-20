---
title: Space Tours iAd
apple_id: DTS40010222
resource_type: Sample Code
platform: iAd Producer|iOS
topic: User Experience
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/samplecode/SpaceTours/Listings/spacetours_ad_AdUnit_js_store_js.html
archived_at: '2026-07-18T03:25:15.200521Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Space Tours iAd](Space%20Tours%20iAd.md)


[Next](spacetours.ad-AdUnit-js-video.js.md)[Previous](spacetours.ad-AdUnit-js-photos.js.md)

# spacetours.ad/AdUnit/js/store.js

```
/*
    File: store.js
Abstract: The View Controller subclass that implements the store page.
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

iAd.Class({
  name: 'StoreController',
  superclass: iAd.ViewController
});

StoreController.prototype.init = function (configuration) {
  this.callSuper(configuration);

  // An associative array of offers from the store for each item.
  this.offers = {};

  if (runningInAdContext) {
    // Register the set of items we want to sell.
    window.ad.store.registerItemsForPurchase(StoreItems);
    // Look up each of them on the store.
    for (var i=0; i < StoreItems.length; i++) {
      window.ad.store.lookupItemWithID(StoreItems[i], this);
    }
  }
};

StoreController.prototype.buyItem = function (event) {
  // Get the index of the element we want to buy from the custom
  // HTML attribute we added to the buttons.
  var index = event.currentTarget.getAttribute("tt-index");
  if (runningInAdContext) {
    // Get the offer corresponding to the item that we received from the store.
    var offer = this.offers[StoreItems[index]];
    if (offer) {
      // Make the actual purchase.
      window.ad.store.purchaseItemWithID(StoreItems[index], offer, this);
    }
  }
};

/* ---------------------------- */
/* StoreListener implementation */
/* ---------------------------- */

StoreController.prototype.storeItemLookupDidSucceed = function(item) {
  // A lookup we invoked earlier has succeeded. Keep a copy of the offer from
  // the store because we will need it later for the actual purchase.
  this.offers[item.adamId] = item.offers[0].identifier;
};

StoreController.prototype.storeItemLookupDidFail = function(adamId, errorCode) {
  var errorMessage = "";
  switch (errorCode) {
    case 1: errorMessage = "Lookup did not return buy parameters"; break;
    case 2: errorMessage = "Item metadata expires too soon"; break;
    case 3: errorMessage = "Item not found in store"; break;
    case 4: errorMessage = "iPhone Simulator not supported"; break;
    case 5: errorMessage = "User canceled purchase"; break;
    case 6: errorMessage = "Must lookup item before attempting purchase"; break;
    default: errorMessage = "Unknown error";
  }
  console.log("Purchasing Lookup Error: " + errorMessage);
};

StoreController.prototype.storeItemMetadataDidExpire = function(adamID) {
  console.log("Metadata has expired for item: " + adamID);
};

StoreController.prototype.storeItemPurchaseDidFail = function(adamID, errorCode) {
  var errorMessage = "";
  switch (errorCode) {
    case 1: errorMessage = "Lookup did not return buy parameters"; break;
    case 2: errorMessage = "Item metadata expires too soon"; break;
    case 3: errorMessage = "Item not found in store"; break;
    case 4: errorMessage = "iPhone Simulator not supported"; break;
    case 5: errorMessage = "User canceled purchase"; break;
    case 6: errorMessage = "Must lookup item before attempting purchase"; break;
    default: errorMessage = "Unknown error";
  }
  console.log("Purchasing Buy Error: " + errorMessage);
};

StoreController.prototype.storeItemPurchaseDidSucceed = function(adamID) {
  console.log("Purchase succeeded!");
};
```

[Next](spacetours.ad-AdUnit-js-video.js.md)[Previous](spacetours.ad-AdUnit-js-photos.js.md)

