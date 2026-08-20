---
title: 'ComplexBrowser: Using NSBrowser class'
apple_id: DTS40008829
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-04-07'
source_url: https://developer.apple.com/library/archive/samplecode/ComplexBrowser/Listings/ComplexBrowser_PreviewViewController_m.html
archived_at: '2026-07-18T03:04:07.074813Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ComplexBrowser: Using NSBrowser class](ComplexBrowser-%20Using%20NSBrowser%20class.md)


[Next](ComplexBrowser-FileSystemBrowserCell.h.md)[Previous](ComplexBrowser-FileSystemNode.h.md)

# ComplexBrowser/PreviewViewController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View Controller subclass used for our preview pane in NSBrowser.
 */

#import "PreviewViewController.h"
#import "FileSystemNode.h"

@implementation PreviewViewController

- (void)mouseDown:(NSEvent *)theEvent {

    [super mouseDown:theEvent];

    // check for double click
    if ([theEvent clickCount] > 1) {
        // Find the clicked item and open it in Finder
        FileSystemNode *node = self.representedObject;
        [[NSWorkspace sharedWorkspace] openFile:node.URL.path];
    }
}

@end
```

[Next](ComplexBrowser-FileSystemBrowserCell.h.md)[Previous](ComplexBrowser-FileSystemNode.h.md)

