---
title: 'CloudCaptions: How integrate CloudKit into your application'
apple_id: TP40014732
resource_type: Sample Code
platform: iOS
topic: null
technology: CloudKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/CloudCaptions/Listings/CloudCaptions_AAPLPost_h.html
archived_at: '2026-07-18T03:03:30.582311Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudCaptions: How integrate CloudKit into your application](CloudCaptions-%20How%20integrate%20CloudKit%20into%20your%20application.md)


[Next](CloudCaptions-AAPLPostTableViewCell.m.md)[Previous](CloudCaptions-AAPLExistingImageCollectionView.h.md)

# CloudCaptions/AAPLPost.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Container model used to manage post records

 */

@import CloudKit;
#import "AAPLImage.h"

static NSString * const AAPLPostRecordType = @"Post";
static NSString * const AAPLPostTextKey = @"ImageText";
static NSString * const AAPLPostFontKey = @"Font";
static NSString * const AAPLPostImageRefKey = @"ImageRef";
static NSString * const AAPLPostTagsKey = @"Tags";

@interface AAPLPost : NSObject

- (instancetype) initWithRecord:(CKRecord *)postRecord NS_DESIGNATED_INITIALIZER;
- (void) loadImageWithKeys:(NSArray *)keys completion:(void(^)())updateBlock;

@property (strong, atomic) CKRecord *postRecord;
@property (strong, atomic) AAPLImage *imageRecord;

@end
```

[Next](CloudCaptions-AAPLPostTableViewCell.m.md)[Previous](CloudCaptions-AAPLExistingImageCollectionView.h.md)

