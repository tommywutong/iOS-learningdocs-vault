---
title: 'CloudCaptions: How integrate CloudKit into your application'
apple_id: TP40014732
resource_type: Sample Code
platform: iOS
topic: null
technology: CloudKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/CloudCaptions/Listings/CloudCaptions_AAPLExistingImageCollectionView_h.html
archived_at: '2026-07-18T03:03:30.002797Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudCaptions: How integrate CloudKit into your application](CloudCaptions-%20How%20integrate%20CloudKit%20into%20your%20application.md)


[Next](CloudCaptions-AAPLPost.h.md)[Previous](CloudCaptions-AAPLSubmitPostViewController.h.md)

# CloudCaptions/AAPLExistingImageCollectionView.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Collection view that creates an AAPLExistingImageCollectionViewCell for each record added to its imageRecords array


 */

@import CloudKit;
@import UIKit;

@interface AAPLExistingImageCollectionView : UICollectionView <UICollectionViewDataSource>

@property (nonatomic, readonly) NSUInteger count;
- (void) addImageFromRecord:(CKRecord *)toAdd;
- (CKRecordID *) getRecordIDAtIndex:(NSIndexPath *)index;
- (void) cellAtIndex:(NSIndexPath *)index isLoading:(BOOL)loading;

@end
```

[Next](CloudCaptions-AAPLPost.h.md)[Previous](CloudCaptions-AAPLSubmitPostViewController.h.md)

