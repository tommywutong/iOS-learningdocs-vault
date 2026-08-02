---
title: 'ComplexBrowser: Using NSBrowser class'
apple_id: DTS40008829
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-04-07'
source_url: https://developer.apple.com/library/archive/samplecode/ComplexBrowser/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:04:07.213764Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ComplexBrowser: Using NSBrowser class](ComplexBrowser-%20Using%20NSBrowser%20class.md)


[Next](ComplexBrowser-AppController.h.md)[Previous](ComplexBrowser-main.m.md)

# ReadMe.md

```
# ComplexBrowser

## Description

ComplexBrowser is a more advanced version of SimpleCocoaBrowser. It extends on the SimpleCocoaBrowser example by adding more customization. It only supports the new 10.6 item-based browser API, but it is possible to use the same concepts with the old API. It demonstrates header views, preview views, custom cells, and drag and drop.

AppController.h/.m

The AppController class lives in the MainMenu.xib. It is set as the delegate for the main NSApplication instance, and the delegate for the NSBrowser. It also has a single outlet set to the browser.  This class contains the root delegate implementation to provide data for the browser, and implements drag and drop.

FileSystemNode.h/.m

This class is a simple wrapper around the file system. Its main purpose is to cache the children for a given NSURL. We do this in order to get a consistent children count. 

FileSystemBrowserCell.h/.m

A simple custom cell that draws the file system icon at the appropriate location.

## Requirements

### Build

Xcode 7.1, OS X 10.10 SDK or later

### Runtime

OS X 10.10 or later

Copyright (C) 2009-2015 Apple Inc. All rights reserved.
```

[Next](ComplexBrowser-AppController.h.md)[Previous](ComplexBrowser-main.m.md)

