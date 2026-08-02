---
title: QuickLookDownloader
apple_id: DTS40009082
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: QuickLook
published: '2017-10-26'
source_url: https://developer.apple.com/library/archive/samplecode/QuickLookDownloader/Listings/QuickLookDownloader_AppDelegate_m.html
archived_at: '2026-07-18T03:21:43.488013Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickLookDownloader](QuickLookDownloader.md)


[Next](QuickLookDownloader-DownloadCell.m.md)[Previous](README.md.md)

# QuickLookDownloader/AppDelegate.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Application delegate class ; opens/closes the Quick Look panel.
 */

@import Cocoa;
@import Quartz;  // for QLPreviewPanel

#import "AppDelegate.h"

@implementation AppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)notification
{
    if ([[NSDocumentController sharedDocumentController] documents].count == 0)
    {
        // open a new document window if there are none open
        [[NSDocumentController sharedDocumentController] newDocument:self];
    }
}

- (IBAction)togglePreviewPanel:(id)previewPanel
{
    if ([QLPreviewPanel sharedPreviewPanelExists] && [[QLPreviewPanel sharedPreviewPanel] isVisible])
    {
        [[QLPreviewPanel sharedPreviewPanel] orderOut:nil];
    }
    else
    {
        [[QLPreviewPanel sharedPreviewPanel] makeKeyAndOrderFront:nil];
    }
}

- (BOOL)validateMenuItem:(NSMenuItem *)menuItem
{
    SEL action = [menuItem action];
    if (action == @selector(togglePreviewPanel:))
    {
        if ([QLPreviewPanel sharedPreviewPanelExists] && [[QLPreviewPanel sharedPreviewPanel] isVisible])
        {
            [menuItem setTitle:NSLocalizedString(@"Close Quick Look panel", "")];
        }
        else
        {
            [menuItem setTitle:NSLocalizedString(@"Open Quick Look panel", "")];
        }
        return YES;
    }
    return NO;
}

@end
```

[Next](QuickLookDownloader-DownloadCell.m.md)[Previous](README.md.md)

