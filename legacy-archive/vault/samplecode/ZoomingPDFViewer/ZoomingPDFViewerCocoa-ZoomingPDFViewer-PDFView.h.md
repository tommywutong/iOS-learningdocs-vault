---
title: ZoomingPDFViewer
apple_id: DTS40010281
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: CoreGraphics
published: '2017-04-27'
source_url: https://developer.apple.com/library/archive/samplecode/ZoomingPDFViewer/Listings/ZoomingPDFViewerCocoa_ZoomingPDFViewer_PDFView_h.html
archived_at: '2026-07-18T03:28:44.673780Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZoomingPDFViewer](ZoomingPDFViewer.md)


[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-DataViewController.h.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-RootViewController.m.md)

# ZoomingPDFViewerCocoa/ZoomingPDFViewer/PDFView.h

```objc
//
//  PDFView.h
//  PageBasedPDF
//
//  Created by Bob Thomas on 7/15/13.
//  Copyright (c) 2013 Apple DTS. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface PDFView : UIView

@property CGPDFDocumentRef pdf;
@property CGPDFPageRef page;
@property int pageNumber;
@property CGFloat myScale;

@end
```

[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-DataViewController.h.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-RootViewController.m.md)

