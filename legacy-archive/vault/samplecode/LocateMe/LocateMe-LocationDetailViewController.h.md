---
title: LocateMe
apple_id: DTS40007801
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreLocation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LocateMe/Listings/LocateMe_LocationDetailViewController_h.html
archived_at: '2026-07-18T03:13:46.222601Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LocateMe](LocateMe.md)


[Next](LocateMe-TrackLocationViewController.h.md)[Previous](LocateMe-GetLocationViewController.h.md)

# LocateMe/LocationDetailViewController.h

```objc
/*
Copyright (C) 2014 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:

Lists the values for all the properties of a single CLLocation object.

*/

#import <UIKit/UIKit.h>
#import <CoreLocation/CoreLocation.h>

@interface LocationDetailViewController : UITableViewController

@property (nonatomic, strong) CLLocation *location;

@end
```

[Next](LocateMe-TrackLocationViewController.h.md)[Previous](LocateMe-GetLocationViewController.h.md)

