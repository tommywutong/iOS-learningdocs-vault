---
title: LocateMe
apple_id: DTS40007801
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreLocation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LocateMe/Listings/LocateMe_GetLocationViewController_h.html
archived_at: '2026-07-18T03:13:46.080243Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LocateMe](LocateMe.md)


[Next](LocateMe-LocationDetailViewController.h.md)[Previous](LocateMe-LocationDetailViewController.m.md)

# LocateMe/GetLocationViewController.h

```objc
/*
Copyright (C) 2014 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:

Attempts to acquire a location measurement with a specific level of accuracy. A timeout is used to avoid wasting power in the case where a sufficiently accurate measurement cannot be acquired. Presents a SetupViewController instance so the user can configure the desired accuracy and timeout. Uses a LocationDetailViewController instance to drill down into details for a given location measurement.

*/

#import <UIKit/UIKit.h>

@interface GetLocationViewController : UIViewController

@end
```

[Next](LocateMe-LocationDetailViewController.h.md)[Previous](LocateMe-LocationDetailViewController.m.md)

