---
title: Packaged Document for OS X
apple_id: DTS40012955
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/PackagedDocument/Listings/PackagedDocument_MyTextPictDocument_h.html
archived_at: '2026-07-18T03:18:44.915513Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for OS X](Packaged%20Document%20for%20OS%20X.md)


[Next](PackagedDocument-ImageView.h.md)[Previous](PackagedDocument-ViewController.m.md)

# PackagedDocument/MyTextPictDocument.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The NSDocument subclass for reading/writing it data and connecting with iCloud.
 */

#import <Cocoa/Cocoa.h>

@interface MyTextPictDocument : NSDocument

@property (strong) NSImage *image;

- (void)updateTextView:(NSTextView *)textView;
- (void)updateImageView:(NSImageView *)imageView;

- (void)updateImageModel:(NSImage *)image;
- (void)updateTextModel:(NSString *)text;

@end
```

[Next](PackagedDocument-ImageView.h.md)[Previous](PackagedDocument-ViewController.m.md)

