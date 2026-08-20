---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKTimedReminders_EKTimedReminders_TimedTabBarController_h.html
archived_at: '2026-07-18T03:07:31.246891Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](LICENSE.txt.md)[Previous](EKTimedReminders-EKTimedReminders-TimedTabBarController.m.md)

# EKTimedReminders/EKTimedReminders/TimedTabBarController.h

```objc
/*

 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This view controller manages the child view controllers: CompletedReminders, PastDueReminders and UpcomingReminders.
         It calls TimedReminderStore to check access to the Reminders application. It listens and handles TimedReminderStore notifications.
         It calls TimedReminderStore to fetch upcoming, past-due, and completed reminders. It notifies the UpcomingReminders, PastDueReminders,
         and CompletedReminders view controllers upon receiving their associated data.

 */

@interface TimedTabBarController : UITabBarController
@end
```

[Next](LICENSE.txt.md)[Previous](EKTimedReminders-EKTimedReminders-TimedTabBarController.m.md)

