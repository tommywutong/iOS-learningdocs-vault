---
title: Packaged Document for OS X
apple_id: DTS40012955
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/PackagedDocument/Listings/PackagedDocument_ImageView_h.html
archived_at: '2026-07-18T03:18:44.774155Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for OS X](Packaged%20Document%20for%20OS%20X.md)


[Next](PackagedDocument-ImageView.m.md)[Previous](PackagedDocument-MyTextPictDocument.h.md)

# PackagedDocument/ImageView.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom NSImageView for intercepting delete/cut/paste operations.
 */

#import <Cocoa/Cocoa.h>

@protocol ImageViewDelegate;

@interface ImageView : NSImageView

@property (weak) id<ImageViewDelegate> delegate;

@end

@protocol ImageViewDelegate <NSObject>

@required
- (void)imageView:(ImageView *)imageView didChangeImage:(NSImage *)image;

@end
```

[Next](PackagedDocument-ImageView.m.md)[Previous](PackagedDocument-MyTextPictDocument.h.md)

