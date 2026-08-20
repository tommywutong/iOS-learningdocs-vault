---
title: Space Tours iAd
apple_id: DTS40010222
resource_type: Sample Code
platform: iAd Producer|iOS
topic: User Experience
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/samplecode/SpaceTours/Listings/spacetours_ad_AdUnit_js_maps_js.html
archived_at: '2026-07-18T03:25:15.034151Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Space Tours iAd](Space%20Tours%20iAd.md)


[Next](spacetours.ad-AdUnit-js-menu.js.md)[Previous](spacetours.ad-AdUnit-js-main.js.md)

# spacetours.ad/AdUnit/js/maps.js

```
/*
    File: maps.js
Abstract: The View Controller subclass that implements the map.
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
  name: 'MapsController',
  superclass: iAd.ViewController
});

MapsController.prototype.init = function (configuration) {
  this.callSuper(configuration);

  // We want to zoom the map to the annotations, but only the
  // first time they are added.
  this.mapHasZoomed = false;
};

/* ---------------------------------- */
/* Methods overridden from superclass */
/* ---------------------------------- */

MapsController.prototype.viewDidLoad = function () {
  this.callSuper();

  // Since maps are only available in the iAd system, we can not
  // execute this code unless we are there.

  if (runningInAdContext) {

    // Create a set of annotations but don't add them to the map yet.
    var pinURL = window.location.toString().replace(/\/[^\/]*$/, "/") + "assets/map/pin.png";
    this.annotations = new Array();
    this.annotationBounds = { minx : Number.MAX_VALUE, miny : Number.MAX_VALUE, maxx : -Number.MAX_VALUE, maxy : -Number.MAX_VALUE};
    for (var i=0; i < MapLocations.length; i++) {
      var info = MapLocations[i];
      var specialPinType = info[5];
      var annotation = {
        identifier : "id" + info[0],
        title : info[1],
        subtitle : info[2],
        latitude : info[3],
        longitude : info[4],
        imageURL : pinURL,
        // The image for the pin has the location point (where the 'pin' looks
        // like it is hitting the ground) offset from the center point of the
        // image. Tell the map how it should position the image to make things
        // look correct, otherwise zooming will make the pin appear to move.
        xOffset : 0,
        yOffset : -18
      };

      // Keep track of the annotation boundaries, so we can zoom to this location.
      this.annotationBounds.minx = Math.min(this.annotationBounds.minx, info[3]);
      this.annotationBounds.miny = Math.min(this.annotationBounds.miny, info[4]);
      this.annotationBounds.maxx = Math.max(this.annotationBounds.maxx, info[3]);
      this.annotationBounds.maxy = Math.max(this.annotationBounds.maxy, info[4]);

      // Add the pin to a local array.
      this.annotations.push(annotation);
    }
  }
};

// Create the maps plugin and add it to the document.
MapsController.prototype.viewDidAppear = function() {
  this.callSuper();
  if (runningInAdContext) {

    // Create the map plugin
    var map = document.createElement('object');
    map.setAttribute("type", "application/x-geomap");
    this.outlets.mapcontainer.appendChild(map);
    this.map = map;

    // The plugin API is not ready to be used until the next execution
    // cycle. Call an initialize method to set the map up as soon
    // as possible.
    this.callMethodNameAfterDelay('initializeMap', 0);
  }
};

MapsController.prototype.initializeMap = function() {
  // Make sure we are the listener object, so we're told about map updates.
  this.map.listener = this;

  // Show current user location
  this.map.showsUserLocation = true;

  // Add the annotations. Do it with a slight delay so that
  // the user can see the pins drop.
  var annotations = this.annotations;
  var _this = this;
  window.setTimeout(function() {
    _this.map.addAnnotations(annotations);
  }, 500);

  // If the user set a region (by panning or zooming themselves)
  // then restore it.
  if (this.lastRegion) {
    var region = {
      latitude : this.lastRegion.latitude,
      longitude : this.lastRegion.longitude,
      latitudeDelta : this.lastRegion.latitudeDelta,
      longitudeDelta : this.lastRegion.longitudeDelta
    };
    this.map.setRegion(region, false);
  }
};

// Remove and delete the map object when it is no longer needed.
MapsController.prototype.viewWillDisappear = function() {
  if (runningInAdContext) {
    this.outlets.mapcontainer.removeChild(this.map);
    this.map = null;
  }
};

/* -------------------------- */
/* MapListener implementation */
/* -------------------------- */

// Keep track of the current region so that if the user navigates away from
// this view, we can set the region correctly upon return.
MapsController.prototype.mapRegionDidChange = function (region) {
  this.lastRegion = region;
};

// When we get told the user location is available, zoom to all the
// annotations so the user knows where they are in relation. Only do this
// the first time the location becomes available.
MapsController.prototype.mapDidUpdateUserLocation = function (location) {
  if (!this.mapHasZoomed) {
    this.mapHasZoomed = true;
    // Get the annotation bounds we recorded earlier, and set this as the current map region.
    var latitudeDelta = this.annotationBounds.maxx - this.annotationBounds.minx;
    var longitudeDelta = this.annotationBounds.maxy - this.annotationBounds.miny;
    // We don't want to zoom completely in on the annotations. We should add
    // a little extra to the region, in this case 25%.
    var region = {
      latitude : this.annotationBounds.minx + (0.5 * latitudeDelta),
      longitude : this.annotationBounds.miny + (0.5 * longitudeDelta),
      latitudeDelta : latitudeDelta * 1.25,
      longitudeDelta : longitudeDelta * 1.25
    };
    this.map.setRegion(region, true);
  }
};
```

[Next](spacetours.ad-AdUnit-js-menu.js.md)[Previous](spacetours.ad-AdUnit-js-main.js.md)

