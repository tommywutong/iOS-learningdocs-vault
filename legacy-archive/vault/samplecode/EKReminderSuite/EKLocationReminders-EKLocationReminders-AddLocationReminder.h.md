---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKLocationReminders_EKLocationReminders_AddLocationReminder_h.html
archived_at: '2026-07-18T03:07:28.887167Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKLocationReminders-EKLocationReminders-AppDelegate.h.md)[Previous](EKLocationReminders-EKLocationReminders-RemindersViewController.m.md)

# EKLocationReminders/EKLocationReminders/AddLocationReminder.h

```objc
/*

 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This view controller allows you to enter the title, proximity, and geofence's radius for a new location-based reminder.

 */

#import "LocationReminder.h"

@interface AddLocationReminder : UITableViewController
@property (nonatomic, strong) LocationReminder *reminder;
// Location's name
@property (nonatomic, copy) NSString *name;
// Location's address
@property (nonatomic, copy) NSString *address;
// Used to pass back the user input to the Map view controller
@property (nonatomic, strong) NSDictionary *userInput;

@end
```

[Next](EKLocationReminders-EKLocationReminders-AppDelegate.h.md)[Previous](EKLocationReminders-EKLocationReminders-RemindersViewController.m.md)

