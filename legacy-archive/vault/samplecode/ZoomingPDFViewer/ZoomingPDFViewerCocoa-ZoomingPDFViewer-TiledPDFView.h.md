---
title: ZoomingPDFViewer
apple_id: DTS40010281
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: CoreGraphics
published: '2017-04-27'
source_url: https://developer.apple.com/library/archive/samplecode/ZoomingPDFViewer/Listings/ZoomingPDFViewerCocoa_ZoomingPDFViewer_TiledPDFView_h.html
archived_at: '2026-07-18T03:28:44.976214Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZoomingPDFViewer](ZoomingPDFViewer.md)


[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-DataViewController.m.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-TiledPDFScrollView.m.md)

# ZoomingPDFViewerCocoa/ZoomingPDFViewer/TiledPDFView.h

```objc
/*
Copyright (C) 2017 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
This view is backed by a CATiledLayer into which the PDF page is rendered into.
*/


#import <UIKit/UIKit.h>


@interface TiledPDFView: UIView


@property CGPDFPageRef pdfPage;

@property CGFloat myScale;


- (id)initWithFrame:(CGRect)frame scale:(CGFloat)scale;
- (void)dealloc;
+ (Class)layerClass;
- (void)setPage:(CGPDFPageRef)newPage;
- (void)drawLayer:(CALayer*)layer inContext:(CGContextRef)context;

@end
```

[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-DataViewController.m.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-TiledPDFScrollView.m.md)

