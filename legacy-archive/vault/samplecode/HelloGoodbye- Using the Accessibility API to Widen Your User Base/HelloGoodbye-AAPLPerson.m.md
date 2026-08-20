---
title: 'HelloGoodbye: Using the Accessibility API to Widen Your User Base'
apple_id: TP40014593
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGoodbye/Listings/HelloGoodbye_AAPLPerson_m.html
archived_at: '2026-07-18T03:11:50.109704Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGoodbye: Using the Accessibility API to Widen Your User Base](HelloGoodbye-%20Using%20the%20Accessibility%20API%20to%20Widen%20Your%20User%20Base.md)


[Next](HelloGoodbye-AAPLMatchesViewController.m.md)[Previous](HelloGoodbye-AAPLStartViewController.h.md)

# HelloGoodbye/AAPLPerson.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  A model class that represents a user in the application.

 */

#import "AAPLPerson.h"

static NSString *const AAPLPersonPhotoKey = @"photo";
static NSString *const AAPLPersonAgeKey = @"age";
static NSString *const AAPLPersonHobbiesKey = @"hobbies";
static NSString *const AAPLPersonElevatorPitchKey = @"elevatorPitch";

@implementation AAPLPerson

+ (instancetype)personWithDictionary:(NSDictionary *)personDictionary {
    AAPLPerson *person = [[self alloc] init];

    person.photo = [UIImage imageNamed:personDictionary[AAPLPersonPhotoKey]];
    person.age = [personDictionary[AAPLPersonAgeKey] unsignedIntegerValue];
    person.hobbies = personDictionary[AAPLPersonHobbiesKey];
    person.elevatorPitch = personDictionary[AAPLPersonElevatorPitchKey];
    return person;
}

@end
```

[Next](HelloGoodbye-AAPLMatchesViewController.m.md)[Previous](HelloGoodbye-AAPLStartViewController.h.md)

