---
title: HID Calibrator
apple_id: DTS40007645
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2014-02-17'
source_url: https://developer.apple.com/library/archive/samplecode/HID_Calibrator/Listings/HID_Calibrator_IOHIDElementCollectionViewItem_h.html
archived_at: '2026-07-18T03:11:12.738616Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HID Calibrator](HID%20Calibrator.md)


[Next](HIDCalibrator-IOHIDElementCollectionViewItem.m.md)[Previous](HIDCalibrator-IOHIDDeviceWindowCtrl.m.md)

# HID_Calibrator/IOHIDElementCollectionViewItem.h

```objc
//
//  IOHIDElementCollectionView.h
//  HID_Calibrator
//
//  Created by George Warner on 3/27/11.
//  Copyright 2011 Apple Inc. All rights reserved.
//

#import <Foundation/Foundation.h>

#import "MyLevelIndicatorView.h"

@interface IOHIDElementCollectionViewItem : NSCollectionViewItem
@property (unsafe_unretained, readonly) IBOutlet MyLevelIndicatorView   *levelIndicatorView;
@end
```

[Next](HIDCalibrator-IOHIDElementCollectionViewItem.m.md)[Previous](HIDCalibrator-IOHIDDeviceWindowCtrl.m.md)

