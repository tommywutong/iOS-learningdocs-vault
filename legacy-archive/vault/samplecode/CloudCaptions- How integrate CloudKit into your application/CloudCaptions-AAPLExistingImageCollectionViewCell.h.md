---
title: 'CloudCaptions: How integrate CloudKit into your application'
apple_id: TP40014732
resource_type: Sample Code
platform: iOS
topic: null
technology: CloudKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/CloudCaptions/Listings/CloudCaptions_AAPLExistingImageCollectionViewCell_h.html
archived_at: '2026-07-18T03:03:29.913589Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudCaptions: How integrate CloudKit into your application](CloudCaptions-%20How%20integrate%20CloudKit%20into%20your%20application.md)


[Next](CloudCaptions-AAPLSubscriptionController.m.md)[Previous](CloudCaptions-main.m.md)

# CloudCaptions/AAPLExistingImageCollectionViewCell.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

 Custom collection view cell object used to display the thumbnail for the AAPLImage assigned to it

 */

@import UIKit;
#import "AAPLImage.h"

@interface AAPLExistingImageCollectionViewCell : UICollectionViewCell

@property (strong, atomic) IBOutlet UIImageView *thumbnailImage;
- (void) setLoading:(BOOL)loading;

@end
```

[Next](CloudCaptions-AAPLSubscriptionController.m.md)[Previous](CloudCaptions-main.m.md)

