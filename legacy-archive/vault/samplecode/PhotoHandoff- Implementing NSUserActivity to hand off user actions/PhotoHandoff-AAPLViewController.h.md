---
title: 'PhotoHandoff: Implementing NSUserActivity to hand off user actions'
apple_id: TP40014785
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoHandoff/Listings/PhotoHandoff_AAPLViewController_h.html
archived_at: '2026-07-18T03:18:50.921894Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoHandoff: Implementing NSUserActivity to hand off user actions](PhotoHandoff-%20Implementing%20NSUserActivity%20to%20hand%20off%20user%20actions.md)


[Next](PhotoHandoff-AAPLAppDelegate.h.md)[Previous](PhotoHandoff-AAPLImageFilter.m.md)

# PhotoHandoff/AAPLViewController.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  The primary collection view controller for this app.

 */

#import <UIKit/UIKit.h>

@class AAPLDataSource;

@interface AAPLViewController : UICollectionViewController

@property (nonatomic, strong) AAPLDataSource *dataSource;

// these are used by the AppDelegate
- (BOOL)handleUserActivity:(NSUserActivity *)userActivity;
- (void)prepareForActivity;
- (void)handleActivityFailure;

@end
```

[Next](PhotoHandoff-AAPLAppDelegate.h.md)[Previous](PhotoHandoff-AAPLImageFilter.m.md)

