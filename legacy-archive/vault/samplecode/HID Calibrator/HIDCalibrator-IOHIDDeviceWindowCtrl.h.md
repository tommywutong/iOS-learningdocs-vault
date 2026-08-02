---
title: HID Calibrator
apple_id: DTS40007645
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2014-02-17'
source_url: https://developer.apple.com/library/archive/samplecode/HID_Calibrator/Listings/HID_Calibrator_IOHIDDeviceWindowCtrl_h.html
archived_at: '2026-07-18T03:11:12.543089Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HID Calibrator](HID%20Calibrator.md)


[Next](HIDCalibrator-IOHIDDeviceWindowCtrl.m.md)[Previous](HIDCalibrator-IOHIDDeviceView.m.md)

# HID_Calibrator/IOHIDDeviceWindowCtrl.h

```objc
//
//  IOHIDDeviceWindowCtrl.h
//  HID_Calibrator
//
//  Created by George Warner on 3/26/11.
//  Copyright 2011 Apple Inc. All rights reserved.
//

#import <Cocoa/Cocoa.h>

#include "HID_Utilities_External.h"

@interface IOHIDDeviceWindowCtrl : NSWindowController

-(id)initWithIOHIDDeviceRef:(IOHIDDeviceRef)inIOHIDDeviceRef;

@property (assign, nonatomic, readwrite) IOHIDDeviceRef _IOHIDDeviceRef;
@property (unsafe_unretained, nonatomic, readwrite) NSArray * _IOHIDElementModels;
@property (unsafe_unretained, readonly) NSString * name;
@end
```

[Next](HIDCalibrator-IOHIDDeviceWindowCtrl.m.md)[Previous](HIDCalibrator-IOHIDDeviceView.m.md)

