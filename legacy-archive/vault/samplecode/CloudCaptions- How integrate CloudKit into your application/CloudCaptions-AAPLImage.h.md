---
title: 'CloudCaptions: How integrate CloudKit into your application'
apple_id: TP40014732
resource_type: Sample Code
platform: iOS
topic: null
technology: CloudKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/CloudCaptions/Listings/CloudCaptions_AAPLImage_h.html
archived_at: '2026-07-18T03:03:30.256413Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudCaptions: How integrate CloudKit into your application](CloudCaptions-%20How%20integrate%20CloudKit%20into%20your%20application.md)


[Next](CloudCaptions-AAPLPostManager.h.md)[Previous](CloudCaptions-AAPLSubscriptionController.h.md)

# CloudCaptions/AAPLImage.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Container model used to manage Image records

 */

@import UIKit;
@import CloudKit;

static NSString * const AAPLImageRecordType = @"Image";
static NSString * const AAPLImageThumbnailKey = @"Thumb";
static NSString * const AAPLImageFullsizeKey = @"Full";

@interface AAPLImage : NSObject

- (instancetype) initWithImage:(UIImage *)image;
- (instancetype) initWithRecord:(CKRecord *)record;

@property (readonly, getter=isOnServer) BOOL onServer;
@property (strong, readonly, atomic) CKRecord *record;
@property (strong, readonly, atomic) UIImage *fullImage;
@property (strong, readonly, atomic) UIImage *thumbnail;

@end
```

[Next](CloudCaptions-AAPLPostManager.h.md)[Previous](CloudCaptions-AAPLSubscriptionController.h.md)

