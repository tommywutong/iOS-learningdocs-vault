---
title: QuickLookDownloader
apple_id: DTS40009082
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: QuickLook
published: '2017-10-26'
source_url: https://developer.apple.com/library/archive/samplecode/QuickLookDownloader/Listings/README_md.html
archived_at: '2026-07-18T03:21:44.010956Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickLookDownloader](QuickLookDownloader.md)


[Next](QuickLookDownloader-AppDelegate.m.md)[Previous](QuickLookDownloader-main.m.md)

# README.md

```
# QuickLookDownloader

## Description

QuickLookDownloader manages file downloads from the internet, displaying thumbnail images in the download list and high-detail previews using the QLPreviewPanel class.  This application demonstrates the two methods for displaying Quick Look content inside your application.

DownloadItem.m shows how to asynchronously get the Quick Look thumbnail for a file.

AppDelegate.m shows how to open and close the Quick Look panel. The standard menu shortcut for the Quick Look panel is ⌘-Y but the user should also be able to use the space key.

MyDocument.m shows how to control and provide the delegate and data source of the Quick Look panel.

DownloadsTableView.m subclasses NSTableView to handle the space key and open the Quick Look panel.

## Further Reading

https://developer.apple.com/library/mac/documentation/Quartz/Reference/QLPreviewPanel_Class/Reference/Reference.html

## Runtime

Enter the URL of a file that's capable of being previewed, e.g. https://developer.apple.com/apple-touch-icon.png

Once the download is complete, observe how the standard document icon is replaced by a Quick Look thumbnail.
Select the file in the table and hit the space bar to show the document in the Quick Look preview panel.

## Requirements

### Build
OS X 10.12 SDK or later

### Runtime

OS X 10.10 or later

Copyright (C) 2009-2017 Apple Inc. All rights reserved.
```

[Next](QuickLookDownloader-AppDelegate.m.md)[Previous](QuickLookDownloader-main.m.md)

