---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKLocationReminders_EKLocationReminders_LocationReminderStore_m.html
archived_at: '2026-07-18T03:07:29.186548Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKTimedReminders-ReadMe.md.md)[Previous](EKLocationReminders-EKLocationReminders-LocationTabBarController.h.md)

# EKLocationReminders/EKLocationReminders/LocationReminderStore.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An EKRSReminderStore subclass that shows how to create location-based reminders using EKReminder and EKAlarm.
 */

#import "LocationReminderStore.h"
#import "EKRSReminderStoreUtilities.h"

@implementation LocationReminderStore

+(LocationReminderStore *)sharedInstance
{
    static dispatch_once_t onceToken;
    static LocationReminderStore * locationReminderStoreSharedInstance;

    dispatch_once(&onceToken, ^{
        locationReminderStoreSharedInstance = [[LocationReminderStore alloc] init];
    });
    return locationReminderStoreSharedInstance;
}


#pragma mark -
#pragma mark Add Location Reminder

// Create a location-based reminder
-(void)createLocationReminder:(LocationReminder *)reminder
{
    EKReminder *myReminder = [EKReminder reminderWithEventStore:self.eventStore];
    myReminder.title = reminder.title;
    myReminder.calendar = self.calendar;

    // Create an alarm
    EKAlarm *alarm = [[EKAlarm alloc] init];
    // Configure a geofence by setting up the structured location and proximity properties
    alarm.proximity = [alarm proximityMatchingName:reminder.proximity];
    alarm.structuredLocation = reminder.structuredLocation;

    // Add the above alarm to myReminder
    [myReminder addAlarm:alarm];

    // Attempt to save the reminder
    [self save:myReminder];
}

@end
```

[Next](EKTimedReminders-ReadMe.md.md)[Previous](EKLocationReminders-EKLocationReminders-LocationTabBarController.h.md)

