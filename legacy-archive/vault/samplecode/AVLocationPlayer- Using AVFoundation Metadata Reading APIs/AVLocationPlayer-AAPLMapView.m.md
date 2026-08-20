---
title: 'AVLocationPlayer: Using AVFoundation Metadata Reading APIs'
apple_id: TP40014495
resource_type: Sample Code
platform: macOS
topic: null
technology: AVFoundation
published: '2015-04-30'
source_url: https://developer.apple.com/library/archive/samplecode/AVLocationPlayer/Listings/AVLocationPlayer_AAPLMapView_m.html
archived_at: '2026-07-18T03:00:18.060013Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVLocationPlayer: Using AVFoundation Metadata Reading APIs](AVLocationPlayer-%20Using%20AVFoundation%20Metadata%20Reading%20APIs.md)


[Next](Document%20Revision%20History.md)[Previous](AVLocationPlayer-AAPLMapView.h.md)

# AVLocationPlayer/AAPLMapView.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom map view which handles user interaction for seeking in video.
 */

#import "AAPLMapView.h"

NSString *const AAPLMapViewSeekPositionKey = @"AAPLMapViewSeekPositionKey";
NSString *const AAPLMapViewUserDidUpdateSeekPositionNotification = @"AAPLMapViewUserDidUpdateSeekPositionNotification";
NSString *const AAPLMapViewUserDidInteractWithMapNotification = @"AAPLMapViewUserDidInteractWithMapNotification";

@implementation AAPLMapView

- (void)rightMouseDown:(NSEvent *)theEvent
{
    NSPoint eventLocation = [theEvent locationInWindow];
    NSPoint localPoint = [self convertPoint:eventLocation fromView:nil];

    CLLocationCoordinate2D locCoord = [self convertPoint:localPoint toCoordinateFromView:self];
    CLLocation *newLocation = [[CLLocation alloc] initWithLatitude:locCoord.latitude longitude:locCoord.longitude];

    NSNotification *notification = [NSNotification notificationWithName:AAPLMapViewUserDidUpdateSeekPositionNotification
                                                                 object:self
                                                               userInfo:@{AAPLMapViewSeekPositionKey : newLocation}];
    [[NSNotificationCenter defaultCenter] postNotification:notification];
}

- (void)mouseDragged:(NSEvent *)theEvent
{
    NSNotification *notification = [NSNotification notificationWithName:AAPLMapViewUserDidInteractWithMapNotification
                                                                 object:self
                                                               userInfo:nil];
    [[NSNotificationCenter defaultCenter] postNotification:notification];

    [super mouseDragged:theEvent];
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](AVLocationPlayer-AAPLMapView.h.md)

