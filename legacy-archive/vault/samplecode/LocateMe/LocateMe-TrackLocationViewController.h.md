---
title: LocateMe
apple_id: DTS40007801
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreLocation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LocateMe/Listings/LocateMe_TrackLocationViewController_h.html
archived_at: '2026-07-18T03:13:46.387907Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LocateMe](LocateMe.md)


[Next](LocateMe-AppDelegate.h.md)[Previous](LocateMe-LocationDetailViewController.h.md)

# LocateMe/TrackLocationViewController.h

```objc
/*
Copyright (C) 2014 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:

Attempts to track the user location with a specific level of accuracy. A "distance filter" indicates the smallest change in location that triggers an update from the location manager to its delegate. Presents a SetupViewController instance so the user can configure the desired accuracy and distance filter. Uses a LocationDetailViewController instance to drill down into details for a given location measurement.

*/

#import <UIKit/UIKit.h>

@interface TrackLocationViewController : UIViewController

@end
```

[Next](LocateMe-AppDelegate.h.md)[Previous](LocateMe-LocationDetailViewController.h.md)

