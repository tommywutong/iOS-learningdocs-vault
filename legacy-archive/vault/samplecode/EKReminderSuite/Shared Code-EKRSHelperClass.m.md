---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/Shared_Code_EKRSHelperClass_m.html
archived_at: '2026-07-18T03:07:31.874793Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](Shared%20Code-EKRSReminderStoreUtilities.h.md)[Previous](EKLocationReminders-EKLocationReminders-main.m.md)

# Shared Code/EKRSHelperClass.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A helper class that includes methods to create a date formatter, generate a custom date, and display an alert.
 */

#import "EKRSHelperClass.h"

@implementation EKRSHelperClass

#pragma mark - Date Formatter

// Create a date formatter with a short date and time
+(NSDateFormatter *)dateFormatter
{
    NSDateFormatter *myDateFormatter = [[NSDateFormatter alloc] init];
    myDateFormatter.dateStyle = NSDateFormatterShortStyle;
    myDateFormatter.timeStyle = NSDateFormatterShortStyle;

    return myDateFormatter;
}


#pragma mark - Create a Date

// Create a new date by adding a given number of days to the current date
+(NSDate*)dateByAddingDays:(NSInteger)day
{
    NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSCalendarIdentifierGregorian];
    NSDateComponents *dateComponents = [[NSDateComponents alloc] init];
    dateComponents.day = day;

    return [gregorian dateByAddingComponents:dateComponents toDate:[NSDate date] options:0];
}


#pragma mark - Create Alert Dialog

// Return an alert with a given title and message
+(UIAlertController *)alertWithTitle:(NSString *)title message:(NSString *)message
{
    UIAlertController *alert = [UIAlertController alertControllerWithTitle:title
                                                                   message:message
                                                            preferredStyle:UIAlertControllerStyleActionSheet];


    UIAlertAction *defaultAction = [UIAlertAction actionWithTitle:NSLocalizedString(@"OK", nil)
                                                            style:UIAlertActionStyleDefault
                                                          handler:^(UIAlertAction * action) {}];

    [alert addAction:defaultAction];

    return alert;
}

@end
```

[Next](Shared%20Code-EKRSReminderStoreUtilities.h.md)[Previous](EKLocationReminders-EKLocationReminders-main.m.md)

