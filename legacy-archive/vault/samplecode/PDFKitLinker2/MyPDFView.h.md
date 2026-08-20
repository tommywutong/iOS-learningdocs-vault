---
title: PDFKitLinker2
apple_id: DTS10003594
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-08-10'
source_url: https://developer.apple.com/library/archive/samplecode/PDFKitLinker2/Listings/MyPDFView_h.html
archived_at: '2026-07-18T03:18:26.192663Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PDFKitLinker2](PDFKitLinker2.md)


[Next](MyPDFView.m.md)[Previous](MyDocument.m.md)

# MyPDFView.h

```objc
// ======================================================================================================================
//  MyPDFView.h
// ======================================================================================================================


#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>


@interface MyPDFView : PDFView
{
    PDFAnnotationLink   *_activeAnnotation;
    PDFPage             *_activePage;
    NSRect              _wasBounds;
    NSPoint             _mouseDownLoc;
    NSPoint             _clickDelta;
    BOOL                _dragging;
    BOOL                _resizing;
    BOOL                _mouseDownInAnnotation;
}

- (void) transformContextForPage: (PDFPage *) page;

- (void) delete: (id) sender;
- (void) printDocument: (id) sender;

- (PDFAnnotationLink *) activeAnnotation;
- (void) setActiveAnnotation: (PDFAnnotationLink *) newLink;
- (NSSize) defaultNewLinkSize;
- (NSRect) resizeThumbForRect: (NSRect) rect rotation: (int) rotation;

@end
```

[Next](MyPDFView.m.md)[Previous](MyDocument.m.md)

