---
title: 'PhotoHandoff: Implementing NSUserActivity to hand off user actions'
apple_id: TP40014785
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoHandoff/Listings/PhotoHandoff_AAPLCustomCellBackground_m.html
archived_at: '2026-07-18T03:18:50.382714Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoHandoff: Implementing NSUserActivity to hand off user actions](PhotoHandoff-%20Implementing%20NSUserActivity%20to%20hand%20off%20user%20actions.md)


[Next](PhotoHandoff-AAPLAppDelegate.m.md)[Previous](LICENSE.txt.md)

# PhotoHandoff/AAPLCustomCellBackground.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 */

#import "AAPLCustomCellBackground.h"

@implementation AAPLCustomCellBackground

+ (UIView *)customCellBackground {

    id obj = [[self class] alloc];
    return obj;
}

- (instancetype)initWithFrame:(CGRect)frame {

    self = [super initWithFrame:frame];
    if (self != nil) {
        self.backgroundColor = [UIColor lightGrayColor];
        self.layer.cornerRadius = 5.0;
    }
    return self;
}

@end
```

[Next](PhotoHandoff-AAPLAppDelegate.m.md)[Previous](LICENSE.txt.md)

