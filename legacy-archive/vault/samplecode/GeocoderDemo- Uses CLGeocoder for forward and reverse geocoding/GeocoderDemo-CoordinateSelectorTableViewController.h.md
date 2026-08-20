---
title: 'GeocoderDemo: Uses CLGeocoder for forward and reverse geocoding'
apple_id: DTS40011097
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreLocation
published: '2015-10-30'
source_url: https://developer.apple.com/library/archive/samplecode/GeocoderDemo/Listings/GeocoderDemo_CoordinateSelectorTableViewController_h.html
archived_at: '2026-07-18T03:10:42.238714Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GeocoderDemo: Uses CLGeocoder for forward and reverse geocoding](GeocoderDemo-%20Uses%20CLGeocoder%20for%20forward%20and%20reverse%20geocoding.md)


[Next](Document%20Revision%20History.md)[Previous](GeocoderDemo-GeocoderDemoAppDelegate.h.md)

# GeocoderDemo/CoordinateSelectorTableViewController.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 UITableViewController that allows for the selection of a CLCoordinate2D.
 */

@import UIKit;
@import CoreLocation;

typedef NS_ENUM(NSInteger, CoordinateSelectorLastSelectedType)
{
    CoordinateSelectorLastSelectedTypeSearch = 1,
    CoordinateSelectorLastSelectedTypeCurrent,
    CoordinateSelectorLastSelectedTypeUndefined,
} ;

// this class contains a list of names and associated Coordinates as well as allowing
// for the selection of a custom Coordinate it vends the users selection through
// the 4 selected properties..
//
@interface CoordinateSelectorTableViewController : UITableViewController <UITextFieldDelegate, CLLocationManagerDelegate>

@property (readonly) CLLocationCoordinate2D selectedCoordinate;
@property (readonly) CoordinateSelectorLastSelectedType selectedType;
@property (readonly) NSString *selectedName;

@end
```

[Next](Document%20Revision%20History.md)[Previous](GeocoderDemo-GeocoderDemoAppDelegate.h.md)

