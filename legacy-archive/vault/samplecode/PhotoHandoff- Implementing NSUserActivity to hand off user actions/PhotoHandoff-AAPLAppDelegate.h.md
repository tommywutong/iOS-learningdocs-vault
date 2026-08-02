---
title: 'PhotoHandoff: Implementing NSUserActivity to hand off user actions'
apple_id: TP40014785
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoHandoff/Listings/PhotoHandoff_AAPLAppDelegate_h.html
archived_at: '2026-07-18T03:18:50.098859Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoHandoff: Implementing NSUserActivity to hand off user actions](PhotoHandoff-%20Implementing%20NSUserActivity%20to%20hand%20off%20user%20actions.md)


[Next](PhotoHandoff-AAPLDataSource.m.md)[Previous](PhotoHandoff-AAPLViewController.h.md)

# PhotoHandoff/AAPLAppDelegate.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  The sample's application delegate.

 */

#import <UIKit/UIKit.h>

@class AAPLDataSource;

@interface AAPLAppDelegate : UIResponder <UIApplicationDelegate>

@property (nonatomic, strong) UIWindow *window;
@property (nonatomic, readonly) AAPLDataSource *dataSource;

@end
```

[Next](PhotoHandoff-AAPLDataSource.m.md)[Previous](PhotoHandoff-AAPLViewController.h.md)

