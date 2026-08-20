---
title: HID Calibrator
apple_id: DTS40007645
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2014-02-17'
source_url: https://developer.apple.com/library/archive/samplecode/HID_Calibrator/Listings/HID_Calibrator_MyLevelIndicatorView_h.html
archived_at: '2026-07-18T03:11:13.007590Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HID Calibrator](HID%20Calibrator.md)


[Next](HIDCalibrator-MyLevelIndicatorView.m.md)[Previous](HIDCalibrator-main.m.md)

# HID_Calibrator/MyLevelIndicatorView.h

```objc
//
//  MyLevelIndicatorView.h
//  HID_Calibrator
//
//  Created by George Warner on 4/1/11.
//  Copyright 2011 Apple Inc. All rights reserved.
//

#import <Cocoa/Cocoa.h>

#import "IOHIDElementModel.h"


@interface MyLevelIndicatorView : NSView 
@property (assign, readwrite)   IOHIDElementModel * representedObject;

// this is a fake property used as a binding so changes to our element 
// model's calVal property will tell this view to update.
@property (assign, readwrite)   double  reDraw;
@end
```

[Next](HIDCalibrator-MyLevelIndicatorView.m.md)[Previous](HIDCalibrator-main.m.md)

