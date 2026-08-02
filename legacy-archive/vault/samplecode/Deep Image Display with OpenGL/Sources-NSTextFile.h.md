---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_NSTextFile_h.html
archived_at: '2026-07-18T03:06:08.644385Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-Quad2D.fs.md)[Previous](Sources-GLQuad.mm.md)

# Sources/NSTextFile.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for loading a text file.
 */

#import <Cocoa/Cocoa.h>

@interface NSTextFile : NSObject

// Load a text file located at a URL
- (nullable instancetype) initWithURL:(nullable NSURL *)url;

+ (nullable instancetype) textWithURL:(nullable NSURL *)url;

// Load a text file located at an absolute path
- (nullable instancetype) initWithFile:(nullable NSString *)path;

+ (nullable instancetype) textWithFile:(nullable NSString *)path;

// Load a text file in application's bundle
- (nullable instancetype) initWithResource:(nullable NSString *)name
                                       ext:(nullable NSString *)ext;

+ (nullable instancetype) textWithResource:(nullable NSString *)name
                                       ext:(nullable NSString *)ext;

// Text file content
@property (nonatomic, readonly, nullable) const char* source;

@end
```

[Next](Sources-Quad2D.fs.md)[Previous](Sources-GLQuad.mm.md)

