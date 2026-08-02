---
title: 'Regions: region monitoring, significant location changes, background location
  service, location service authorization'
apple_id: DTS40010726
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/Regions/Listings/Regions_RegionAnnotation_h.html
archived_at: '2026-07-18T03:22:05.303235Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Regions: region monitoring, significant location changes, background location service, location service authorization](Regions-%20region%20monitoring%2C%20significant%20location%20changes%2C%20background%20location%20se.md)


[Next](Regions-RegionAnnotationView.m.md)[Previous](Regions-RegionsViewController.h.md)

# Regions/RegionAnnotation.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The annotation to represent a region that is being monitored.
 */

@import MapKit;

@interface RegionAnnotation : NSObject <MKAnnotation> {

}

@property (nonatomic, strong) CLRegion *region;
@property (nonatomic, readwrite) CLLocationCoordinate2D coordinate;
@property (nonatomic, readwrite) CLLocationDistance radius;
@property (nonatomic, copy) NSString *title;

- (instancetype)initWithCLRegion:(CLRegion *)newRegion;

@end
```

[Next](Regions-RegionAnnotationView.m.md)[Previous](Regions-RegionsViewController.h.md)

