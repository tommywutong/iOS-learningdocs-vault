---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKLocationReminders_EKLocationReminders_LocationReminderStore_h.html
archived_at: '2026-07-18T03:07:29.118856Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKLocationReminders-EKLocationReminders-LocationReminder.h.md)[Previous](EKLocationReminders-ReadMe.md.md)

# EKLocationReminders/EKLocationReminders/LocationReminderStore.h

```objc
/*

 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An EKRSReminderStore subclass that shows how to create location-based reminders using EKReminder and EKAlarm.

 */

#import "EKRSReminderStore.h"
#import "LocationReminder.h"

@interface LocationReminderStore : EKRSReminderStore
+(LocationReminderStore *)sharedInstance;
-(void)createLocationReminder:(LocationReminder *)reminder;

@end
```

[Next](EKLocationReminders-EKLocationReminders-LocationReminder.h.md)[Previous](EKLocationReminders-ReadMe.md.md)

