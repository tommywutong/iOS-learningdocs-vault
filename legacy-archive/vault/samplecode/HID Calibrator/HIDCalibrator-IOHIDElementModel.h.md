---
title: HID Calibrator
apple_id: DTS40007645
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2014-02-17'
source_url: https://developer.apple.com/library/archive/samplecode/HID_Calibrator/Listings/HID_Calibrator_IOHIDElementModel_h.html
archived_at: '2026-07-18T03:11:12.849834Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HID Calibrator](HID%20Calibrator.md)


[Next](HIDCalibrator-IOHIDElementModel.m.md)[Previous](HIDCalibrator-IOHIDElementCollectionViewItem.m.md)

# HID_Calibrator/IOHIDElementModel.h

```objc
//
//  HIDElementModel.h
//  HID_Calibrator
//
//  Created by George Warner on 3/26/11.
//  Copyright 2011 Apple Inc. All rights reserved.
//

#import <Foundation/Foundation.h>

#include "HID_Utilities_External.h"

@interface IOHIDElementModel : NSObject 

-(id)initWithIOHIDElementRef:(IOHIDElementRef)inIOHIDElementRef;

@property(unsafe_unretained, readonly) NSString * description;
@property(nonatomic, assign, readwrite) IOHIDElementRef _IOHIDElementRef;

@property (readonly) double logMin, logMax;
@property (readonly) double phyMin, phyMax;
@property (assign, readwrite) double phyVal;
@property (assign, readwrite) double satMin, satMax;
@property (assign, readwrite) double calMin, calMax, calVal;
@property (assign, readwrite) double deadzoneMin, deadzoneMax;

@end
```

[Next](HIDCalibrator-IOHIDElementModel.m.md)[Previous](HIDCalibrator-IOHIDElementCollectionViewItem.m.md)

