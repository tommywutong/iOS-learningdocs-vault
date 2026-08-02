---
title: QuickLookDownloader
apple_id: DTS40009082
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: QuickLook
published: '2017-10-26'
source_url: https://developer.apple.com/library/archive/samplecode/QuickLookDownloader/Listings/QuickLookDownloader_DownloadCell_h.html
archived_at: '2026-07-18T03:21:43.537987Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickLookDownloader](QuickLookDownloader.md)


[Next](QuickLookDownloader-MyDocument.h.md)[Previous](QuickLookDownloader-DownloadsTableView.m.md)

# QuickLookDownloader/DownloadCell.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 DownloadCell can display a title, an icon and a subtitle.
*/

@import Cocoa;

#define TEXT_SIZE 12.0

@interface DownloadCell : NSTextFieldCell

@property (copy) NSURL *originalURL;

@end
```

[Next](QuickLookDownloader-MyDocument.h.md)[Previous](QuickLookDownloader-DownloadsTableView.m.md)

