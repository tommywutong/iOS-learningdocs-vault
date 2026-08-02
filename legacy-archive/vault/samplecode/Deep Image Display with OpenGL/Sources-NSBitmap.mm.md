---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_NSBitmap_mm.html
archived_at: '2026-07-18T03:06:08.600836Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](LICENSE.txt.md)[Previous](Sources-Quad2D.vs.md)

# Sources/NSBitmap.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating a bitmap from an image.
 */

#import "NSBitmap.h"

typedef NSArray<NSImageRep *>  NSImageRepArray;

@implementation NSBitmap
{
@private
    NSBitmapImageRep* _bitmap;
}

- (NSBitmapImageRep *) _bitmapImageRep:(nullable NSImage *)image
{
    if(image)
    {
        NSImageRepArray* reps = image.representations;

        if(reps)
        {
            NSImageRep* rep = nil;

            for(rep in reps)
            {
                if([rep isKindOfClass:[NSBitmapImageRep class]])
                {
                    return static_cast<NSBitmapImageRep *>(rep);
                } // if
            } // for
        } // if
    } // if

    return nil;
} // _bitmapImageRep

- (nullable instancetype) initWithImage:(nullable NSImage *)image
{
    self = [super init];

    if(self)
    {
        _bitmap = [[self _bitmapImageRep:image] retain];
    } // if

    return self;
} // initWithImage

+ (nullable instancetype) bitmapWithImage:(nullable NSImage *)image
{
    return [[[NSBitmap allocWithZone:[self zone]] initWithImage:image] autorelease];
} // bitmapWithImage

- (void) dealloc
{
    if(_bitmap)
    {
        [_bitmap release];
    } // if

    [super dealloc];
} // dealloc

@end
```

[Next](LICENSE.txt.md)[Previous](Sources-Quad2D.vs.md)

