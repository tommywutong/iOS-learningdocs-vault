---
title: 'Regions: region monitoring, significant location changes, background location
  service, location service authorization'
apple_id: DTS40010726
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/Regions/Listings/Regions_RegionAnnotationView_h.html
archived_at: '2026-07-18T03:22:05.205430Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Regions: region monitoring, significant location changes, background location service, location service authorization](Regions-%20region%20monitoring%2C%20significant%20location%20changes%2C%20background%20location%20se.md)


[Next](Regions-RegionsViewController.h.md)[Previous](Regions-RegionsViewController.m.md)

# Regions/RegionAnnotationView.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The custom annotation view to display a region that is being monitored.
 */

#import <MapKit/MapKit.h>

@class RegionAnnotation;

@interface RegionAnnotationView : MKPinAnnotationView { 

}


@property (nonatomic, weak) MKMapView *map;
@property (nonatomic, weak) RegionAnnotation *theAnnotation;

- (instancetype)initWithAnnotation:(id <MKAnnotation>)annotation NS_DESIGNATED_INITIALIZER;
- (void)updateRadiusOverlay;
- (void)removeRadiusOverlay;

@end
```

[Next](Regions-RegionsViewController.h.md)[Previous](Regions-RegionsViewController.m.md)

