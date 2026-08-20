---
title: 'PhotoHandoff: Implementing NSUserActivity to hand off user actions'
apple_id: TP40014785
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoHandoff/Listings/PhotoHandoff_AAPLCell_h.html
archived_at: '2026-07-18T03:18:50.211202Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoHandoff: Implementing NSUserActivity to hand off user actions](PhotoHandoff-%20Implementing%20NSUserActivity%20to%20hand%20off%20user%20actions.md)


[Next](PhotoHandoff-AAPLCell.m.md)[Previous](PhotoHandoff-AAPLFilterViewController.m.md)

# PhotoHandoff/AAPLCell.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Custom collection view cell for displaying image and its label.

 */

#import <UIKit/UIKit.h>

@interface AAPLCell : UICollectionViewCell

@property (strong, nonatomic) IBOutlet UIImageView *image;
@property (strong, nonatomic) IBOutlet UILabel *label;

@end
```

[Next](PhotoHandoff-AAPLCell.m.md)[Previous](PhotoHandoff-AAPLFilterViewController.m.md)

