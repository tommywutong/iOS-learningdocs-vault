---
title: 'PhotoHandoff: Implementing NSUserActivity to hand off user actions'
apple_id: TP40014785
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoHandoff/Listings/PhotoHandoff_AAPLDetailViewController_h.html
archived_at: '2026-07-18T03:18:50.503549Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoHandoff: Implementing NSUserActivity to hand off user actions](PhotoHandoff-%20Implementing%20NSUserActivity%20to%20hand%20off%20user%20actions.md)


[Next](PhotoHandoff-AAPLDataSource.h.md)[Previous](PhotoHandoff-AAPLDataSource.m.md)

# PhotoHandoff/AAPLDetailViewController.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.

 See LICENSE.txt for this sample’s licensing information



 Abstract:



  The secondary detailed view controller to display a single photo.


 */

#import <UIKit/UIKit.h>

@class AAPLDataSource;

@interface AAPLDetailViewController : UIViewController <UIObjectRestoration>

@property (nonatomic, strong) NSString *imageIdentifier;
@property (nonatomic, strong) AAPLDataSource *dataSource;

- (void)restoreActivityForImageIdentifier:(NSString *)imageIdentifier userInfoDictionary:(NSDictionary *)userInfoDictionary;
- (void)prepareForActivity;
- (void)dismissFromActivityWithCompletionHandler:(void (^)(void))completionHandler;

@end
```

[Next](PhotoHandoff-AAPLDataSource.h.md)[Previous](PhotoHandoff-AAPLDataSource.m.md)

