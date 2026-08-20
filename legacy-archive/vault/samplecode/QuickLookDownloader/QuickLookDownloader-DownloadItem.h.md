---
title: QuickLookDownloader
apple_id: DTS40009082
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: QuickLook
published: '2017-10-26'
source_url: https://developer.apple.com/library/archive/samplecode/QuickLookDownloader/Listings/QuickLookDownloader_DownloadItem_h.html
archived_at: '2026-07-18T03:21:43.615085Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickLookDownloader](QuickLookDownloader.md)


[Next](QuickLookDownloader-DownloadsTableView.h.md)[Previous](QuickLookDownloader-AppDelegate.h.md)

# QuickLookDownloader/DownloadItem.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 DownloadItem stores information of a downloaded item used by MyDocument.
*/

@import Cocoa;

@interface DownloadItem : NSObject <NSTableViewDelegate, NSTableViewDataSource>

- (id)initWithOriginalURL:(NSURL *)downloadURL fileURL:(NSURL *)onDiskURL;
- (id)initWithSavedPropertyList:(id)propertyList;

@property (readonly) NSURL *originalURL;
@property (readonly) NSURL *resolvedFileURL;

@property (weak, readonly) NSString *displayName;
@property (nonatomic, strong) NSImage *iconImage;

@property (unsafe_unretained, readonly) id propertyListForSaving;

@end
```

[Next](QuickLookDownloader-DownloadsTableView.h.md)[Previous](QuickLookDownloader-AppDelegate.h.md)

