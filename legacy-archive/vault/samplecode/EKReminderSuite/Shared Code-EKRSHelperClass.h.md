---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/Shared_Code_EKRSHelperClass_h.html
archived_at: '2026-07-18T03:07:31.838812Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](Shared%20Code-EKRSConstants.m.md)[Previous](Shared%20Code-EKRSReminderStore.h.md)

# Shared Code/EKRSHelperClass.h

```objc
/*

 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A helper class that includes methods to create a date formatter, generate a custom date, and display an alert.

 */

#define kMeter 1609.344

@interface EKRSHelperClass : NSObject
+(NSDateFormatter *)dateFormatter;
+(NSDate*)dateByAddingDays:(NSInteger)day;
+(UIAlertController *)alertWithTitle:(NSString *)title message:(NSString *)message;

@end
```

[Next](Shared%20Code-EKRSConstants.m.md)[Previous](Shared%20Code-EKRSReminderStore.h.md)

