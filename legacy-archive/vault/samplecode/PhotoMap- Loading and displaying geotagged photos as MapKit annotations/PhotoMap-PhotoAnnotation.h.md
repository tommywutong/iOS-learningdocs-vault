---
title: 'PhotoMap: Loading and displaying geotagged photos as MapKit annotations'
apple_id: DTS40011109
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: MapKit
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoMap/Listings/PhotoMap_PhotoAnnotation_h.html
archived_at: '2026-07-18T03:18:52.146406Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoMap: Loading and displaying geotagged photos as MapKit annotations](PhotoMap-%20Loading%20and%20displaying%20geotagged%20photos%20as%20MapKit%20annotations.md)


[Next](PhotoMap-LoadingStatus.h.md)[Previous](PhotoMap-PhotoMapAppDelegate.m.md)

# PhotoMap/PhotoAnnotation.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A simple model class to display pins representing photos on the map.
 */

@import Foundation;
@import MapKit;

@interface PhotoAnnotation : NSObject <MKAnnotation>

- (id)initWithImagePath:(NSString *)imagePath title:(NSString *)title coordinate:(CLLocationCoordinate2D)coordinate;

@property (nonatomic, strong) UIImage *image;
@property (nonatomic, copy) NSString *imagePath;
@property (nonatomic, copy) NSString *title;
@property (nonatomic, copy) NSString *subtitle;
@property (nonatomic) CLLocationCoordinate2D coordinate;

@property (nonatomic, strong) PhotoAnnotation *clusterAnnotation;
@property (nonatomic, strong) NSArray *containedAnnotations;

- (void)updateSubtitleIfNeeded;

@end
```

[Next](PhotoMap-LoadingStatus.h.md)[Previous](PhotoMap-PhotoMapAppDelegate.m.md)

