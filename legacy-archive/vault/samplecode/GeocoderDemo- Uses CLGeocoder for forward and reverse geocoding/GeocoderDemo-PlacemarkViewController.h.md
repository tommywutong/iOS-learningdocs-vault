---
title: 'GeocoderDemo: Uses CLGeocoder for forward and reverse geocoding'
apple_id: DTS40011097
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreLocation
published: '2015-10-30'
source_url: https://developer.apple.com/library/archive/samplecode/GeocoderDemo/Listings/GeocoderDemo_PlacemarkViewController_h.html
archived_at: '2026-07-18T03:10:42.747720Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GeocoderDemo: Uses CLGeocoder for forward and reverse geocoding](GeocoderDemo-%20Uses%20CLGeocoder%20for%20forward%20and%20reverse%20geocoding.md)


[Next](GeocoderDemo-ReverseViewController.h.md)[Previous](GeocoderDemo-DistanceViewController.h.md)

# GeocoderDemo/PlacemarkViewController.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 UITableViewController that displays the propeties of a CLPlacemark.
 */

@import UIKit;
@import MapKit;

@interface PlacemarkViewController : UITableViewController <MKAnnotation>

- (instancetype)initWithPlacemark:(CLPlacemark *)placemark NS_DESIGNATED_INITIALIZER;

#pragma mark - MKAnnotation Protocol (for map pin)

@property (nonatomic, readonly) CLLocationCoordinate2D coordinate;
@property (NS_NONATOMIC_IOSONLY, copy) NSString *title;

@end
```

[Next](GeocoderDemo-ReverseViewController.h.md)[Previous](GeocoderDemo-DistanceViewController.h.md)

