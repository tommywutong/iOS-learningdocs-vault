---
title: 'PhotoHandoff: Implementing NSUserActivity to hand off user actions'
apple_id: TP40014785
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoHandoff/Listings/PhotoHandoff_AAPLFilterViewController_h.html
archived_at: '2026-07-18T03:18:50.722067Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoHandoff: Implementing NSUserActivity to hand off user actions](PhotoHandoff-%20Implementing%20NSUserActivity%20to%20hand%20off%20user%20actions.md)


[Next](PhotoHandoff-AAPLCustomCellBackground.h.md)[Previous](PhotoHandoff-AAPLDataSource.h.md)

# PhotoHandoff/AAPLFilterViewController.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.

 See LICENSE.txt for this sample’s licensing information



 Abstract:



  View Controller to inspect and update image filter settings


 */

#import <UIKit/UIKit.h>

@class AAPLImageFilter;

@protocol AAPLFilterViewControllerDelegate;

@interface AAPLFilterViewController : UIViewController

@property (nonatomic, strong) AAPLImageFilter *filter;
@property (nonatomic, weak) IBOutlet UISlider *slider;
@property (nonatomic, weak) IBOutlet UISwitch *activeSwitch;
@property (nonatomic, weak) IBOutlet UINavigationBar *navigationBar;
@property (nonatomic, weak) IBOutlet UIActivityIndicatorView *activityIndicator;

@property (nonatomic, weak) id <AAPLFilterViewControllerDelegate> delegate;

@end

@protocol AAPLFilterViewControllerDelegate <NSObject>

- (void)wasDismissed;

@end
```

[Next](PhotoHandoff-AAPLCustomCellBackground.h.md)[Previous](PhotoHandoff-AAPLDataSource.h.md)

