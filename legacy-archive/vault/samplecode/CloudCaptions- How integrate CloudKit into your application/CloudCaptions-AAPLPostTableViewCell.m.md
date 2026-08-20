---
title: 'CloudCaptions: How integrate CloudKit into your application'
apple_id: TP40014732
resource_type: Sample Code
platform: iOS
topic: null
technology: CloudKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/CloudCaptions/Listings/CloudCaptions_AAPLPostTableViewCell_m.html
archived_at: '2026-07-18T03:03:30.534299Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudCaptions: How integrate CloudKit into your application](CloudCaptions-%20How%20integrate%20CloudKit%20into%20your%20application.md)


[Next](CloudCaptions-AAPLPost.m.md)[Previous](CloudCaptions-AAPLPost.h.md)

# CloudCaptions/AAPLPostTableViewCell.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 */

#import "AAPLPostTableViewCell.h"
#import "AAPLPost.h"

@interface AAPLPostTableViewCell ()

@property (strong, nonatomic) NSString *fontName;
@property (strong, nonatomic) IBOutlet UILabel *textLabelInCell;
@property (strong, nonatomic) IBOutlet UIImageView *imageViewInCell;
@property (strong, nonatomic) IBOutlet UIActivityIndicatorView *activityIndicator;

@end


#pragma mark -

@implementation AAPLPostTableViewCell
- (void)layoutSubviews
{
    [super layoutSubviews];
    UIFont *labelFont = [UIFont fontWithName:self.fontName size:24];
    [self.textLabelInCell setFont:labelFont];
}

- (void) displayInfoForPost:(AAPLPost *)post
{
    // Sets how the cell appears based on the AAPLPost passed in
    [self.activityIndicator startAnimating];
    self.imageViewInCell.image = [post.imageRecord fullImage];

    self.fontName = post.postRecord[AAPLPostFontKey];
    self.textLabelInCell.text = post.postRecord[AAPLPostTextKey];
}

@end
```

[Next](CloudCaptions-AAPLPost.m.md)[Previous](CloudCaptions-AAPLPost.h.md)

