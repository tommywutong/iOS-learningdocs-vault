---
title: 'Breadcrumb: Using CoreLocation to track user movement'
apple_id: DTS40010048
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: CoreLocation
published: '2018-05-17'
source_url: https://developer.apple.com/library/archive/samplecode/Breadcrumb/Listings/Breadcrumb_CrumbPath_h.html
archived_at: '2026-07-27T06:57:01.932594Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Breadcrumb: Using CoreLocation to track user movement](Breadcrumb-%20Using%20CoreLocation%20to%20track%20user%20movement.md)


[Next](LICENSE.txt.md)[Previous](Breadcrumb-BreadcrumbAppDelegate.m.md)

# Breadcrumb/CrumbPath.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 CrumbPath is an MKOverlay model class representing a path that changes over time.
 */

@import MapKit;

@interface CrumbPath : NSObject <MKOverlay>

// Initialize the CrumbPath with the starting coordinate.
// The CrumbPath's boundingMapRect will be set to a sufficiently large square
// centered on the starting coordinate.
//
- (instancetype)initWithCenterCoordinate:(CLLocationCoordinate2D)coord NS_DESIGNATED_INITIALIZER;

// Add a location observation. A MKMapRect containing the newly added point
// and the previously added point is returned so that the view can be updated
// in that rectangle.  If the added coordinate has not moved far enough from
// the previously added coordinate it will not be added to the list and
// MKMapRectNull will be returned.
//
- (MKMapRect)addCoordinate:(CLLocationCoordinate2D)coord boundingMapRectChanged:(BOOL *)boundingMapRectChanged;

// Synchronously evaluate a block with the current buffer of points.
- (void)readPointsWithBlockAndWait:(void (^)(MKMapPoint *pointsArray, NSUInteger pointArrayCount))block;

@end
```

[Next](LICENSE.txt.md)[Previous](Breadcrumb-BreadcrumbAppDelegate.m.md)
