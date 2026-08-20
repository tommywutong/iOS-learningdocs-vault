---
title: 'SimpleCocoaBrowser: Using NSBrowser class'
apple_id: DTS40008872
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-04-29'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleCocoaBrowser/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:23:57.203061Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleCocoaBrowser: Using NSBrowser class](SimpleCocoaBrowser-%20Using%20NSBrowser%20class.md)


[Next](LICENSE.txt.md)[Previous](SimpleBrowser-FileSystemNode.h.md)

# ReadMe.md

```
# SimpleCocoaBrowser

## Description

SimpleCocoaBrowser is a very simple example of how to create a basic NSBrowser delegate implementation. See the ComplexBrowser example for a more interesting example, and to see the use of a custom cell.  As a delegate it utilizes NSBrowser’s "item-based" API.

AppController.h/.m

The AppController class lives in the MainMenu.xib. It is set as the delegate for the main NSApplication instance, and the delegate for the NSBrowser. It also has a single outlet set to the browser.

FileSystemNode.h/.m

This class is a simple wrapper around the file system. Its main purpose is to cache the children for a given NSURL. We do this in order to get a consistent children count. 


## Requirements

### Build

Xcode 7.1, OS X 10.10 SDK or later

### Runtime

OS X 10.10 or later

Copyright (C) 2009-2016 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](SimpleBrowser-FileSystemNode.h.md)

