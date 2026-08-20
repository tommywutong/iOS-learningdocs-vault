---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_NSBitmap_h.html
archived_at: '2026-07-18T03:06:08.551332Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-NSTextFile.mm.md)[Previous](Sources-GLShader.mm.md)

# Sources/NSBitmap.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating a bitmap from an image.
 */

#import <Cocoa/Cocoa.h>

@interface NSBitmap : NSObject

- (nullable instancetype) initWithImage:(nullable NSImage *)image;

+ (nullable instancetype) bitmapWithImage:(nullable NSImage *)image;

@property (nonatomic, readonly, nullable) NSBitmapImageRep* bitmap;

@end
```

[Next](Sources-NSTextFile.mm.md)[Previous](Sources-GLShader.mm.md)

