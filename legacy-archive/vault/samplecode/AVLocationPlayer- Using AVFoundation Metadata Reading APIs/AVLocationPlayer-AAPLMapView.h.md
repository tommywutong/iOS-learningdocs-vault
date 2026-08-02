---
title: 'AVLocationPlayer: Using AVFoundation Metadata Reading APIs'
apple_id: TP40014495
resource_type: Sample Code
platform: macOS
topic: null
technology: AVFoundation
published: '2015-04-30'
source_url: https://developer.apple.com/library/archive/samplecode/AVLocationPlayer/Listings/AVLocationPlayer_AAPLMapView_h.html
archived_at: '2026-07-18T03:00:18.021127Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVLocationPlayer: Using AVFoundation Metadata Reading APIs](AVLocationPlayer-%20Using%20AVFoundation%20Metadata%20Reading%20APIs.md)


[Next](AVLocationPlayer-AAPLMapView.m.md)[Previous](AVLocationPlayer-AAPLDocument.m.md)

# AVLocationPlayer/AAPLMapView.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom map view which handles user interaction for seeking in video.
 */

@import Cocoa;
@import MapKit;

NSString *const AAPLMapViewSeekPositionKey;
// Notifications which post user interactions with the map

// Register for AAPLMapViewUserDidUpdateSeekPosition to be notified of a point on map where user right clicked, to seek video to correspond to that location. Use this notification in combination with AAPLMapViewSeekPositionKey to access the location where user clicked.
NSString *const AAPLMapViewUserDidUpdateSeekPositionNotification;

// Register for AAPLMapViewUserDidInteractWithMap to be notified of when a user dragged on map so we can stop centering the map with playback updates.
NSString *const AAPLMapViewUserDidInteractWithMapNotification;

@interface AAPLMapView : MKMapView
@end
```

[Next](AVLocationPlayer-AAPLMapView.m.md)[Previous](AVLocationPlayer-AAPLDocument.m.md)

