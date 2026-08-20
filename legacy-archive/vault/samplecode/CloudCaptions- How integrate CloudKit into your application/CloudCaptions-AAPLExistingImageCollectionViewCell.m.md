---
title: 'CloudCaptions: How integrate CloudKit into your application'
apple_id: TP40014732
resource_type: Sample Code
platform: iOS
topic: null
technology: CloudKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/CloudCaptions/Listings/CloudCaptions_AAPLExistingImageCollectionViewCell_m.html
archived_at: '2026-07-18T03:03:29.956811Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudCaptions: How integrate CloudKit into your application](CloudCaptions-%20How%20integrate%20CloudKit%20into%20your%20application.md)


[Next](CloudCaptions-AAPLSubmitPostViewController.m.md)[Previous](CloudCaptions-AAPLPostTableViewCell.h.md)

# CloudCaptions/AAPLExistingImageCollectionViewCell.m

```objc
/*
Copyright (C) 2014 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

 */

#import "AAPLExistingImageCollectionViewCell.h"

@interface AAPLExistingImageCollectionViewCell ()

@property (strong, nonatomic) IBOutlet UIActivityIndicatorView *loadingIndicator;
@property (strong, atomic) UIVisualEffectView *blurSubview;

@end


#pragma mark -

@implementation AAPLExistingImageCollectionViewCell

- (void) setLoading:(BOOL)loading
{
    if(loading)
    {
        [self.loadingIndicator startAnimating];

        UIBlurEffect *blurEffect = [UIBlurEffect effectWithStyle:UIBlurEffectStyleLight];
        self.blurSubview = [[UIVisualEffectView alloc] initWithEffect:blurEffect];
        self.blurSubview.frame = self.thumbnailImage.frame;
        [self.thumbnailImage addSubview:self.blurSubview];
    }
    else
    {
        if(self.blurSubview)
        {
            [self.blurSubview removeFromSuperview];
            self.blurSubview = nil;
        }
        [self.loadingIndicator stopAnimating];
    }
}

@end
```

[Next](CloudCaptions-AAPLSubmitPostViewController.m.md)[Previous](CloudCaptions-AAPLPostTableViewCell.h.md)

