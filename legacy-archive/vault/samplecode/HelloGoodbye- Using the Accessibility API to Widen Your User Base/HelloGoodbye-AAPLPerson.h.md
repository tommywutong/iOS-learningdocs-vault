---
title: 'HelloGoodbye: Using the Accessibility API to Widen Your User Base'
apple_id: TP40014593
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGoodbye/Listings/HelloGoodbye_AAPLPerson_h.html
archived_at: '2026-07-18T03:11:50.072595Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGoodbye: Using the Accessibility API to Widen Your User Base](HelloGoodbye-%20Using%20the%20Accessibility%20API%20to%20Widen%20Your%20User%20Base.md)


[Next](HelloGoodbye-AAPLAppDelegate.m.md)[Previous](HelloGoodbye-AAPLCardView.m.md)

# HelloGoodbye/AAPLPerson.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  A model class that represents a user in the application.

 */

@import UIKit;

@interface AAPLPerson : NSObject

@property (nonatomic) UIImage *photo;
@property (nonatomic) NSUInteger age;
@property (nonatomic) NSString *hobbies;
@property (nonatomic) NSString *elevatorPitch;

// Property list deserialization
+ (instancetype)personWithDictionary:(NSDictionary *)personDictionary;

@end
```

[Next](HelloGoodbye-AAPLAppDelegate.m.md)[Previous](HelloGoodbye-AAPLCardView.m.md)

