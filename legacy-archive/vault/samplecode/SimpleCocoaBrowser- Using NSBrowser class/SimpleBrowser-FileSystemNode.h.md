---
title: 'SimpleCocoaBrowser: Using NSBrowser class'
apple_id: DTS40008872
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-04-29'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleCocoaBrowser/Listings/SimpleBrowser_FileSystemNode_h.html
archived_at: '2026-07-18T03:23:57.339181Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleCocoaBrowser: Using NSBrowser class](SimpleCocoaBrowser-%20Using%20NSBrowser%20class.md)


[Next](ReadMe.md.md)[Previous](SimpleBrowser-FileSystemNode.m.md)

# SimpleBrowser/FileSystemNode.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An abstract wrapper node around the file system.
 */

@import Cocoa;

// This is a simple wrapper around the file system. Its main purpose is to cache children.
@interface FileSystemNode : NSObject <NSToolbarDelegate>

// The designated initializer
- (id)initWithURL:(NSURL *)url NS_DESIGNATED_INITIALIZER;

@property(readonly) NSURL *URL;
@property(readonly, copy) NSString *displayName;
@property(readonly, strong) NSImage *icon;
@property(readonly, strong) NSArray *children;
@property(readonly) BOOL isDirectory;
@property(readonly) BOOL isPackage;
@property(readonly, strong) NSColor *labelColor;

- (void)invalidateChildren;

@end
```

[Next](ReadMe.md.md)[Previous](SimpleBrowser-FileSystemNode.m.md)

