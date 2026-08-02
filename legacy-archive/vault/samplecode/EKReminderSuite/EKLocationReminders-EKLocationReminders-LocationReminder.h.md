---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKLocationReminders_EKLocationReminders_LocationReminder_h.html
archived_at: '2026-07-18T03:07:29.252199Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKLocationReminders-EKLocationReminders-RemindersViewController.h.md)[Previous](EKLocationReminders-EKLocationReminders-LocationReminderStore.h.md)

# EKLocationReminders/EKLocationReminders/LocationReminder.h

```objc
/*

 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Model class representing a location reminder.

 */


@interface LocationReminder : NSObject
@property(nonatomic) double radius;
// Reminder's title
@property (nonatomic, copy) NSString *title;
// Reminder's proximity value
@property (nonatomic, copy) NSString *proximity;
// Reminder's recurrence frequency
@property (nonatomic, copy) NSString *frequency;
// Reminder's location used to trigger alarm
@property (nonatomic, strong) EKStructuredLocation *structuredLocation;

-(instancetype)initWithTitle:(NSString *)name proximity:(NSString *)proximity structureLocation:(EKStructuredLocation *)location NS_DESIGNATED_INITIALIZER;

@end
```

[Next](EKLocationReminders-EKLocationReminders-RemindersViewController.h.md)[Previous](EKLocationReminders-EKLocationReminders-LocationReminderStore.h.md)

