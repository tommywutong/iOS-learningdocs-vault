---
title: 'CloudCaptions: How integrate CloudKit into your application'
apple_id: TP40014732
resource_type: Sample Code
platform: iOS
topic: null
technology: CloudKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/CloudCaptions/Listings/CloudCaptions_AAPLPostManager_h.html
archived_at: '2026-07-18T03:03:30.349438Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudCaptions: How integrate CloudKit into your application](CloudCaptions-%20How%20integrate%20CloudKit%20into%20your%20application.md)


[Next](CloudCaptions-AAPLAppDelegate.h.md)[Previous](CloudCaptions-AAPLImage.h.md)

# CloudCaptions/AAPLPostManager.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Used by AAPLTableViewController to retrieve remote posts and stitch local posts into the tableview

 */

#define updateBy 10

@import Foundation;
@import UIKit;

@class AAPLPost;

@interface AAPLPostManager : NSObject

@property (strong, atomic) NSMutableArray *postCells;
@property (weak, atomic) UIRefreshControl *refreshControl;

- (instancetype) initWithReloadHandler:(void(^)(void))reload NS_DESIGNATED_INITIALIZER;
- (void) loadNewPostsWithAAPLPost:(AAPLPost *)post;
- (void) loadNewPosts;
- (void) loadBatch;
- (void) resetWithTagString:(NSString *)tags;

@end
```

[Next](CloudCaptions-AAPLAppDelegate.h.md)[Previous](CloudCaptions-AAPLImage.h.md)

