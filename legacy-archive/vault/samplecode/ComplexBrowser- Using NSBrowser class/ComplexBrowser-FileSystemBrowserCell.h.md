---
title: 'ComplexBrowser: Using NSBrowser class'
apple_id: DTS40008829
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-04-07'
source_url: https://developer.apple.com/library/archive/samplecode/ComplexBrowser/Listings/ComplexBrowser_FileSystemBrowserCell_h.html
archived_at: '2026-07-18T03:04:06.769388Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ComplexBrowser: Using NSBrowser class](ComplexBrowser-%20Using%20NSBrowser%20class.md)


[Next](ComplexBrowser-PreviewViewController.h.md)[Previous](ComplexBrowser-PreviewViewController.m.md)

# ComplexBrowser/FileSystemBrowserCell.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A cell that can draw an image/icon and a label color.
 */

@import Cocoa;

@interface FileSystemBrowserCell : NSTextFieldCell

@property (strong) NSImage *image;
@property (strong) NSColor *labelColor;

@end
```

[Next](ComplexBrowser-PreviewViewController.h.md)[Previous](ComplexBrowser-PreviewViewController.m.md)

