---
title: ZoomingPDFViewer
apple_id: DTS40010281
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: CoreGraphics
published: '2017-04-27'
source_url: https://developer.apple.com/library/archive/samplecode/ZoomingPDFViewer/Listings/ZoomingPDFViewerCocoa_ZoomingPDFViewer_DataViewController_h.html
archived_at: '2026-07-18T03:28:44.482327Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZoomingPDFViewer](ZoomingPDFViewer.md)


[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-ModelController.h.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-PDFView.h.md)

# ZoomingPDFViewerCocoa/ZoomingPDFViewer/DataViewController.h

```objc
/*
Copyright (C) 2017 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The app's view controller which presents viewable content.
*/



#import <UIKit/UIKit.h>
#import <QuartzCore/QuartzCore.h>



@class TiledPDFScrollView;



@interface DataViewController: UIViewController


@property (strong) IBOutlet TiledPDFScrollView *scrollView;

@property CGPDFDocumentRef pdf;

@property CGPDFPageRef page;

@property int pageNumber;

@property CGFloat myScale;



- (void)dealloc;

- (void)viewDidLoad;

- (void)viewDidLayoutSubviews;

- (void)viewWillTransitionToSize:(CGSize)size withTransitionCoordinator:(id <UIViewControllerTransitionCoordinator>)coordinator;

- (void)restoreScale;

@end
```

[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-ModelController.h.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-PDFView.h.md)

