---
title: QuickLookDownloader
apple_id: DTS40009082
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: QuickLook
published: '2017-10-26'
source_url: https://developer.apple.com/library/archive/samplecode/QuickLookDownloader/Listings/QuickLookDownloader_DownloadsTableView_m.html
archived_at: '2026-07-18T03:21:43.750948Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickLookDownloader](QuickLookDownloader.md)


[Next](QuickLookDownloader-DownloadCell.h.md)[Previous](QuickLookDownloader-DownloadCell.m.md)

# QuickLookDownloader/DownloadsTableView.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 DownloadsTableView overrides NSTableView to support space bar to open Quick Look panel.
 */

#import "DownloadsTableView.h"
#import "AppDelegate.h"

@implementation DownloadsTableView

- (void)keyDown:(NSEvent *)theEvent
{
    NSString *key = [theEvent charactersIgnoringModifiers];
    if ([key isEqual:@" "]) // Space key opens the preview panel.
    {
        AppDelegate *appDelegate = [NSApp delegate];
        [appDelegate togglePreviewPanel:self];
    }
    else
    {
        [super keyDown:theEvent];
    }
}

@end
```

[Next](QuickLookDownloader-DownloadCell.h.md)[Previous](QuickLookDownloader-DownloadCell.m.md)

