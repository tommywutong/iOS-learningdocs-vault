---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKLocationReminders_EKLocationReminders_MyAnnotation_h.html
archived_at: '2026-07-18T03:07:29.627303Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKLocationReminders-EKLocationReminders-LocationTabBarController.m.md)[Previous](EKLocationReminders-EKLocationReminders-LocationReminder.m.md)

# EKLocationReminders/EKLocationReminders/MyAnnotation.h

```objc
/*

 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom MKAnnotation object representing a generic location.

 */

@interface MyAnnotation : NSObject <MKAnnotation>
@property(nonatomic, copy) NSString *address;
-(instancetype)initWithTitle:(NSString *)name latitude:(double)latitude longitude:(double)longitude address:(NSString *)address NS_DESIGNATED_INITIALIZER;

@end
```

[Next](EKLocationReminders-EKLocationReminders-LocationTabBarController.m.md)[Previous](EKLocationReminders-EKLocationReminders-LocationReminder.m.md)

