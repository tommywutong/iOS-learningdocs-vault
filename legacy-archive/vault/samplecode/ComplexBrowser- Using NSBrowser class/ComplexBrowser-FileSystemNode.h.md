---
title: 'ComplexBrowser: Using NSBrowser class'
apple_id: DTS40008829
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-04-07'
source_url: https://developer.apple.com/library/archive/samplecode/ComplexBrowser/Listings/ComplexBrowser_FileSystemNode_h.html
archived_at: '2026-07-18T03:04:06.883710Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ComplexBrowser: Using NSBrowser class](ComplexBrowser-%20Using%20NSBrowser%20class.md)


[Next](ComplexBrowser-PreviewViewController.m.md)[Previous](ComplexBrowser-FileSystemNode.m.md)

# ComplexBrowser/FileSystemNode.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An abstract wrapper node around the file system.
 */

@import Cocoa;

// This is a simple wrapper around the file system. Its main purpose is to cache children.
@interface FileSystemNode : NSObject

// The designated initializer
- (instancetype)initWithURL:(NSURL *)url NS_DESIGNATED_INITIALIZER;

@property (readonly) NSURL *URL;
@property (readonly, copy) NSString *displayName;
@property (readonly, strong) NSImage *icon;
@property (readonly, strong) NSArray *children;
@property (readonly) BOOL isDirectory;
@property (readonly) BOOL isPackage;
@property (readonly, strong) NSColor *labelColor;
@property (readonly) NSUInteger size;
@property (readonly, strong) NSString *formattedFileSize;
@property (readonly, strong) NSString *documentKind;
@property (readonly, strong) NSDate *creationDate;
@property (readonly, strong) NSDate *modificationDate;
@property (readonly, strong) NSDate *lastOpened;

- (void)invalidateChildren;

@end
```

[Next](ComplexBrowser-PreviewViewController.m.md)[Previous](ComplexBrowser-FileSystemNode.m.md)

