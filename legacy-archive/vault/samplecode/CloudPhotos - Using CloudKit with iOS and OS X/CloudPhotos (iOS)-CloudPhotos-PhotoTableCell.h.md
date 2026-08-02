---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__iOS__CloudPhotos_PhotoTableCell_h.html
archived_at: '2026-07-18T03:03:33.556855Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28iOS%29-CloudPhotos-APLPhotoViewController.m.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-CloudPhoto.h.md)

# CloudPhotos (iOS)/CloudPhotos/PhotoTableCell.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom UITableViewCell for displaying photo information in the main table view.
 */

@import UIKit;

@class CloudPhoto;

@interface PhotoTableCell : UITableViewCell

@property (nonatomic, strong) CloudPhoto *photo;

@end
```

[Next](CloudPhotos%20%28iOS%29-CloudPhotos-APLPhotoViewController.m.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-CloudPhoto.h.md)

