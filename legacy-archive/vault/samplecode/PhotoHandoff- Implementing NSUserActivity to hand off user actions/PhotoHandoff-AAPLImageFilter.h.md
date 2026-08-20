---
title: 'PhotoHandoff: Implementing NSUserActivity to hand off user actions'
apple_id: TP40014785
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoHandoff/Listings/PhotoHandoff_AAPLImageFilter_h.html
archived_at: '2026-07-18T03:18:50.826728Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoHandoff: Implementing NSUserActivity to hand off user actions](PhotoHandoff-%20Implementing%20NSUserActivity%20to%20hand%20off%20user%20actions.md)


[Next](PhotoHandoff-AAPLDetailViewController.m.md)[Previous](PhotoHandoff-AAPLAppDelegate.m.md)

# PhotoHandoff/AAPLImageFilter.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.

 See LICENSE.txt for this sample’s licensing information



 Abstract:



  Image Filter Objects


 */

#import <Foundation/Foundation.h>

@interface AAPLImageFilter : NSObject <UIStateRestoring>

- (instancetype)initFilter:(BOOL)useDefaultState NS_DESIGNATED_INITIALIZER;

@property (nonatomic) BOOL active;
@property (nonatomic) BOOL dirty;
@property (nonatomic, readwrite, strong) id<UIStateRestoring> restorationParent;
@property (nonatomic, readwrite, strong) Class<UIObjectRestoration> objectRestorationClass;
@end

#pragma mark -

#define kBlurFilterKey @"BlurFilter"

@interface BlurFilter : AAPLImageFilter
@property (nonatomic) CGFloat blurRadius;
@end

#pragma mark -

#define kModifyFilterKey @"ModifyFilter"

@interface ModifyFilter : AAPLImageFilter
@property (nonatomic) CGFloat intensity;

@end
```

[Next](PhotoHandoff-AAPLDetailViewController.m.md)[Previous](PhotoHandoff-AAPLAppDelegate.m.md)

