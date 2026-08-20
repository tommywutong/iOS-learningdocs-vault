---
title: EKReminderSuite
apple_id: TP40015203
resource_type: Sample Code
platform: iOS
topic: null
technology: null
published: '2015-11-13'
source_url: https://developer.apple.com/library/archive/samplecode/EKReminderSuite/Listings/EKLocationReminders_EKLocationReminders_MyAnnotation_m.html
archived_at: '2026-07-18T03:07:29.762123Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EKReminderSuite](EKReminderSuite.md)


[Next](EKLocationReminders-EKLocationReminders-LocationTabBarController.h.md)[Previous](EKLocationReminders-EKLocationReminders-AddLocationReminder.m.md)

# EKLocationReminders/EKLocationReminders/MyAnnotation.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Custom MKAnnotation object representing a generic location.
 */

#import "MyAnnotation.h"

@interface MyAnnotation()
@property (nonatomic,copy) NSString *title;
@property (nonatomic,assign) CLLocationCoordinate2D coordinate;

@end


@implementation MyAnnotation

-(instancetype)init
{
    self = [self initWithTitle:nil latitude:0.0 longitude:0.0 address: nil];
    if (self != nil)
    {
    }
    return self;
}


-(instancetype)initWithTitle:(NSString *)name latitude:(double)latitude longitude:(double)longitude address:(NSString *)address
{
    self = [super init];
    if(self != nil)
    {
        _title = name;
        _coordinate.latitude = latitude;
        _coordinate.longitude = longitude;
        _address = address;
    }
    return self;
}

@end
```

[Next](EKLocationReminders-EKLocationReminders-LocationTabBarController.h.md)[Previous](EKLocationReminders-EKLocationReminders-AddLocationReminder.m.md)

