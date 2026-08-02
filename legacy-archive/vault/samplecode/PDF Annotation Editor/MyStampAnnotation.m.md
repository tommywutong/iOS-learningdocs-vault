---
title: PDF Annotation Editor
apple_id: DTS10004035
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/samplecode/PDFAnnotationEditor/Listings/MyStampAnnotation_m.html
archived_at: '2026-07-18T03:18:24.940692Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PDF Annotation Editor](PDF%20Annotation%20Editor.md)


[Next](README.md.md)[Previous](MyWindowController.h.md)

# MyStampAnnotation.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This file demonstrates how to subclass -[PDFAnnotation drawWithBox:inContext]
         in order to render our own custom drawing for the MyStampAnnotation subclass
         of PDFAnnotation.
*/ 

// =====================================================================================================================
//  MyStampAnnotation.m
// =====================================================================================================================


#import "MyStampAnnotation.h"


@implementation MyStampAnnotation : PDFAnnotation
// =================================================================================================== MyStampAnnotation
// --------------------------------------------------------------------------------------------------------- drawWithBox

- (void) drawWithBox: (PDFDisplayBox) box
{
    NSImage     *stampImage;

    // Sanity check.
    if( (box < kPDFDisplayBoxMediaBox) || (box > kPDFDisplayBoxArtBox) )
        return;

    // Save.
    [NSGraphicsContext saveGraphicsState];

    // Tranform.
    [self transformContextForBox: box];

    [[NSBezierPath bezierPathWithRect: [self bounds]] setClip];

    // Draw image.
    stampImage = [NSImage imageNamed: @"MyStamp"];
    [[stampImage bestRepresentationForDevice: NULL] drawInRect: [self bounds]];

    // Restore.
    [NSGraphicsContext restoreGraphicsState];
}

// ---------------------------------------------------------------------------------------------- transformContextForBox

- (void) transformContextForBox: (PDFDisplayBox) box
{
    NSAffineTransform   *transform;
    NSRect              boxRect;
    NSInteger           rotation;

    if ([self page] == NULL)
        return;

    // Get the page bounds for box.
    boxRect = [[self page] boundsForBox: box];

    // Identity.
    transform = [NSAffineTransform transform];

    // Handle rotation.
    rotation = [[self page] rotation];
    switch (rotation)
    {
        case 90:
        [transform rotateByDegrees: -90];
        [transform translateXBy: -boxRect.size.width yBy: 0.0];
        break;

        case 180:
        [transform rotateByDegrees: 180];
        [transform translateXBy: -boxRect.size.height yBy: -boxRect.size.width];
        break;

        case 270:
        [transform rotateByDegrees: 90];
        [transform translateXBy: 0.0 yBy: -boxRect.size.height];
        break;
    }

    // Handle origin.
    [transform translateXBy: -boxRect.origin.x yBy: -boxRect.origin.y];

    // Concatenate.
    [transform concat];
}

@end
```

[Next](README.md.md)[Previous](MyWindowController.h.md)

