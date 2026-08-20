---
title: PDF Annotation Editor
apple_id: DTS10004035
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/samplecode/PDFAnnotationEditor/Listings/MyStampAnnotation_h.html
archived_at: '2026-07-18T03:18:24.907043Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PDF Annotation Editor](PDF%20Annotation%20Editor.md)


[Next](PDFViewEdit.m.md)[Previous](README.md.md)

# MyStampAnnotation.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 MyStampAnnotation represents a custom subclass of PDFAnnotation for the stamp
         annotation subtype. PDFKit does not support any native rendering for stamp
         annotations, but we can subclass PDFAnnotation in order to override
         -[PDFAnnotation drawWithBox:inContext:] to render the desired UI for
         this specific annotation subtype. See the implementation file of this class
         for more details.
*/ 

// =====================================================================================================================
//  MyStampAnnotation.h
// =====================================================================================================================


#import <Quartz/Quartz.h>


@interface MyStampAnnotation : PDFAnnotation
{
}

- (void) transformContextForBox: (PDFDisplayBox) box;
@end
```

[Next](PDFViewEdit.m.md)[Previous](README.md.md)

