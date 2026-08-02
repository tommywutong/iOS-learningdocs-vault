---
title: ZoomingPDFViewer
apple_id: DTS40010281
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: CoreGraphics
published: '2017-04-27'
source_url: https://developer.apple.com/library/archive/samplecode/ZoomingPDFViewer/Listings/ZoomingPDFViewerCocoa_ZoomingPDFViewer_TiledPDFView_m.html
archived_at: '2026-07-18T03:28:45.070186Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZoomingPDFViewer](ZoomingPDFViewer.md)


[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-PDFView.m.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-ModelController.h.md)

# ZoomingPDFViewerCocoa/ZoomingPDFViewer/TiledPDFView.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This view is backed by a CATiledLayer into which the PDF page is rendered into.
 */



#import "TiledPDFView.h"
#import <QuartzCore/QuartzCore.h>



@implementation TiledPDFView



// Create a new TiledPDFView with the desired frame and scale.
- (id)initWithFrame:(CGRect)frame scale:(CGFloat)scale
{
    self = [super initWithFrame:frame];
    if ( self ) {

        CATiledLayer *tiledLayer = (CATiledLayer *)[self layer];
        /*
         levelsOfDetail and levelsOfDetailBias determine how the layer is rendered at different zoom levels. This only matters while the view is zooming, because once the the view is done zooming a new TiledPDFView is created at the correct size and scale.
         */
        tiledLayer.levelsOfDetail = 4;
        tiledLayer.levelsOfDetailBias = 3;
        tiledLayer.tileSize = CGSizeMake(512.0, 512.0);
        self.myScale = scale;
        self.layer.borderColor = [UIColor lightGrayColor].CGColor;
        self.layer.borderWidth = 5;
    }
    return self;
}



// Clean up.
- (void)dealloc
{
    if ( self.pdfPage != NULL ) CGPDFPageRelease( self.pdfPage );
}



// The layer's class should be CATiledLayer.
+ (Class)layerClass
{
    return [CATiledLayer class];
}



// Set the CGPDFPageRef for the view.
- (void)setPage:(CGPDFPageRef)newPage
{
    if ( self.pdfPage != NULL ) CGPDFPageRelease( self.pdfPage );
    if ( newPage != NULL ) self.pdfPage = CGPDFPageRetain( newPage );
}



// Draw the CGPDFPageRef into the layer at the correct scale.
- (void)drawLayer:(CALayer *)layer inContext:(CGContextRef)context
{

    // Fill the background with white.
    CGContextSetRGBFillColor(context, 1.0, 1.0, 1.0, 1.0);
    CGContextFillRect(context, self.bounds);

    // Print a blank page and return if our page is null.
    if ( _pdfPage == NULL )
    {
        return;
    }

    // save the cg state
    CGContextSaveGState(context);

    // Flip the context so that the PDF page is rendered right side up.
    CGContextTranslateCTM(context, 0.0, self.bounds.size.height);
    CGContextScaleCTM(context, 1.0, -1.0);

    // Scale the context so that the PDF page is rendered at the correct size for the zoom level.
    CGContextScaleCTM(context, self.myScale, self.myScale);

    // draw the page, restore and exit
    CGContextDrawPDFPage(context, self.pdfPage);
    CGContextRestoreGState(context);
}


@end
```

[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-PDFView.m.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-ModelController.h.md)

